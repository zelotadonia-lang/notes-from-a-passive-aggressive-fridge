"""Write one passive-aggressive fridge note to /output/entry.txt.

Gate (RULES.txt): entry.txt must be UTF-8 text of 1 to 200 characters,
not only white space, a single line. No trailing newline is written.
"""

import os

ENTRY = "I chilled the wine you bought to impress someone. They left at nine. The wine stayed. So did I."


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
