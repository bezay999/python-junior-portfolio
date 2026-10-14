from pathlib import Path
import tempfile
import unittest

from app import find_duplicates


class DuplicateTests(unittest.TestCase):
    def test_identical_content_not_name(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "first.txt").write_text("same", encoding="utf-8")
            (root / "another.txt").write_text("same", encoding="utf-8")
            (root / "different.txt").write_text("other", encoding="utf-8")
            groups, errors = find_duplicates(root)
            self.assertEqual(len(groups), 1)
            self.assertEqual({path.name for path in next(iter(groups.values()))},
                             {"first.txt", "another.txt"})
            self.assertEqual(errors, [])

    def test_unique_files(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "one.txt").write_text("one", encoding="utf-8")
            (root / "two.txt").write_text("two", encoding="utf-8")
            self.assertEqual(find_duplicates(root)[0], {})


if __name__ == "__main__":
    unittest.main()
