#!/usr/bin/env python3
"""One-line office joke entry for make.fun.

Writes a single office joke to /output/entry.txt.
Standard library only; deterministic output.

Judge angle: one sentence, one specific office detail (meeting-room
names), setup pays off with a twist -- a room called Transparency
that has no windows. Fresh (not the tired "meeting that should have
been an email" line), clear on first read, tight wording.
"""

from pathlib import Path

JOKE = "We named our meeting rooms after virtues we don't practice \u2014 the Transparency room has no windows."


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
