#!/usr/bin/env python3
"""One Word for Your Wi-Fi: writes the entry to /output/entry.txt.

Entry: "Ghosting" (8 characters).
Why this word: home Wi-Fi vanishes mid-call, mid-game, mid-download,
then comes back like nothing happened. It reads at once, needs no
explanation, and works as a network name.
"""

import os

ENTRY = "Ghosting"


def main():
    word = ENTRY.strip()
    assert 1 <= len(word) <= 20, "entry must be 1-20 characters"
    assert word and not word.isspace()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(word)


if __name__ == "__main__":
    main()
