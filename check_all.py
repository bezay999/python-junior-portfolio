from pathlib import Path
import subprocess
import sys


def main():
    folders = sorted(path for path in Path(__file__).parent.glob("[0-9][0-9]-*") if path.is_dir())
    failed = []
    for folder in folders:
        print(f"\n{folder.name}", flush=True)
        result = subprocess.run([sys.executable, "-m", "unittest", "discover", "-v"], cwd=folder)
        if result.returncode:
            failed.append(folder.name)
    print(f"\n{len(folders) - len(failed)}/{len(folders)} projects passed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
