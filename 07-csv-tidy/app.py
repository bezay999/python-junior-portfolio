import argparse
import csv
from pathlib import Path


def tidy_rows(rows):
    if not rows:
        raise ValueError("CSV file is empty")
    header = [" ".join(cell.split()) for cell in rows[0]]
    if not header or any(not cell for cell in header):
        raise ValueError("Header cells cannot be empty")
    if len({cell.casefold() for cell in header}) != len(header):
        raise ValueError("Header names must be unique")
    cleaned = [header]
    seen = set()
    removed = 0
    for number, row in enumerate(rows[1:], 2):
        if not row:
            removed += 1
            continue
        if len(row) != len(header):
            raise ValueError(f"Row {number} has {len(row)} cells; expected {len(header)}")
        values = [" ".join(cell.split()) for cell in row]
        if not any(values):
            removed += 1
            continue
        key = tuple(value.casefold() for value in values)
        if key in seen:
            removed += 1
            continue
        seen.add(key)
        cleaned.append(values)
    return cleaned, removed


def clean_file(source, destination):
    if source.resolve() == destination.resolve() or destination.exists():
        raise ValueError("Choose a new output path; the input and existing files are never overwritten")
    with source.open(newline="", encoding="utf-8-sig") as file:
        rows = list(csv.reader(file))
    cleaned, removed = tidy_rows(rows)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", newline="", encoding="utf-8") as file:
        csv.writer(file).writerows(cleaned)
    return len(cleaned) - 1, removed


def main():
    parser = argparse.ArgumentParser(description="Write a tidier copy of a CSV file")
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    try:
        kept, removed = clean_file(args.source, args.output)
    except (OSError, csv.Error, ValueError) as error:
        parser.error(str(error))
    print(f"Wrote {kept} rows to {args.output}; removed {removed} empty or repeated rows.")


if __name__ == "__main__":
    main()
