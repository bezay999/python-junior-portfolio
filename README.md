# Small Python tools for real little problems

This is a collection of ten independent Python projects. I wanted each folder to be something you can understand and run in a few minutes, while still having a real problem behind it. They use the standard library only, so Python 3.9+ is enough.

There is no shared framework to set up. Pick a folder, read its short README, and try the example command. Tests live beside the code.

| # | Project | What it does |
|---|---|---|
| 01 | [Password Pattern Checker](01-password-pattern-checker/README.md) | Gives practical feedback on a password without storing it. |
| 02 | [Duplicate File Scout](02-duplicate-file-scout/README.md) | Finds files with identical content without deleting anything. |
| 03 | [Markdown Link Inspector](03-markdown-link-inspector/README.md) | Finds broken local links in Markdown notes. |
| 04 | [Recipe Scaler](04-recipe-scaler/README.md) | Adjusts ingredient amounts for another serving count. |
| 05 | [Sudoku Validator](05-sudoku-validator/README.md) | Checks a board for conflicts and whether it is complete. |
| 06 | [Morse Translator](06-morse-translator/README.md) | Encodes and decodes short messages. |
| 07 | [CSV Tidy](07-csv-tidy/README.md) | Trims cells and removes empty or repeated rows. |
| 08 | [Meeting Slot Finder](08-meeting-slot-finder/README.md) | Finds a shared free slot between busy periods. |
| 09 | [Settings Doctor](09-settings-doctor/README.md) | Checks a JSON configuration and explains what is wrong. |
| 10 | [Word Rack Helper](10-word-rack-helper/README.md) | Finds dictionary words that can be built from a set of letters. |

To run every test from the repository root:

```bash
python3 check_all.py
```

Or open one folder and run `python3 -m unittest -v`. Sample data is fictional. The file tools avoid changing their input; where a program writes output, its README says exactly where it goes.
