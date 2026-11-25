#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire pointless
meeting to /output/entry.txt. The line is one sentence, UTF-8, 1-200
characters, not only whitespace, so it passes the competition gate.
"""

import os

LINE = (
    "The update was in the email, the decision was in the email, "
    "and the only reason we're here is nobody read the email."
)


def main() -> None:
    text = LINE.strip()
    if not text:
        raise SystemExit("entry is empty")
    if len(text) > 200:
        raise SystemExit(f"entry is {len(text)} characters, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if sum(text.count(c) for c in ".!?") != 1:
        raise SystemExit("entry must be exactly one sentence")
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read it back and confirm the file holds exactly what we wrote.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry.txt does not match the line"
    print(f"Wrote {len(written)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
