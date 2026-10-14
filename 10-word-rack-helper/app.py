import argparse
from collections import Counter
from pathlib import Path
import re


def find_words(rack, dictionary, min_length=3):
    letters = rack.lower()
    if not re.fullmatch(r"[a-z]+", letters):
        raise ValueError("Rack must contain English letters only")
    if min_length < 1:
        raise ValueError("Minimum length must be positive")
    available = Counter(letters)
    matches = set()
    for entry in dictionary:
        word = entry.strip().lower()
        if len(word) < min_length or not re.fullmatch(r"[a-z]+", word):
            continue
        if not Counter(word) - available:
            matches.add(word)
    return sorted(matches, key=lambda word: (-len(word), word))


def main():
    parser = argparse.ArgumentParser(description="Find words made from a rack of letters")
    parser.add_argument("dictionary", type=Path)
    parser.add_argument("rack")
    parser.add_argument("--min-length", type=int, default=3)
    args = parser.parse_args()
    try:
        entries = args.dictionary.read_text(encoding="utf-8").splitlines()
        words = find_words(args.rack, entries, args.min_length)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    if words:
        print("\n".join(words))
    else:
        print("No matching words found.")


if __name__ == "__main__":
    main()
