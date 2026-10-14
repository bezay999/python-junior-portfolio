import csv
from pathlib import Path
import tempfile
import unittest

from app import clean_file, tidy_rows


class CsvTests(unittest.TestCase):
    def test_tidy_rows(self):
        rows = [["name", "city"], [" Ada ", " Warsaw "], ["ada", "WARSAW"], [], ["", ""]]
        cleaned, removed = tidy_rows(rows)
        self.assertEqual(cleaned, [["name", "city"], ["Ada", "Warsaw"]])
        self.assertEqual(removed, 3)

    def test_write_new_file_only(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "input.csv"
            output = Path(folder) / "output.csv"
            source.write_text("name\n Ada \n", encoding="utf-8")
            self.assertEqual(clean_file(source, output), (1, 0))
            with output.open(newline="", encoding="utf-8") as file:
                self.assertEqual(list(csv.reader(file)), [["name"], ["Ada"]])
            self.assertEqual(source.read_text(encoding="utf-8"), "name\n Ada \n")
            with self.assertRaises(ValueError):
                clean_file(source, output)

    def test_wrong_width(self):
        with self.assertRaises(ValueError):
            tidy_rows([["a", "b"], ["one"]])


if __name__ == "__main__":
    unittest.main()
