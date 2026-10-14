import argparse
from collections import defaultdict
import hashlib
from pathlib import Path


def digest(path):
    hasher = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def find_duplicates(root):
    by_size = defaultdict(list)
    errors = []
    for path in root.rglob("*"):
        if path.is_symlink() or not path.is_file():
            continue
        try:
            by_size[path.stat().st_size].append(path)
        except OSError as error:
            errors.append(f"{path}: {error}")

    by_hash = defaultdict(list)
    for paths in by_size.values():
        if len(paths) < 2:
            continue
        for path in paths:
            try:
                by_hash[digest(path)].append(path)
            except OSError as error:
                errors.append(f"{path}: {error}")
    groups = {key: sorted(paths) for key, paths in by_hash.items() if len(paths) > 1}
    return groups, errors


def main():
    parser = argparse.ArgumentParser(description="Report identical files without deleting them")
    parser.add_argument("folder", type=Path)
    args = parser.parse_args()
    if not args.folder.is_dir():
        parser.error("folder must exist and be a directory")

    groups, errors = find_duplicates(args.folder)
    if not groups:
        print("No duplicates found.")
    for file_hash, paths in sorted(groups.items()):
        print(f"\n{file_hash[:12]} ({len(paths)} copies)")
        for path in paths:
            print(f"  {path}")
    for error in errors:
        print(f"Could not read {error}")


if __name__ == "__main__":
    main()
