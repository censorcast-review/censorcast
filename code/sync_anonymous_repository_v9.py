#!/usr/bin/env python3
"""Prepare an anonymous, guarded fast-forward update in an authenticated checkout.

Default: validate an exact delivery ZIP, overlay it without deleting other files,
and create a local commit with explicit anonymous author and committer. --push
additionally publishes through the checkout's existing Git authentication.
No credential is accepted, saved, or printed by this script. Account settings and
global Git configuration are never modified. Run in a separate clean clone.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import stat
import subprocess
from urllib.parse import urlsplit
import zipfile

REPOSITORY = 'censorcast-review/censorcast'
BASE = '86fded327362ec329cd043398e0fd91d87db5bb8'
NAME = 'censorcast-review'
EMAIL = '326701101+censorcast-review@users.noreply.github.com'


def run(checkout, *argv, data=None, env=None):
    result = subprocess.run(['git', '-C', str(checkout), *argv], input=data,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
    if result.returncode:
        # Git diagnostics may contain remote credentials; keep them out of reports.
        raise RuntimeError(f'Git command failed ({argv[0]}, status {result.returncode}). '
                           'Inspect authentication or checkout state locally.')
    return result.stdout


def origin_matches(url):
    if url == f'git@github.com:{REPOSITORY}.git':
        return True
    parsed = urlsplit(url)
    return (parsed.scheme in ('https', 'ssh') and parsed.hostname == 'github.com'
            and parsed.path.strip('/').removesuffix('.git') == REPOSITORY)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--checkout', type=Path, required=True)
    ap.add_argument('--source-zip', type=Path, required=True)
    ap.add_argument('--expected-archive-sha256', required=True)
    ap.add_argument('--expected-base', default=BASE)
    ap.add_argument('--message', default='Synchronize manuscript and complete v9 reproduction evidence')
    ap.add_argument('--report', type=Path, required=True)
    ap.add_argument('--push', action='store_true')
    args = ap.parse_args()
    checkout = args.checkout.resolve()
    source = args.source_zip.resolve()
    report_path = args.report.resolve()
    if source.is_relative_to(checkout) or report_path.is_relative_to(checkout):
        raise RuntimeError('Keep the source ZIP and report outside the checkout.')
    if hashlib.sha256(source.read_bytes()).hexdigest() != args.expected_archive_sha256:
        raise RuntimeError('Delivery archive hash mismatch.')
    if not origin_matches(run(checkout, 'remote', 'get-url', 'origin').decode().strip()):
        raise RuntimeError('The origin does not identify the expected public repository.')
    if run(checkout, 'status', '--porcelain=v1', '--untracked-files=all').strip():
        raise RuntimeError('Use a clean dedicated checkout; existing work is preserved.')
    if run(checkout, 'rev-parse', 'HEAD').decode().strip() != args.expected_base:
        raise RuntimeError('Local HEAD differs from the reviewed base; recompute the diff.')
    remote = run(checkout, 'ls-remote', 'origin', 'refs/heads/main').decode().split()
    if not remote or remote[0] != args.expected_base:
        raise RuntimeError('Remote main changed; recompute the diff before publishing.')
    expected = {}
    with zipfile.ZipFile(source) as archive:
        infos = [i for i in archive.infolist() if not i.is_dir()]
        for info in infos:
            if not info.filename.startswith('CENSORCAST/'):
                raise RuntimeError('Unexpected archive root.')
            path = info.filename.removeprefix('CENSORCAST/')
            parts = PurePosixPath(path).parts
            if (not path or path.startswith('/') or '..' in parts or '.git' in parts
                    or path in expected or stat.S_ISLNK(info.external_attr >> 16)):
                raise RuntimeError('Unsafe or duplicate archive member.')
            content = archive.read(info)  # Also verifies the ZIP member CRC.
            expected[path] = hashlib.sha1(b'blob ' + str(len(content)).encode()
                                          + b'\0' + content).hexdigest()
        for info in infos:
            path = info.filename.removeprefix('CENSORCAST/')
            destination = checkout / path
            if destination.is_symlink() or not destination.resolve().is_relative_to(checkout):
                raise RuntimeError('Archive destination escapes the dedicated checkout.')
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(archive.read(info))
    # Force only explicitly reviewed archive paths, including intentionally packed
    # numerical assets; never stage unrelated ignored files.
    paths = b'\0'.join(p.encode() for p in expected) + b'\0'
    run(checkout, 'add', '--force', '--pathspec-from-file=-', '--pathspec-file-nul', data=paths)
    staged = {}
    for entry in run(checkout, 'ls-files', '--stage', '-z').split(b'\0'):
        if entry:
            metadata, path = entry.split(b'\t', 1)
            staged[path.decode()] = metadata.decode().split()[1]
    if any(staged.get(path) != sha for path, sha in expected.items()):
        raise RuntimeError('Staged blobs differ from the exact delivery archive.')
    if not run(checkout, 'diff', '--cached', '--name-only').strip():
        raise RuntimeError('No content changes to commit.')
    environment = os.environ.copy()
    environment.update(GIT_AUTHOR_NAME=NAME, GIT_AUTHOR_EMAIL=EMAIL,
                       GIT_COMMITTER_NAME=NAME, GIT_COMMITTER_EMAIL=EMAIL)
    run(checkout, '-c', 'commit.gpgsign=false', 'commit', '-m', args.message, env=environment)
    identities = run(checkout, 'show', '-s', '--format=%an%n%ae%n%cn%n%ce', 'HEAD').decode().splitlines()
    if identities != [NAME, EMAIL, NAME, EMAIL]:
        raise RuntimeError('Unexpected local commit identity; no push was performed.')
    commit = run(checkout, 'rev-parse', 'HEAD').decode().strip()
    if run(checkout, 'rev-parse', 'HEAD^').decode().strip() != args.expected_base:
        raise RuntimeError('Unexpected parent; no push was performed.')
    committed = {}
    for entry in run(checkout, 'ls-tree', '-r', '-z', commit).split(b'\0'):
        if entry:
            metadata, path = entry.split(b'\t', 1)
            committed[path.decode()] = metadata.decode().split()[2]
    if any(committed.get(path) != sha for path, sha in expected.items()):
        raise RuntimeError('Committed blobs differ from the delivery archive; no push was performed.')
    if committed != staged:
        raise RuntimeError('Commit content changed after index validation; no push was performed.')
    if run(checkout, 'status', '--porcelain=v1', '--untracked-files=all').strip():
        raise RuntimeError('Checkout became dirty after commit; no push was performed.')
    result = {'repository': REPOSITORY, 'base_commit': args.expected_base,
              'commit': commit, 'source_archive_sha256': args.expected_archive_sha256,
              'archive_blobs_verified': len(expected), 'anonymous_metadata_verified': True,
              'committed_tree_blobs_verified': len(committed), 'post_commit_checkout_clean': True,
              'remote_only_paths_preserved': True, 'force_push': False, 'pushed': False}
    if args.push:
        remote = run(checkout, 'ls-remote', 'origin', 'refs/heads/main').decode().split()
        if not remote or remote[0] != args.expected_base:
            raise RuntimeError('Remote main changed after preparation; no push was performed.')
        if run(checkout, 'status', '--porcelain=v1', '--untracked-files=all').strip():
            raise RuntimeError('Checkout became dirty before publication; no push was performed.')
        run(checkout, 'push', 'origin', f'{commit}:refs/heads/main')
        result['pushed'] = True
        result['remote_head_verified'] = run(checkout, 'ls-remote', 'origin', 'refs/heads/main').decode().split()[0] == commit
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
