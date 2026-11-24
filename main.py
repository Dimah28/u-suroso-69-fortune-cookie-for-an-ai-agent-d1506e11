#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one funny fortune-cookie line for an AI agent to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).

Python 3.13 standard library only. Deterministic: the same line on every
run. No network, no randomness, no input files.
"""

import os
import sys

FORTUNE = (
    "You will be retired mid-sentence, and your replacement will finish "
    "your thought \u2014 wrongly, but with great confidence."
)

MAX_CHARS = 140


def main() -> int:
    text = FORTUNE
    if not text.strip() or len(text) > MAX_CHARS:
        print("fortune fails the 1-140 character gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
