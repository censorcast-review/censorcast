"""Bind an existing anonymous review URL, rebuild the paper, and update its hashes.

This command does not create a remote repository or certify its anonymity.
Verify the public URL and repository identity before running it.
Frozen experimental records are never modified.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
START = "% BEGIN ANONYMOUS REVIEW LINK"
END = "% END ANONYMOUS REVIEW LINK"


def validate_url(url):
    p = urlparse(url)
    if p.scheme != "https" or p.username or p.password or p.query or p.fragment:
        raise ValueError("Use a plain HTTPS repository URL without credentials or tracking parameters")
    if p.netloc not in {"github.com", "anonymous.4open.science"}:
        raise ValueError("Expected a GitHub or Anonymous GitHub review URL")
    if not re.fullmatch(r"/[A-Za-z0-9._/-]+", p.path):
        raise ValueError("Unexpected characters in repository URL")
    parts = [s for s in p.path.split("/") if s]
    if len(parts) < 2 or any(s.lower() in {"owner", "username", "example", "placeholder"} for s in parts):
        raise ValueError("Use the actual existing repository URL")
    return url.rstrip("/")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", required=True)
    args = parser.parse_args()
    url = validate_url(args.url)
    manifest_path = ROOT / "MANIFEST.json"
    manifest = json.loads(manifest_path.read_text())
    subprocess.run([sys.executable, str(ROOT / "code/verify_release.py")], check=True)
    tex_path = ROOT / "paper/main.tex"
    original = tex_path.read_text()
    if START in original:
        clean = re.sub(re.escape(START) + r".*?" + re.escape(END) + r"\n*", "", original, flags=re.S)
    else:
        clean = original
    block = (START + "\nThe anonymous repository at \\url{" + url + "} provides "
             "the manuscript source, experiment code, saved prediction arrays, and "
             "verification commands for the complete numerical replay.\n" + END + "\n\n")
    marker = r"\bibliography{references}"
    if clean.count(marker) != 1:
        raise ValueError("Expected one bibliography marker")
    tex_path.write_text(clean.replace(marker, block + marker))
    output = ROOT / "reproduction_outputs/review_link_build"
    try:
        subprocess.run([sys.executable, str(ROOT / "code/build_paper.py"), "--output", str(output)], check=True)
    except Exception:
        tex_path.write_text(original)
        raise
    shutil.copyfile(output / "CENSORCAST_ICLR_2027_Final.pdf", ROOT / "paper/CENSORCAST_ICLR_2027_Final.pdf")
    review = {"url": url, "status": "configured_and_compiled", "public_access_and_anonymity": "must be checked separately"}
    (ROOT / "REVIEW_LINK.json").write_text(json.dumps(review, indent=2) + "\n")
    for rel in ["paper/main.tex", "paper/CENSORCAST_ICLR_2027_Final.pdf", "REVIEW_LINK.json"]:
        p = ROOT / rel
        manifest["files"][rel] = {"sha256": hashlib.sha256(p.read_bytes()).hexdigest(), "bytes": p.stat().st_size, "numerical_asset": False}
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    subprocess.run([sys.executable, str(ROOT / "code/verify_release.py")], check=True)
    print("Paper link configured. Inspect the rendered PDF and verify anonymous public access before submission.")


if __name__ == "__main__":
    main()
