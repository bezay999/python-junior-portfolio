from pathlib import Path
import tempfile
import unittest

from app import missing_links


class LinkTests(unittest.TestCase):
    def test_local_missing_and_external_links(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "guide.md").write_text("# Guide", encoding="utf-8")
            (root / "my note.md").write_text("# Note", encoding="utf-8")
            (root / "index.md").write_text(
                "[good](guide.md) [space](my%20note.md) [web](https://example.com)\n"
                "[anchor](#top) [bad](gone.md)\n", encoding="utf-8")
            problems = missing_links(root)
            self.assertEqual(len(problems), 1)
            self.assertEqual(problems[0][1:], (2, "gone.md"))

    def test_nested_relative_link(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "notes").mkdir()
            (root / "readme.md").write_text("here", encoding="utf-8")
            (root / "notes" / "today.md").write_text("[home](../readme.md)", encoding="utf-8")
            self.assertEqual(missing_links(root), [])


if __name__ == "__main__":
    unittest.main()
