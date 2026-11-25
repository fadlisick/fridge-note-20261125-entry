"""Passive-aggressive fridge note: one line to /output/entry.txt.

The fridge has a camera, a door sensor and a long memory. The owner logged
a salad in a diet app; the fridge watched the truth happen standing up, in
the dark. The note says so, dryly, and stops there: no lecture, no follow-up,
just the appliance keeping score.
"""

import os
import sys

NOTE = (
    "Your diet app says you ate a salad. "
    "I watched you eat cake standing up, in the dark, like a raccoon."
)

LOWER = 1
UPPER = 200
FILE = "entry.txt"


def output_dir():
    """Where the grader wants the note: the harness folder, else /output."""
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return wanted if wanted else "/output"


def check_note(note):
    """A single non-blank line inside the 1-200 character gate."""
    if note != note.strip():
        raise ValueError("note has stray surrounding space")
    if not note:
        raise ValueError("note is blank")
    if "\n" in note or "\r" in note:
        raise ValueError("note must be one line")
    if len(note) < LOWER or len(note) > UPPER:
        raise ValueError(
            "note is %d characters, gate needs %d-%d"
            % (len(note), LOWER, UPPER)
        )
    return note


def leave_note(directory, note):
    """Write entry.txt, then read it back and confirm it matches."""
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, FILE)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(note)
    with open(target, encoding="utf-8") as handle:
        kept = handle.read()
    if kept != note:
        raise ValueError("entry.txt does not match the note")
    return target


def main():
    note = check_note(NOTE)
    target = leave_note(output_dir(), note)
    sys.stdout.write("left %s (%d chars)\n" % (target, len(note)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
