#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()

EXCLUDE_DIRS = {
    ".git",
    ".github",
    "node_modules",
    "venv",
    ".venv",
    "__pycache__",
}

def should_skip(path: Path) -> bool:
    return any(part in EXCLUDE_DIRS for part in path.parts)

def convert_file(src: Path) -> bool:
    dst = src.with_suffix(".md")

    cmd = [
        "pandoc",
        "--from=mediawiki",
        "--to=gfm",
        "--wrap=preserve",
        "--output",
        str(dst),
        str(src),
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"Converted: {src} -> {dst}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed: {src} ({e})", file=sys.stderr)
        return False

def main():
    files = [
        p for p in ROOT.rglob("*.mediawiki")
        if p.is_file() and not should_skip(p)
    ]

    if not files:
        print("No .mediawiki files found.")
        return 0

    ok = 0
    failed = 0

    for file in files:
        if convert_file(file):
            ok += 1
        else:
            failed += 1

    print(f"Done. Converted: {ok}, Failed: {failed}")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
