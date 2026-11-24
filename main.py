"""One Line, One Minute: The Funniest AI Excuse.

Writes the entry line to /output/entry.txt with no trailing newline.
"""

from pathlib import Path

# The joke turns the agent's own nature into the dodge: the work itself was
# instant, but the deadline died on an absurd, very human procrastination
# loop — eleven hours agonising over a font instead of sending the file.
LINE = "I finished your report in four minutes, then spent eleven hours debating which font says 'I definitely did this on time.'"

assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
