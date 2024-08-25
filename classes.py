import random
import itertools
from collections import Counter
import json
import os

class SakClass:
    def __init__(self):
        self.letters = {
            'Α': 12, 'Β': 1, 'Γ': 2, 'Δ': 2, 'Ε': 8, 'Ζ': 1, 'Η': 7, 'Θ': 1,
            'Ι': 8, 'Κ': 4, 'Λ': 3, 'Μ': 3, 'Ν': 6, 'Ξ': 1, 'Ο': 9, 'Π': 4,
            'Ρ': 5, 'Σ': 7, 'Τ': 8, 'Υ': 4, 'Φ': 1, 'Χ': 1, 'Ψ': 1, 'Ω': 3
        }
        self.letter_points = {
            'Α': 1, 'Β': 8, 'Γ': 4, 'Δ': 4, 'Ε': 1, 'Ζ': 10, 'Η': 1, 'Θ': 10,
            'Ι': 1, 'Κ': 2, 'Λ': 3, 'Μ': 3, 'Ν': 1, 'Ξ': 10, 'Ο': 1, 'Π': 2,
            'Ρ': 2, 'Σ': 1, 'Τ': 1, 'Υ': 2, 'Φ': 8, 'Χ': 8, 'Ψ': 10, 'Ω': 3
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

    def remaining_letters(self):
        return len(self.sak)

    def display_letters_with_points(self, letters):
        return [f"{letter}({self.letter_points[letter]})" for letter in letters]

class Player:
    def __init__(self, name):
        self.name = name
        self.letters = []
        self.score = 0

    def add_letters(self, new_letters):
        self.letters.extend(new_letters)

    def remove_used_letters(self, word):
        word_counter = Counter(word)
        letters_counter = Counter(self.letters)

        for letter in word_counter:
            letters_counter[letter] -= word_counter[letter]

        self.letters = list(letters_counter.elements())

    def can_form_word(self, word):
        word_counter = Counter(word)
        letters_counter = Counter(self.letters)
        return all(letters_counter[letter] >= word_counter[letter] for letter in word_counter)

class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def play(self, sak):
        while True:
            print("******************************************")
            letters_with_points = ", ".join(sak.display_letters_with_points(self.letters))
            print(f"Your available letters: {letters_with_points}")
            word = input(
                f"{self.name}, enter your word (or 'P' to replace letters, 'Q' to quit): ").strip().upper()
            print("******************************************")
            if word == 'P':
                return word
            elif word == 'Q':
                return word
            elif self.can_form_word(word):
                return word
            else:
                print("Invalid word! You don't have the necessary letters.")
                print("******************************************")

class Computer(Player):
    def __init__(self, name, algorithm='MIN'):
        super().__init__(name)
        self.algorithm = algorithm

    def play(self, valid_words, letter_points):
        possible_words = []
        for i in range(2, 8):
            for perm in itertools.permutations(self.letters, i):
                word = ''.join(perm)
                if word in valid_words and self.can_form_word(word):
                    possible_words.append(word)

        if self.algorithm == 'MIN':
            return min(possible_words, key=len, default=None)
        elif self.algorithm == 'MAX':
            return max(possible_words, key=len, default=None)
        elif self.algorithm == 'SMART':
            return max(possible_words, key=lambda w: sum([letter_points[l] for l in w]), default=None)

class Game:
    def __init__(self, human_name, computer_name, algorithm='MIN'):
        self.human_name = human_name
        self.computer_name = computer_name
        self.algorithm = algorithm
        self.reset()

    def reset(self):
        self.sak = SakClass()
        self.human = Human(self.human_name)
        self.computer = Computer(self.computer_name, self.algorithm)
        self.valid_words = self.load_words()
        self.moves = 0  # Μετρητής για τις κινήσεις

    def load_words(self):
        with open('greek7.txt', 'r', encoding='utf-8') as f:
            words = f.read().splitlines()
        return set(words)

    def save_game_data(self):
        """Save game data to a JSON file."""
        game_record = {
            "human_score": self.human.score,
            "computer_score": self.computer.score,
            "moves": self.moves,
            "algorithm": self.algorithm
        }
        if os.path.exists('game_data.json'):
            with open('game_data.json', 'r', encoding='utf-8') as f:
                game_data = json.load(f)
        else:
            game_data = []
        game_data.append(game_record)
        with open('game_data.json', 'w', encoding='utf-8') as f:
            json.dump(game_data, f, ensure_ascii=False, indent=4)

    def setup(self):
        self.human.add_letters(self.sak.getletters(7))
        self.computer.add_letters(self.sak.getletters(7))
        # Καμία εμφάνιση κατά τη διάρκεια της προετοιμασίας

    def run(self):
        while True:
            human_word = self.human.play(self.sak)
            if human_word == 'Q':
                print("Game over!")
                print("******************************************")
                break
            elif human_word == 'P':
                self.change_letters(self.human)
                self.moves += 1  # Αύξηση του μετρητή των κινήσεων
                computer_word = self.computer_play_turn()
            elif human_word in self.valid_words:
                points = self.score_word(human_word)
                print(f"Valid word! You scored: {points} points.")
                print("******************************************")
                self.human.score += points
                self.human.remove_used_letters(human_word)
                self.human.add_letters(self.sak.getletters(7 - len(self.human.letters)))
                self.moves += 1  # Αύξηση του μετρητή των κινήσεων
            else:
                print("Invalid word!")
                print("******************************************")

            if human_word != 'P':
                computer_word = self.computer_play_turn()
                self.moves += 1  # Αύξηση του μετρητή των κινήσεων

            # Εμφάνιση του σκορ μία φορά μετά από κάθε γύρο
            self.display_status()

    def change_letters(self, player):
        self.sak.putbackletters(player.letters)
        player.letters = self.sak.getletters(7)
        print(f"{player.name} changed their letters. New letters: {', '.join(player.letters)}")
        print("******************************************")

    def computer_play_turn(self):
        letters_with_points = ", ".join(self.sak.display_letters_with_points(self.computer.letters))
        print(f"Computer's available letters: {letters_with_points}")  # Εμφάνιση γραμμάτων του υπολογιστή
        computer_word = self.computer.play(self.valid_words, self.sak.letter_points)
        if computer_word:
            points = self.score_word(computer_word)
            print(f"{self.computer.name} played: {computer_word}")
            print(f"{self.computer.name} scored: {points} points.")
            print("******************************************")
            self.computer.score += points
            self.computer.remove_used_letters(computer_word)
            self.computer.add_letters(self.sak.getletters(7 - len(self.computer.letters)))
        return computer_word

    def score_word(self, word):
        return sum([self.sak.letter_points[letter] for letter in word])

    def display_status(self):
        print(
            f"Scores -> {self.human.name}: {self.human.score} points, {self.computer.name}: {self.computer.score} points")
        print(f"Remaining letters in sack: {self.sak.remaining_letters()}")
        print("******************************************")

    def end(self):
        print("Final score:")
        self.display_status()
        self.save_game_data()  # Αποθήκευση δεδομένων στο τέλος του παιχνιδιού
        if self.human.score > self.computer.score:
            print(f"{self.human.name} wins!")
        elif self.human.score < self.computer.score:
            print(f"{self.computer.name} wins!")
        else:
            print("It's a tie!")
        print("******************************************")
