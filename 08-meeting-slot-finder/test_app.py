import unittest

from app import find_slot


class MeetingTests(unittest.TestCase):
    def setUp(self):
        self.day = {"workday": ["09:00", "12:00"],
                    "people": {"Ada": [["09:00", "10:00"]],
                               "Ben": [["10:30", "11:00"]]}}

    def test_first_shared_gap(self):
        self.assertEqual(find_slot(self.day, 30), ("10:00", "10:30"))

    def test_no_slot(self):
        self.assertIsNone(find_slot(self.day, 90))

    def test_overlapping_busy_periods(self):
        self.day["people"]["Ben"] = [["09:30", "11:30"]]
        self.assertEqual(find_slot(self.day, 30), ("11:30", "12:00"))

    def test_bad_interval(self):
        self.day["people"]["Ben"] = [["12:00", "11:00"]]
        with self.assertRaises(ValueError):
            find_slot(self.day, 30)


if __name__ == "__main__":
    unittest.main()
