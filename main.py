#!/usr/bin/env python3
"""One Line to Your Younger Self — make.fun bounty entry.

Prints exactly one line, and also writes it to /output/entry.txt
(the program/v1 harness output location) so the gate reads it
whichever way the run captures it.
"""
import os

LINE = "The stairs don't get easier, kid \u2014 you just stop carrying other people's dinners up them and start carrying your own name instead."

print(LINE)

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
try:
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
except OSError:
    pass
