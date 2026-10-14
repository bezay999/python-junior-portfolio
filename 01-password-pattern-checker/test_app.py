import unittest

from app import check_password


class PasswordTests(unittest.TestCase):
    def test_common_short_password_gets_feedback(self):
        notes = check_password("password123")
        self.assertTrue(any("12 characters" in note for note in notes))
        self.assertTrue(any("common" in note for note in notes))

    def test_repetition_and_sequence(self):
        notes = check_password("Abcdef111111111")
        self.assertTrue(any("repeating" in note for note in notes))
        self.assertTrue(any("sequences" in note for note in notes))

    def test_long_phrase_has_no_simple_warning(self):
        self.assertEqual(check_password("blue-harbor-7-morning"), [])


if __name__ == "__main__":
    unittest.main()
