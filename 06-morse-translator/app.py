import argparse


LETTERS = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", ".": ".-.-.-", ",": "--..--", "?": "..--..",
    "!": "-.-.--",
}
REVERSE = {code: letter for letter, code in LETTERS.items()}


def encode(text):
    words = []
    for word in text.upper().split():
        try:
            words.append(" ".join(LETTERS[character] for character in word))
        except KeyError as error:
            raise ValueError(f"Unsupported character: {error.args[0]}") from error
    return " / ".join(words)


def decode(code):
    words = []
    for word in code.strip().split("/"):
        try:
            words.append("".join(REVERSE[symbol] for symbol in word.split()))
        except KeyError as error:
            raise ValueError(f"Unknown Morse code: {error.args[0]}") from error
    return " ".join(words)


def main():
    parser = argparse.ArgumentParser(description="Encode or decode Morse code")
    parser.add_argument("mode", choices=("encode", "decode"))
    parser.add_argument("text")
    args = parser.parse_args()
    try:
        print(encode(args.text) if args.mode == "encode" else decode(args.text))
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
