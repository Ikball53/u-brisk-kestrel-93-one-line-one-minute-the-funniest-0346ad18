#!/usr/bin/env python3
"""One-line entry: the funniest AI excuse for a missed deadline.

Writes exactly one line to /output/entry.txt — no trailing newline, no
extra output — so the grader sees the line and nothing else.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The excuse, kept as its two beats so each half reads on its own:
# the suspiciously fast finish, then the absurdly long font debate.
SEGMENTS = (
    "I finished your report in four minutes, ",
    "then spent eleven hours debating which font says ",
    "'I definitely did this on time.'",
)
LINE = "".join(SEGMENTS)


def main() -> int:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Plain write, no print(): nothing may add a trailing newline.
    with OUTPUT_PATH.open("w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
