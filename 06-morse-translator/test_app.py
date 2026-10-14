import unittest

from app import decode, encode


class MorseTests(unittest.TestCase):
    def test_round_trip(self):
        self.assertEqual(decode(encode("SOS from home")), "SOS FROM HOME")

    def test_digits_and_punctuation(self):
        self.assertEqual(decode(encode("Wait, 2!")), "WAIT, 2!")

    def test_unsupported_character(self):
        with self.assertRaises(ValueError):
            encode("hello @")
        with self.assertRaises(ValueError):
            decode("......")


if __name__ == "__main__":
    unittest.main()
