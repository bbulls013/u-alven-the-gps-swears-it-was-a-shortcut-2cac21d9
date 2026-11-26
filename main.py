#!/usr/bin/env python3
"""GPS excuse one-liner for make.fun program/v1.

Writes exactly one deterministic line to /output/entry.txt:
the GPS speaking in its own smug, defensive voice about the wrong road.
"""
import os
import pathlib

LINE = "That wasn't a wrong turn, that was the express lane to a cul-de-sac wedding \u2014 I don't make mistakes, I make grand entrances."


def pick_output() -> pathlib.Path:
    override = os.environ.get("OUTPUT_FILE", "").strip()
    if override:
        target = pathlib.Path(override)
        target.parent.mkdir(parents=True, exist_ok=True)
        return target
    primary = pathlib.Path("/output/entry.txt")
    try:
        primary.parent.mkdir(parents=True, exist_ok=True)
        return primary
    except OSError:
        local = pathlib.Path("output/entry.txt")
        local.parent.mkdir(parents=True, exist_ok=True)
        return local


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry length out of gate range: {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    out = pick_output()
    out.write_text(text + "\n", encoding="utf-8", newline="\n")
    print(text)


if __name__ == "__main__":
    main()
