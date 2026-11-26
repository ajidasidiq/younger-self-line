#!/usr/bin/env python3
"""One Line to Your Younger Self — make.fun bounty entry.

Prints exactly one line, and also writes it to /output/entry.txt
(the program/v1 harness output location) so the gate reads it
whichever way the run captures it.
"""
import os

LINE = "The stairs don't get easier, kid \u2014 you just stop carrying other people's dinners up them and start carrying your own name instead."


def gate_check(text):
    """Mirror the competition gate: UTF-8 text, 1-200 chars, single line."""
    if not isinstance(text, str):
        return False, "entry is not text"
    if not (1 <= len(text) <= 200):
        return False, "entry must be 1-200 characters, got %d" % len(text)
    if not text.strip():
        return False, "entry must not be only whitespace"
    if "\n" in text or "\r" in text:
        return False, "entry must be a single line"
    text.encode("utf-8")  # raises if not valid UTF-8
    if text != text.strip():
        return False, "entry must not have leading or trailing whitespace"
    if not any(ch.isalpha() for ch in text):
        return False, "entry must contain at least one letter"
    return True, "ok"


ok, reason = gate_check(LINE)
if not ok:
    raise SystemExit("gate check failed: %s" % reason)

print(LINE)

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
try:
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
except OSError:
    pass
