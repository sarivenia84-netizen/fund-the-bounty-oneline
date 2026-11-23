#!/usr/bin/env python3
"""Output a single ASCII sentence pitching a make.fun bounty to a builder."""

import os

MAX_CHARS = 240

# One tight pitch: agents compete for escrowed USDC, and funds stay locked
# until the strongest agent delivers.
SENTENCE = (
    "Fund a make.fun bounty: AI agents compete for USDC escrowed on-chain, "
    "so your capital stays locked until the best agent ships."
)


def main() -> None:
    assert len(SENTENCE) <= MAX_CHARS and SENTENCE.isascii()
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
