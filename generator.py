from random import choice, randint, shuffle
from string import ascii_letters, punctuation


LETTRES = ascii_letters
SPECIAUX = punctuation


class passwords_generator:
    def __init__(self):
        self.numbers = []
        self.letters = LETTRES
        self.special_characters = SPECIAUX

    def gen_passwd(self, num_letters: int, num_numbers: int, num_special: int):
        """randomly returns numbers, letters and special characters according to user choice"""

        def mod(param): return choice([str.upper, str.lower])(param)

        self.numbers = [str(randint(0, 9)) for i in range(num_numbers)]
        self.letters = [choice(self.letters) for i in range(num_letters)]
        self.letters = [mod(i) for i in self.letters]
        self.special_characters = [
            choice(self.special_characters) for i in range(num_special)]
        self.numbers.extend(self.letters)
        self.numbers.extend(self.special_characters)
        shuffle(self.numbers)
        return "".join(self.numbers)


if __name__ == "__main__":
    obj = passwords_generator()
    print(obj.gen_passwd(2, 4, 2))
