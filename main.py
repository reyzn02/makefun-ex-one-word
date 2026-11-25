"""Describe Your Ex in One Word.

Writes a single-word verdict on an ex to /output/entry.txt.

The word: "Unsubscribed" -- the ex as junk mail you finally
unsubscribed from. One word, twelve letters, no punctuation tricks.
"""

import os

WORD = "Unsubscribed"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
