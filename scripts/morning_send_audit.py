#!/usr/bin/env python3
"""
morning_send_audit.py — the outreach engine's self-audit.

The schedule says what was *supposed* to send. The send log says what
*actually* sent. This script compares the two every morning and flags any
lane that under-fired, so a dead lane is caught the same day instead of at
the end of the month.

Inputs:
    schedule.csv: date,lane,expected_count
    sends.csv:    date,lane,sent_count

Usage:
    python3 morning_send_audit.py schedule.csv sends.csv
Exit code 1 if any lane missed, 0 if every lane fired as scheduled.
"""

import csv
import sys
from collections import defaultdict


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    schedule, sends = load(sys.argv[1]), load(sys.argv[2])

    actual = defaultdict(int)
    for s in sends:
        actual[(s["date"], s["lane"])] += int(s["sent_count"])

    misses = []
    for row in schedule:
        key = (row["date"], row["lane"])
        expected = int(row["expected_count"])
        got = actual.get(key, 0)
        status = "OK  " if got >= expected else "MISS"
        if got < expected:
            misses.append(key)
        print(f"{status} {row['date']}  {row['lane']:<18} expected {expected:>3}  sent {got:>3}")

    if misses:
        print(f"\n{len(misses)} lane(s) under-fired. Investigate today.")
        sys.exit(1)
    print("\nAll lanes fired as scheduled.")


if __name__ == "__main__":
    main()
