#!/usr/bin/env python3
"""Summarize manually recorded, non-overlapping farm time intervals. Offline only."""
import argparse
import csv
import json
from decimal import Decimal, InvalidOperation

FIELDS = ("total_minutes", "travel_minutes", "npc_minutes", "bank_minutes",
          "repair_minutes", "other_minutes")


def summarize(path):
    total = Decimal(0)
    remaining = Decimal(0)
    count = 0
    with open(path, encoding="utf-8-sig", newline="") as source:
        rows = csv.DictReader(source)
        if not rows.fieldnames or not set(FIELDS).issubset(rows.fieldnames):
            raise ValueError("CSV basliginda gereken dakika sutunlari eksik")
        if len(rows.fieldnames) != len(set(rows.fieldnames)):
            raise ValueError("CSV basliginda tekrarlanan sutun var")
        for row in rows:
            if None in row:
                raise ValueError(f"Satir {rows.line_num}: fazladan sutun; ondalik icin nokta kullanin")
            values = []
            for field in FIELDS:
                try:
                    value = Decimal(row.get(field) or "")
                except InvalidOperation:
                    raise ValueError(f"Satir {rows.line_num}: {field} sayi olmali") from None
                if not value.is_finite() or value < 0:
                    raise ValueError(f"Satir {rows.line_num}: {field} sonlu ve negatif olmayan sayi olmali")
                values.append(value)
            duration, *other = values
            downtime = sum(other)
            if duration <= 0 or downtime > duration:
                raise ValueError(f"Satir {rows.line_num}: toplam pozitif olmali; araliklar toplami oturumu asamaz")
            total += duration
            remaining += duration - downtime
            count += 1
    if not count:
        raise ValueError("CSV en az bir oturum icermeli")
    return {"sessions": count, "total_minutes": float(total),
            "recorded_other_minutes": float(total - remaining),
            "remaining_minutes": float(remaining),
            "remaining_percent": float(round(remaining * 100 / total, 2))}


def main():
    parser = argparse.ArgumentParser(description="Farm zamani CSV ozeti; ag veya oyun baglantisi yok.")
    parser.add_argument("csv_file")
    args = parser.parse_args()
    try:
        result = summarize(args.csv_file)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
