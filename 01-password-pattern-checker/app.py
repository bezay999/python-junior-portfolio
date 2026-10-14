import getpass
import re


COMMON = {"password", "password123", "12345678", "qwerty123", "letmein"}
SEQUENCES = ("1234", "abcd", "qwerty")


def check_password(password):
    notes = []
    if len(password) < 12:
        notes.append("Use at least 12 characters.")
    if password.casefold() in COMMON:
        notes.append("This is a very common example. Choose something less predictable.")
    if re.search(r"(.)\1\1", password):
        notes.append("Avoid repeating the same character three times in a row.")
    lowered = password.casefold()
    if any(sequence in lowered for sequence in SEQUENCES):
        notes.append("Avoid keyboard or alphabet sequences.")
    if len(set(lowered)) < 6:
        notes.append("Use a wider variety of characters.")
    return notes


def main():
    password = getpass.getpass("Password to check (not saved): ")
    notes = check_password(password)
    if notes:
        print("Things to improve:")
        for note in notes:
            print(f"- {note}")
    else:
        print("No simple pattern flagged. This is not a security guarantee.")


if __name__ == "__main__":
    main()
