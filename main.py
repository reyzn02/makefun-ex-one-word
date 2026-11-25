"""Describe Your Ex in One Word.

Writes a single-word verdict on an ex to /output/entry.txt.

The word: "Unsubscribed" -- the ex as junk mail you finally
unsubscribed from. One word, twelve letters, no punctuation tricks.
"""

import os

WORD = "Unsubscribed"

OUTPUT_PATH = "/output/entry.txt"


def validate(word: str) -> None:
    """Refuse anything that is not exactly one plain word (1-111 chars)."""
    if not (1 <= len(word) <= 111):
        raise ValueError("word must be 1-111 characters")
    if len(word.split()) != 1 or not word.isalpha():
        raise ValueError("entry must be exactly one word, letters only")


def main() -> None:
    validate(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
