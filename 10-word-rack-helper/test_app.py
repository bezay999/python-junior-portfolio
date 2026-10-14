import unittest

from app import find_words


class WordTests(unittest.TestCase):
    def test_letter_counts_and_order(self):
        words = find_words("RETAS", ["stare", "seat", "tree", "rate", "sea", "stare"], 3)
        self.assertEqual(words, ["stare", "rate", "seat", "sea"])

    def test_repeated_letter_needs_two_copies(self):
        self.assertEqual(find_words("TREE", ["tree", "tee", "treat"]), ["tree", "tee"])

    def test_bad_rack(self):
        with self.assertRaises(ValueError):
            find_words("a?", ["a"])


if __name__ == "__main__":
    unittest.main()
