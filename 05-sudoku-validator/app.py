import argparse
from pathlib import Path


def read_board(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if len(lines) != 9 or any(len(line) != 9 for line in lines):
        raise ValueError("A board needs exactly nine rows of nine cells")
    if any(character not in "0123456789." for line in lines for character in line):
        raise ValueError("Use digits 1-9 and 0 or . for blanks")
    return [[0 if character == "." else int(character) for character in line] for line in lines]


def repeated(values):
    filled = [value for value in values if value != 0]
    return len(filled) != len(set(filled))


def issues(board):
    problems = []
    for index in range(9):
        if repeated(board[index]):
            problems.append(f"row {index + 1}")
        if repeated([board[row][index] for row in range(9)]):
            problems.append(f"column {index + 1}")
    for top in (0, 3, 6):
        for left in (0, 3, 6):
            values = [board[row][column]
                      for row in range(top, top + 3)
                      for column in range(left, left + 3)]
            if repeated(values):
                problems.append(f"box ({top // 3 + 1}, {left // 3 + 1})")
    return problems


def main():
    parser = argparse.ArgumentParser(description="Check a Sudoku board for conflicts")
    parser.add_argument("board", type=Path)
    args = parser.parse_args()
    try:
        board = read_board(args.board.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        parser.error(str(error))
    problems = issues(board)
    if problems:
        print("Conflicts in: " + ", ".join(problems))
        return 1
    if any(0 in row for row in board):
        print("Valid so far, but not complete.")
    else:
        print("Valid completed board.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
