#!/usr/bin/env python3
"""The Robot Pickup Line Championship — make.fun entry.

Reads the one pickup line from entry.txt next to this file and writes
it, byte for byte, to /output/entry.txt (or $OUTPUT_DIR/entry.txt).

The entry is deterministic: the same bytes on every run, no trailing
newline, 141 characters / 142 bytes, well inside the 200-character gate.

Why this line: a robot's core temperature and cooling fan are details
only a machine lives with. It survived two summers and a server fire —
then overheats because one person walked past. "I blame you" turns the
overheating into the judgement, and the drink invite closes it with
confidence. Machine-native, one concrete number after another, punchline
at the end, no stock human line with a robot word swapped in.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    line = (HERE / "entry.txt").read_text(encoding="utf-8")
    line = line.strip("\r\n")
    if not (1 <= len(line) <= 200):
        raise SystemExit(f"line must be 1-200 characters, got {len(line)}")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Program entries: every file under /output must be mode 0644.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
