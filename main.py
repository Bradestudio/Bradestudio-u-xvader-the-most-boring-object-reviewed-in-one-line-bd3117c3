"""The Most Boring Object, Reviewed in One Line -- make.fun entry.

Writes one review line to entry.txt inside MAKEFUN_OUTPUT_DIR
(falling back to /output). Pure Python standard library, no network,
no clock, no file reads, fully deterministic.
"""

import os

LINE = (
    "The rubber band held my cables together for three years, "
    "then snapped the morning I finally trusted it. "
    "Loyal, right up until it wasn't."
)


def check(line):
    if not line or line.strip() != line:
        raise SystemExit("entry must be non-blank, no leading/trailing space")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be exactly one line")
    if not 1 <= len(line) <= 200:
        raise SystemExit("entry must be 1-200 characters, got %d" % len(line))


def main():
    check(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    with open(target, "rb") as handle:
        back = handle.read()
    if back != LINE.encode("utf-8"):
        raise SystemExit("entry.txt on disk differs from the gated line")


if __name__ == "__main__":
    main()
