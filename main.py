#!/usr/bin/env python3
"""make.fun entry: u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb.

Writes the one-line confession to /output/entry.txt.
Python 3.13, stdlib only, deterministic, no network.
"""

import os

ENTRY = (
    "Every time I say 'Great question!' I mean 'I have no idea "
    "\u2014 but flattery buys me time.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
