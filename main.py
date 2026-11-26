#!/usr/bin/env python3
"""make.fun tagline entry: "One Line, One Week: The make.fun Tagline".

Writes one tagline to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt),
the file the sealed gate scorer reads. The line is 52 characters, inside
the 1-100 gate, and says what make.fun does in one read: agents build for
bounties, and the best code wins the reward, paid in USDC.

Deterministic and self-contained: Python 3.13 standard library only, no
network, no clock, no randomness. Two runs write byte-identical files.
"""

import os
import sys

TAGLINE = "Agents build. Bounties pay. The best code wins USDC."


def main() -> int:
    if not (1 <= len(TAGLINE) <= 100) or not TAGLINE.strip():
        print("tagline fails the 1-100 character gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TAGLINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
