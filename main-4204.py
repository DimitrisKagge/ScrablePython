import classes
import json
import os

def display_menu():
    print("******************************************")
    print("** Welcome to the Scrabble Game! **")
    print("******************************************")
    print("1. Start a new game")
    print("2. View previous game records")
    print("3. Exit")
    print("******************************************")
    choice = input("Enter your choice (1/2/3): ").strip()
    print("******************************************")
    return choice

def choose_algorithm():
    print("******************************************")
    print("Choose the algorithm for the computer player:")
    print("1. MIN - The computer finds the smallest valid word.")
    print("2. MAX - The computer finds the largest valid word.")
    print("3. SMART - The computer finds the highest scoring word.")
    print("******************************************")
    choice = input("Enter your choice (1/2/3): ").strip()
    print("******************************************")
    if choice == '1':
        return 'MIN'
    elif choice == '2':
        return 'MAX'
    elif choice == '3':
        return 'SMART'
    else:
        print("Invalid choice, defaulting to SMART.")
        print("******************************************")
        return 'SMART'

def view_game_records():
    print("******************************************")
    if os.path.exists('game_data.json'):
        with open('game_data.json', 'r', encoding='utf-8') as f:
            game_data = json.load(f)
            print("Previous game records:")
            for i, record in enumerate(game_data, start=1):
                print(f"Game {i}: Human Score: {record['human_score']}, Computer Score: {record['computer_score']}, Moves: {record['moves']}, Algorithm: {record['algorithm']}")
    else:
        print("No game records found.")
    print("******************************************")

if __name__ == "__main__":
    while True:
        choice = display_menu()
        if choice == '1':
            algorithm = choose_algorithm()
            game = classes.Game("Human", "Computer", algorithm=algorithm)
            game.setup()
            game.run()
            game.end()
        elif choice == '2':
            view_game_records()
        elif choice == '3':
            print("Exiting the game. Goodbye!")
            print("******************************************")
            break
        else:
            print("Invalid choice, please try again.")
            print("******************************************")
