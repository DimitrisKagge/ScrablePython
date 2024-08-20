import random
import itertools

class SakClass:
    def __init__(self):
        self.letters = {
            'Α': 12, 'Β': 1, 'Γ': 2, 'Δ': 2, 'Ε': 8, 'Ζ': 1, 'Η': 7, 'Θ': 1,
            'Ι': 8, 'Κ': 4, 'Λ': 3, 'Μ': 3, 'Ν': 6, 'Ξ': 1, 'Ο': 9, 'Π': 4,
            'Ρ': 5, 'Σ': 7, 'Τ': 8, 'Υ': 4, 'Φ': 1, 'Χ': 1, 'Ψ': 1, 'Ω': 3
        }
        self.letter_points = {
            'Α': 1, 'Β': 8, 'Γ': 4, 'Δ': 4, 'Ε': 1, 'Ζ': 10, 'Η': 1, 'Θ': 10,
            'Ι': 1, 'Κ': 2, 'Λ': 3, 'Μ': 2, 'Ν': 1, 'Ξ': 10, 'Ο': 1, 'Π': 2,
            'Ρ': 2, 'Σ': 1, 'Τ': 1, 'Υ': 2, 'Φ': 8, 'Χ': 10, 'Ψ': 10, 'Ω': 3
        }
        self.sak = self.randomize_sak()

    def randomize_sak(self):
        sak = []
        for letter, count in self.letters.items():
            sak.extend([letter] * count)
        random.shuffle(sak)
        return sak

    def getletters(self, n):
        letters = self.sak[:n]
        self.sak = self.sak[n:]
        return letters

    def putbackletters(self, letters):
        self.sak.extend(letters)
        random.shuffle(self.sak)

class Player:
    def __init__(self, name):
        self.name = name
        self.letters = []

    def __repr__(self):
        return f"Player({self.name}, Letters: {self.letters})"

class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def play(self):
        word = input(f"{self.name}, enter your word: ")
        return word

class Computer(Player):
    def __init__(self, name, algorithm='MIN'):
        super().__init__(name)
        self.algorithm = algorithm

    def play(self, valid_words):
        if self.algorithm == 'MIN':
            for i in range(2, 8):
                for perm in itertools.permutations(self.letters, i):
                    word = ''.join(perm)
                    if word in valid_words:
                        return word
        elif self.algorithm == 'MAX':
            for i in range(7, 1, -1):
                for perm in itertools.permutations(self.letters, i):
                    word = ''.join(perm)
                    if word in valid_words:
                        return word
        elif self.algorithm == 'SMART':
            best_word = ''
            max_points = 0
            for i in range(2, 8):
                for perm in itertools.permutations(self.letters, i):
                    word = ''.join(perm)
                    if word in valid_words:
                        points = sum([self.letter_points[letter] for letter in word])
                        if points > max_points:
                            max_points = points
                            best_word = word
            return best_word

class Game:
    def __init__(self, human_name, computer_name, algorithm='MIN'):
        self.sak = SakClass()
        self.human = Human(human_name)
        self.computer = Computer(computer_name, algorithm)
        self.valid_words = self.load_words()

    def load_words(self):
        with open('greek7.txt', 'r', encoding='utf-8') as f:
            words = f.read().splitlines()
        return set(words)

    def setup(self):
        self.human.letters = self.sak.getletters(7)
        self.computer.letters = self.sak.getletters(7)
        print(f"{self.human.name}'s letters: {self.human.letters}")
        print(f"{self.computer.name} is ready.")

    def run(self):
        while True:
            human_word = self.human.play()
            if human_word == 'q':
                print("Game over!")
                break
            elif human_word == 'p':
                self.sak.putbackletters(self.human.letters)
                self.human.letters = self.sak.getletters(7)
                continue
            elif human_word in self.valid_words:
                print(f"Valid word! You scored: {self.score_word(human_word)} points.")
                self.human.letters = self.sak.getletters(7)
            else:
                print("Invalid word!")

            computer_word = self.computer.play(self.valid_words)
            if computer_word:
                print(f"{self.computer.name} played: {computer_word}")
                print(f"{self.computer.name} scored: {self.score_word(computer_word)} points.")
                self.computer.letters = self.sak.getletters(7)

    def score_word(self, word):
        return sum([self.sak.letter_points[letter] for letter in word])

    def end(self):
        print("Final score:")

