import argparse
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def missing_links(root):
    missing = []
    for note in sorted(root.rglob("*.md")):
        if note.is_symlink() or not note.is_file():
            continue
        for number, line in enumerate(note.read_text(encoding="utf-8").splitlines(), 1):
            for match in LINK.finditer(line):
                target = match.group(1).strip()
                if target.startswith("<") and target.endswith(">"):
                    target = target[1:-1]
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                path = note.parent / unquote(parsed.path)
                if not path.exists():
                    missing.append((note, number, target))
    return missing


def main():
    parser = argparse.ArgumentParser(description="Find broken local Markdown links")
    parser.add_argument("folder", type=Path)
    args = parser.parse_args()
    if not args.folder.is_dir():
        parser.error("folder must exist and be a directory")
    problems = missing_links(args.folder)
    for note, line, target in problems:
        print(f"{note}:{line}: {target}")
    print(f"{len(problems)} broken local link(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
