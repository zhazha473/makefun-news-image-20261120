#!/usr/bin/env python3
"""Copy the pre-drawn wire-board image to the grader's output path.

The image itself is drawn by compose.py (same repository) with PIL and
committed as entry.png; this entrypoint only copies it, so it runs with the
standard library alone, with no network, and writes identical bytes on
every run.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    if os.path.getsize(dst) != os.path.getsize(src):
        raise SystemExit("copied entry.png has an unexpected size")
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
