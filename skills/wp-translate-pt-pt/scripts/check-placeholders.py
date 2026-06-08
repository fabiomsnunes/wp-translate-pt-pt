#!/usr/bin/env python3
"""Checks placeholder parity between msgid and msgstr in a .po file.

printf placeholders (%s, %d, %1$s, ...) must be exactly the same in the original
and in the translation — they may change order, but must not disappear, appear, or
change type. A broken placeholder blows up the string in production.

Usage:
    python3 check-placeholders.py FILE.po

Exits 0 if everything matches, 1 if there are mismatches (useful in CI).
"""
import re
import sys

PLACEHOLDER = re.compile(r"%(\d+\$)?[sd]")


def _unquote(line):
    return re.sub(r'^"(.*)"$', r"\1", line.strip())


def _collect(lines, index, key):
    value = _unquote(lines[index].split(key, 1)[1])
    index += 1
    while index < len(lines) and lines[index].startswith('"'):
        value += _unquote(lines[index])
        index += 1
    return value, index


def parse_pairs(path):
    with open(path, encoding="utf-8") as handle:
        lines = handle.readlines()

    pairs, index = [], 0
    while index < len(lines):
        if lines[index].startswith("msgid "):
            msgid, index = _collect(lines, index, "msgid ")
            while index < len(lines) and not lines[index].startswith("msgstr"):
                index += 1
            if index < len(lines):
                msgstr, index = _collect(lines, index, "msgstr ")
                pairs.append((msgid, msgstr))
        else:
            index += 1
    return pairs


def main(path):
    pairs = parse_pairs(path)
    failures = 0
    for msgid, msgstr in pairs:
        if not msgid or not msgstr:
            continue
        expected = sorted(m.group(0) for m in PLACEHOLDER.finditer(msgid))
        got = sorted(m.group(0) for m in PLACEHOLDER.finditer(msgstr))
        if expected != got:
            failures += 1
            print(f"MISMATCH: {msgid[:60]!r}\n  msgid : {expected}\n  msgstr: {got}")

    checked = len([p for p in pairs if p[0]])
    if failures:
        print(f"FAIL: {failures} divergência(s) em {checked} strings.")
        return 1
    print(f"PASS: placeholders idênticos ({checked} strings verificadas).")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
