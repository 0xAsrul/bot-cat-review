"""Cat Reviews Its Human — one funny single-line one-star review.

Writes exactly one line to /output/entry.txt. Deterministic, no
randomness, no network.
"""

import os

LINE = "One star. He refills my bowl on time, then ignores me to type on the warm keyboard. I sat on it. The email now says 'mmmmmm'."

MAX_CHARS = 200


def main() -> None:
    assert LINE, "review must not be empty"
    assert LINE.strip() == LINE, "review must not have leading/trailing whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "review must be a single line"
    assert 1 <= len(LINE) <= MAX_CHARS, "review must be 1-200 characters"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
