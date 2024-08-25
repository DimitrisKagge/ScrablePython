import os  # Εισαγωγή του module os για διαχείριση αρχείων
import json  # Εισαγωγή του module json για διαχείριση δεδομένων JSON
import classes  # Εισαγωγή του module classes που περιέχει τις κλάσεις του παιχνιδιού


def guidelines():
    """
    Οδηγίες για την εργασία Scrabble:

    1. Ποιές κλάσεις έχετε υλοποιήσει στον κώδικά σας:
        - SakClass: Διαχειρίζεται τα γράμματα του σακουλάκιου.
        - Player: Βασική κλάση που περιγράφει έναν παίκτη.
        - Human: Υποκλάση της Player, αντιπροσωπεύει τον ανθρώπινο παίκτη.
        - Computer: Υποκλάση της Player, αντιπροσωπεύει τον υπολογιστή και περιλαμβάνει αλγορίθμους για το παιχνίδι.
        - Game: Διαχειρίζεται τη ροή του παιχνιδιού και συντονίζει την αλληλεπίδραση μεταξύ των παικτών.

    2. Ποιά κληρονομικότητα έχετε υλοποιήσει:
        - Η κλάση Player είναι η βασική κλάση.
        - Η κλάση Human κληρονομεί από την Player και προσθέτει μεθόδους για τον ανθρώπινο παίκτη.
        - Η κλάση Computer κληρονομεί από την Player και προσθέτει αλγορίθμους για την επιλογή λέξεων.

    3. Ποιά επέκταση μεθόδων έχετε υλοποιήσει:
        - Η μέθοδος `play` επεκτείνεται τόσο στην κλάση Human όσο και στην κλάση Computer, προσαρμόζοντας τη λειτουργία της ανάλογα με το αν ο παίκτης είναι άνθρωπος ή υπολογιστής.

    4. Αν έχετε εφαρμόσει υπερφόρτωση τελεστών ή χρησιμοποιήσατε decorators:
        - Στον παρόντα κώδικα δεν εφαρμόστηκε υπερφόρτωση τελεστών ή χρήση decorators.

    5. Σε ποιά δομή (λίστα ή λεξικό-dictionary) οργανώνει η εφαρμογή σας τις λέξεις της γλώσσας στη διάρκεια του παιχνιδιού:
        - Οι λέξεις της γλώσσας οργανώνονται σε σύνολο (set) στη μέθοδο `load_words` της κλάσης Game για γρήγορη αναζήτηση.

    6. Ποιόν αλγόριθμο (ή αλγορίθμους) υλοποιήσατε για να παίξει ο Η/Υ:
        - Υλοποιήθηκαν οι αλγόριθμοι MIN (μικρότερη λέξη), MAX (μεγαλύτερη λέξη), και SMART (υψηλότερη βαθμολογία) στην κλάση Computer.

    Σημείωση: Εκτελέστε την εντολή `help(guidelines)` για να δείτε αυτή την τεκμηρίωση.
    """


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
    if os.path.exists('game_data.json'):
        with open('game_data.json', 'r', encoding='utf-8') as f:
            game_data = json.load(f)
            print("Previous game records:")
            for i, record in enumerate(game_data, start=1):
                print(
                    f"Game {i}: Human Score: {record['human_score']}, Computer Score: {record['computer_score']}, Moves: {record['moves']}, Algorithm: {record['algorithm']}")
    else:
        print("No game records found.")
    print("******************************************")


if __name__ == "__main__":
    guidelines()  # Κλήση της συνάρτησης guidelines για να καταχωρηθεί στη μνήμη
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
