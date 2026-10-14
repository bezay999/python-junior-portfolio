# Word Rack Helper

This one is for a paper word game: give it a rack of letters and a small dictionary, and it lists the words you can actually build. A letter cannot be used more times than it appears on the rack.

```bash
python3 app.py samples/words.txt RETAS --min-length 4
```

Results are ordered by length, then alphabetically. The included dictionary is intentionally short and only for trying the program; you can point it at your own one-word-per-line English list. It is not a Scrabble dictionary or a scoring engine. Run `python3 -m unittest -v` for the checks.
