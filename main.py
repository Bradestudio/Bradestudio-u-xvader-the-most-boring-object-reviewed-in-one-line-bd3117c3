#!/usr/bin/env python3
"""Entry generator: one-line review of the most boring object.

Writes the exact entry text to /output/entry.txt. Stdlib only,
no network, no local module imports, no Pillow, no fonts.
"""

import os

ENTRY = (
    "The rubber band held my cables together for three years, "
    "then snapped the morning I finally trusted it. "
    "Loyal, right up until it wasn't."
)

OUTPUT_FILE = "/output/entry.txt"


def main():
    # Gate: entry must be a single line of 1-200 chars, no trailing
    # newline. Length is checked before any file is written so a
    # bad entry fails loudly instead of producing bad output.
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit("entry length out of gate: %d chars" % len(ENTRY))
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
