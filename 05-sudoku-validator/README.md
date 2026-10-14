# Sudoku Validator

I like puzzle tools that answer a narrow question well. This one does not solve Sudoku; it checks whether a 9×9 board has repeated numbers in any row, column, or 3×3 box. `0` or `.` means an empty cell.

```bash
python3 app.py samples/board.txt
```

The sample is a completed board. Try changing a digit to see a conflict report. A board with blanks can still be valid, just unfinished. Run `python3 -m unittest -v` in this folder for the checks.
