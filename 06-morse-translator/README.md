# Morse Translator

Morse code makes a nice little exercise in dictionaries and text parsing. This tool translates letters, numbers, and a few punctuation marks in both directions. It is an encoding exercise, not private encryption.

```bash
python3 app.py encode "SOS from home"
python3 app.py decode "... --- ... / ..-. .-. --- -- / .... --- -- ."
```

Words are separated by `/` in Morse. Unsupported characters or unknown codes produce an error instead of silently disappearing. Run `python3 -m unittest -v` to check round trips and error cases.
