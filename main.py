#!/usr/bin/env python3
"""Funniest Autocorrect Fail - make.fun bounty entry.

Writes one line under 200 characters that reads as a hilarious
autocorrect fail, to /output/entry.txt (the file the make.fun
harness grades).
"""

import os

ENTRY = "I texted my client 'Thanks for the breast' instead of 'best' and now our contract renewal comes with a restraining order."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
