import unittest

from app import issues, read_board


SOLVED = """534678912
672195348
198342567
859761423
426853791
713924856
961537284
287419635
345286179"""


class SudokuTests(unittest.TestCase):
    def test_completed_board(self):
        self.assertEqual(issues(read_board(SOLVED)), [])

    def test_blank_is_not_a_conflict(self):
        self.assertEqual(issues(read_board("." + SOLVED[1:])), [])

    def test_duplicate_number(self):
        board = read_board("5" + SOLVED[1:])
        board[0][1] = 5
        self.assertIn("row 1", issues(board))

    def test_bad_shape(self):
        with self.assertRaises(ValueError):
            read_board("123")


if __name__ == "__main__":
    unittest.main()
