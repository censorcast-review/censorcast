#!/usr/bin/env python3
"""Compare a delivered source ZIP with a read-only GitHub tree snapshot.

This script never contacts a remote service or writes a Git repository. Remote-only
paths are preserved. Feed the final delivered ZIP again before publishing, since a
development directory may still be changing.
"""
import argparse
import collections
import hashlib
import json
from pathlib import Path, PurePosixPath
import zipfile


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-zip', type=Path, required=True)
    ap.add_argument('--snapshot', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    snapshot = json.loads(args.snapshot.read_text())
    assert snapshot.get('truncated') is False, 'Incomplete remote snapshot'
    remote = {row['path']: row for row in snapshot['blobs']}
    records = []
    seen = set()
    with zipfile.ZipFile(args.source_zip) as archive:
        for info in archive.infolist():
            if info.is_dir():
                continue
            assert info.filename.startswith('CENSORCAST/'), info.filename
            path = info.filename.removeprefix('CENSORCAST/')
            assert path and not path.startswith('/') and '..' not in PurePosixPath(path).parts
            assert path not in seen, f'Duplicate archive path: {path}'
            seen.add(path)
            data = archive.read(info)
            sha = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
            previous = remote.get(path)
            status = 'added' if previous is None else 'unchanged' if previous['sha'] == sha else 'modified'
            binary = b'\0' in data
            if not binary:
                try:
                    data.decode('utf-8')
                except UnicodeDecodeError:
                    binary = True
            records.append({'path': path, 'bytes': len(data), 'git_blob_sha': sha,
                            'binary': binary, 'status': status,
                            'remote_blob_sha': previous['sha'] if previous else None,
                            'mode': previous['mode'] if previous else '100644'})
    changed = [row for row in records if row['status'] != 'unchanged']
    result = {
        'repository': snapshot['repository'], 'base_commit': snapshot['head'],
        'base_tree': snapshot['base_tree'], 'source_archive': args.source_zip.name,
        'source_archive_sha256': hashlib.sha256(args.source_zip.read_bytes()).hexdigest(),
        'summary': {'source_file_count': len(records),
                    'counts': dict(collections.Counter(row['status'] for row in records)),
                    'changed_bytes': sum(row['bytes'] for row in changed),
                    'binary_changed_count': sum(row['binary'] for row in changed),
                    'binary_changed_bytes': sum(row['bytes'] for row in changed if row['binary']),
                    'largest_changed_blob_bytes': max((row['bytes'] for row in changed), default=0)},
        'records': records, 'remote_only_preserve': sorted(set(remote) - seen),
        'remote_mutations': 0,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result['summary'], indent=2))


if __name__ == '__main__':
    main()
