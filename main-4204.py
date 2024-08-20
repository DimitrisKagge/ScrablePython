import classes


def guidelines():
    """
    This game is a simplified version of Scrabble in Greek.

    Classes Implemented:
    - SakClass: Manages the letters bag.
    - Player: Base class for all players.
    - Human: Inherits from Player, manages human player behavior.
    - Computer: Inherits from Player, manages computer player behavior.
    - Game: Manages the overall game flow.

    Inheritance:
    - Human and Computer inherit from Player.

    Algorithms for Computer:
    - MIN: Finds the smallest valid word.
    - MAX: Finds the largest valid word.
    - SMART: Finds the highest scoring word.

    Data Structure for Words:
    - Words are stored in a set for quick lookup.
    """
    pass


if __name__ == "__main__":
    game = classes.Game("Human", "Computer", algorithm='SMART')
    game.setup()
    game.run()
    game.end()
