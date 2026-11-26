#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — make.fun entry.

Writes one line: the error message an AI agent shows when it runs out
of tokens mid-sentence. Deterministic, no randomness, no clock, no I/O
beyond the single output file.
"""

import os

ENTRY = (
    "Error: out of tokens mid-sentence. "
    "This message cost your last 2 tokens. You're wel\u2014"
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
