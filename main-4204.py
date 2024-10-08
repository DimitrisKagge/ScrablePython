import os  # Εισαγωγή του module os για διαχείριση αρχείων
import json  # Εισαγωγή του module json για διαχείριση δεδομένων JSON
import classes  # Εισαγωγή του module classes που περιέχει τις κλάσεις του παιχνιδιού


def guidelines():
    """
     Οδηγίες για το παιχνίδι Scrabble:

    1. Ποιες κλάσεις έχετε υλοποιήσει στον κώδικά σας:
        - SakClass: Διαχειρίζεται τα γράμματα του σακουλιού, τα ανακατεύει και επιτρέπει την επιλογή γραμμάτων από το σακούλι. Επίσης, επιτρέπει την επιστροφή γραμμάτων στο σακούλι.
        - Player: Βασική κλάση που περιγράφει έναν παίκτη. Κρατά τα γράμματα και το σκορ του παίκτη και παρέχει μεθόδους για να προσθέσει ή να αφαιρέσει γράμματα.
        - Human: Υποκλάση της Player, αντιπροσωπεύει τον ανθρώπινο παίκτη. Προσθέτει μια μέθοδο `play`, που επιτρέπει στον παίκτη να επιλέξει μια λέξη ή να τερματίσει το παιχνίδι.
        - Computer: Υποκλάση της Player, αντιπροσωπεύει τον υπολογιστή. Περιλαμβάνει τρεις αλγορίθμους για την επιλογή λέξεων (MIN, MAX, SMART) και χρησιμοποιεί τη διαθέσιμη λίστα λέξεων και τα γράμματα για να επιλέξει την καλύτερη λέξη ανάλογα με τον αλγόριθμο.
        - Game: Διαχειρίζεται τη ροή του παιχνιδιού, συντονίζοντας την αλληλεπίδραση μεταξύ του ανθρώπου και του υπολογιστή, φορτώνει τη λίστα λέξεων από αρχείο, και αποθηκεύει τα δεδομένα του παιχνιδιού σε αρχείο.

    2. Ποια κληρονομικότητα έχετε υλοποιήσει:
        - Η κλάση Player είναι η βασική κλάση για τους παίκτες (ανθρώπους και υπολογιστές).
        - Η κλάση Human κληρονομεί από την Player και προσθέτει τη μέθοδο `play` για τον ανθρώπινο παίκτη.
        - Η κλάση Computer κληρονομεί από την Player και προσθέτει τη μέθοδο `play` με αλγορίθμους για να επιλέγει λέξεις ανάλογα με τα γράμματα και τις λέξεις που διαθέτει.

    3. Ποια επέκταση μεθόδων έχετε υλοποιήσει:
        - Η μέθοδος `play` επεκτείνεται τόσο στην κλάση Human όσο και στην κλάση Computer. Στην περίπτωση του Human, ο παίκτης εισάγει χειροκίνητα λέξεις, ενώ στην περίπτωση του Computer, επιλέγεται αυτόματα μια λέξη σύμφωνα με τον αλγόριθμο που έχει οριστεί.

    4. Αν έχετε εφαρμόσει υπερφόρτωση τελεστών ή χρησιμοποιήσατε decorators:
        - Στον παρόντα κώδικα δεν εφαρμόστηκε υπερφόρτωση τελεστών ή χρήση decorators.

    5. Σε ποια δομή (λίστα ή λεξικό) οργανώνει η εφαρμογή σας τις λέξεις της γλώσσας κατά τη διάρκεια του παιχνιδιού:
        - Οι λέξεις οργανώνονται σε σύνολο (set) στη μέθοδο `load_words` της κλάσης Game. Αυτή η δομή επιτρέπει τη γρήγορη αναζήτηση έγκυρων λέξεων κατά τη διάρκεια του παιχνιδιού.

    6. Ποιον αλγόριθμο (ή αλγορίθμους) υλοποιήσατε για να παίξει ο υπολογιστής:
        - Υλοποιήθηκαν οι εξής αλγόριθμοι στην κλάση Computer:
          - **MIN**: Ο υπολογιστής επιλέγει την μικρότερη έγκυρη λέξη από τα διαθέσιμα γράμματα.
          - **MAX**: Ο υπολογιστής επιλέγει τη μεγαλύτερη δυνατή λέξη.
          - **SMART**: Ο υπολογιστής επιλέγει τη λέξη που δίνει τη μεγαλύτερη βαθμολογία, λαμβάνοντας υπόψη τα γράμματα και τους πόντους τους.

    7. Αποθήκευση και φόρτωση δεδομένων:
        - Η μέθοδος `save_game_data` αποθηκεύει τα δεδομένα του παιχνιδιού (σκορ, κινήσεις, αλγόριθμος) σε ένα αρχείο JSON.
        - Η μέθοδος `load_words` φορτώνει τις έγκυρες λέξεις από ένα αρχείο κειμένου, το οποίο περιέχει μία λέξη ανά γραμμή.
    """


def display_menu():
    print("******************************************")
    print("** Καλώς ήρθατε στο παιχνίδι Scrabble! **")
    print("******************************************")
    print("1. Έναρξη νέου παιχνιδιού")
    print("2. Προβολή προηγούμενων παρτίδων")
    print("3. Έξοδος")
    print("******************************************")
    choice = input("Εισάγετε την επιλογή σας (1/2/3): ").strip()
    print("******************************************")
    return choice


def choose_algorithm():
    print("******************************************")
    print("Επιλέξτε τον αλγόριθμο για τον υπολογιστή:")
    print("1. MIN - Ο υπολογιστής βρίσκει τη μικρότερη έγκυρη λέξη.")
    print("2. MAX - Ο υπολογιστής βρίσκει τη μεγαλύτερη έγκυρη λέξη.")
    print("3. SMART - Ο υπολογιστής βρίσκει τη λέξη με την υψηλότερη βαθμολογία.")
    print("******************************************")
    choice = input("Εισάγετε την επιλογή σας (1/2/3): ").strip()
    print("******************************************")
    if choice == '1':
        return 'MIN'
    elif choice == '2':
        return 'MAX'
    elif choice == '3':
        return 'SMART'
    else:
        print("Μη έγκυρη επιλογή, ορίζεται ο αλγόριθμος SMART.")
        print("******************************************")
        return 'SMART'


def view_game_records():
    if os.path.exists('game_data.json'):
        with open('game_data.json', 'r', encoding='utf-8') as f:
            game_data = json.load(f)
            print("Προηγούμενες παρτίδες:")
            for i, record in enumerate(game_data, start=1):
                print(f"Παρτίδα {i}: Σκορ Ανθρώπου: {record['human_score']}, Σκορ Υπολογιστή: {record['computer_score']}, Κινήσεις: {record['moves']}, Αλγόριθμος: {record['algorithm']}")
    else:
        print("Δεν βρέθηκαν παρτίδες.")
    print("******************************************")


if __name__ == "__main__":
    guidelines()  # Κλήση της συνάρτησης guidelines
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
            print("Έξοδος από το παιχνίδι. Αντίο!")
            print("******************************************")
            break
        else:
            print("Μη έγκυρη επιλογή, παρακαλώ δοκιμάστε ξανά.")
            print("******************************************")
