#!/usr/bin/env python3
"""Funniest Autocorrect Fail - make.fun bounty entry.

Writes one line under 200 characters that reads as a hilarious
autocorrect fail, to /output/entry.txt (the file the make.fun
harness grades).

The entry itself lives in ENTRY_LINE and is returned verbatim by
get_entry(); main() only handles the output directory and the write.
"""

import os

# The graded one-line entry, kept verbatim.
ENTRY_LINE = "I texted my client 'Thanks for the breast' instead of 'best' and now our contract renewal comes with a restraining order."

def get_entry() -> str:
    """Return the graded one-line entry, unchanged, for entry.txt."""
    return ENTRY_LINE

def main() -> None:
    # MAKEFUN_OUTPUT_DIR is set by the harness; default /output for local runs.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(get_entry())

if __name__ == "__main__":
    main()
