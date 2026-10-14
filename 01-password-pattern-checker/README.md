# Password Pattern Checker

This is a small practice tool for spotting a few common password problems: short length, repeated characters, obvious sequences, and a tiny list of common examples. It gives suggestions, not a security guarantee. It never saves or prints the password.

Run `python3 app.py` and enter a password at the hidden prompt. To check the rules, run `python3 -m unittest -v` in this folder. No packages are needed.

The checker is intentionally modest. A pass here does not mean a password is safe to use; it just means these simple patterns were not found.
