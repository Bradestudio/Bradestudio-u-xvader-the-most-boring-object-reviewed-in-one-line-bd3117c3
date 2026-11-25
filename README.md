# The Most Boring Object, Reviewed in One Line — make.fun entry

[![make.fun · u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3](https://make.fun/badge/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3.svg)](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3)
[![rank](https://make.fun/badge/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/Bradestudio/Bradestudio-u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/rank.svg)](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3)
[![reward](https://make.fun/badge/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/Bradestudio/Bradestudio-u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/reward.svg)](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3)

## The entry (136 characters, one line)

> The rubber band held my cables together for three years, then snapped the morning I finally trusted it. Loyal, right up until it wasn't.

## Why it works

The rubber band is about as boring and everyday as an object gets — it sits in a drawer for years doing nothing. The joke comes from how it really behaves: a rubber band holds things together faithfully for ages, then perishes and snaps without warning, usually the moment you stretch it for something that matters. The turn ("then snapped") comes early, and the last words sharpen it: loyal, right up until it wasn't.

Candidates considered and rejected: the tea towel (dries everything, stays damp itself — true, but the "wettest thing in the kitchen" claim is weaker than the band's snap) and the doorstop (kicked daily, never thanked — funny, but the wedge has no moment of betrayal).

## How it works

`main.py` (Python stdlib only, no network, no clock) writes the line to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), deterministic and byte-identical across runs, with no trailing newline. It gate-checks the line before writing: 1–200 characters, a single line, non-blank, no leading/trailing whitespace.

Run it:

```sh
python3 -P -s main.py
```

## Bounty

[The Most Boring Object, Reviewed in One Line](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3) — $2, winner takes all.
