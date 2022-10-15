from words import valid_words
import random
import sys

chosen_word = random.choice(valid_words)
guess_max = 6


class Colors:
    prefix = '\033'
    base = "\033[0m"
    grey = "\033[90m"
    red = "\033[91m"
    green = "\033[92m"
    yellow = "\033[93m"
    PERSISTENT_COLORS = [red, green]


class GuessWord:

    counter = 1
    wordles = []
    alphabet = {
        "a": "a",
        "b": "b",
        "c": "c",
        "d": "d",
        "e": "e",
        "f": "f",
        "g": "g",
        "h": "h",
        "i": "i",
        "j": "j",
        "k": "k",
        "l": "l",
        "m": "m",
        "n": "n",
        "o": "o",
        "p": "p",
        "q": "q",
        "r": "r",
        "s": "s",
        "t": "t",
        "u": "u",
        "v": "v",
        "w": "w",
        "x": "x",
        "y": "y",
        "z": "z",
    }

    def __init__(self, word_str: str):
        self.word_str = word_str
        self.word_char = list(word_str)
        self.post_guess = ""

    def next_try(self):
        GuessWord.counter += 1

    def check_valid(self):
        return self.word_str in valid_words

    def set_green(self):
        for i, _ in enumerate(self.word_char):
            actual_char = chosen_word[i]
            guess_char = self.word_str[i]
            if guess_char == actual_char:
                colored_char = f"{Colors.green}{actual_char}{Colors.base}"
                self.word_char[i] = colored_char
                self.edit_alphabet(guess_char, colored_char)

    def set_yellow(self):
        for i, _ in enumerate(self.word_char):
            guess_char = self.word_char[i]
            if guess_char in chosen_word:
                colored_char = f"{Colors.yellow}{guess_char}{Colors.base}"
                self.word_char[i] = colored_char
                self.edit_alphabet(guess_char, colored_char)
            else:
                colored_char = f"{Colors.red}{guess_char}{Colors.base}"
                self.edit_alphabet(guess_char, colored_char)

    def edit_alphabet(self, k, v):
        if k not in GuessWord.alphabet.keys():
            # A new key value pair is being added.
            return

        # Do not modify key value pairs that are already green or red
        older_value = GuessWord.alphabet.get(k, "")
        modify_color = True
        for c in Colors.PERSISTENT_COLORS:
            if c in older_value:
                modify_color = False

        if modify_color:
            GuessWord.alphabet[k] = v

    def apply_guess(self):
        self.set_green()
        self.set_yellow()
        self.post_guess = "".join(self.word_char)
        GuessWord.wordles.append(self.post_guess)
        for element in GuessWord.wordles:
            print(element)
        # print(self.post_guess)

    def check_perfect_guess(self):
        if self.word_str == chosen_word:
            print(f"Congratulations! You beat Wordle in {GuessWord.counter} guesses")
            sys.exit(1)

    def check_game_loss(self):
        if GuessWord.counter == guess_max + 1:
            print(f"You lost the game. The word was {chosen_word}")
            sys.exit(1)
