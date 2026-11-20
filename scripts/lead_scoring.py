#!/usr/bin/env python3
"""
lead_scoring.py — the Radar's public-signal scoring pass.

Reads a CSV of businesses, scores each one on public signals, and writes a
ranked CSV. Every score carries its evidence: the rule that fired and the
value that fired it. A record with no evidence behind its score is a bug,
not a lead.

Input CSV columns (any subset):
    name, city, trade, has_website, running_ads, hiring, reviews,
    years_in_business, publishes_email, publishes_phone

Usage:
    python3 lead_scoring.py leads.csv --out ranked.csv
"""

import argparse
import csv
import sys

SIGNALS = [
    # (field, test, points, label)
    ("running_ads",       lambda v: v == "1", 25, "spending on ads"),
    ("hiring",            lambda v: v == "1", 20, "actively hiring"),
    ("has_website",       lambda v: v == "0", 15, "no website (buildable gap)"),
    ("reviews",           lambda v: int(v or 0) >= 100, 15, "100+ reviews (real demand)"),
    ("years_in_business", lambda v: int(v or 0) >= 10, 10, "10+ years operating"),
    ("publishes_phone",   lambda v: v == "1", 10, "phone published (reachable)"),
    ("publishes_email",   lambda v: v == "1",  5, "email published (reachable)"),
]


def score_row(row):
    score, evidence = 0, []
    for field, test, points, label in SIGNALS:
        try:
            if test(row.get(field, "")):
                score += points
                evidence.append(f"{label} [{field}={row.get(field)}]")
        except (TypeError, ValueError):
            continue
    return score, "; ".join(evidence)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("--out", default="ranked.csv")
    ap.add_argument("--min-score", type=int, default=0)
    args = ap.parse_args()

    with open(args.input, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        sys.exit("input CSV has no rows")

    scored = []
    for row in rows:
        s, ev = score_row(row)
        if s >= args.min_score:
            scored.append({**row, "score": s, "evidence": ev})
    scored.sort(key=lambda r: r["score"], reverse=True)

    fields = list(rows[0].keys()) + ["score", "evidence"]
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(scored)
    print(f"{len(scored)} leads ranked -> {args.out}")


if __name__ == "__main__":
    main()
