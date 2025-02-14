import random

class Game:
    def __init__(self):
        self.choices = ["pierre", "papier", "ciseaux"]

    def get_user_item(self):
        while True:
            choice = input("Choisissez pierre, papier ou ciseaux : ").lower()
            if choice in self.choices:
                return choice
            print("Choix invalide, veuillez entrer pierre, papier ou ciseaux.")

    def get_computer_item(self):
        return random.choice(self.choices)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (user_item == "pierre" and computer_item == "ciseaux") or \
             (user_item == "papier" and computer_item == "pierre") or \
             (user_item == "ciseaux" and computer_item == "papier"):
            return "win"
        else:
            return "loss"

    def play(self):
        user_choice = self.get_user_item()
        computer_choice = self.get_computer_item()

        print(f"Vous avez choisi : {user_choice}")
        print(f"L'ordinateur a choisi : {computer_choice}")

        result = self.get_game_result(user_choice, computer_choice)
        
        if result == "win":
            print("Vous avez gagné !")
        elif result == "loss":
            print("Vous avez perdu...")
        else:
            print("Égalité !")

        return result

def get_user_menu_choice():
    print("\nMenu :")
    print("1. Jouer une nouvelle partie")
    print("2. Afficher les scores")
    print("3. Quitter")

    while True:
        choice = input("Votre choix (1/2/3) : ")
        if choice in ["1", "2", "3"]:
            return choice
        print("Entrée invalide, veuillez choisir 1, 2 ou 3.")

def print_results(results):
    print("\n----- Résumé des résultats -----")
    print(f"Victoires : {results['win']}")
    print(f"Défaites : {results['loss']}")
    print(f"Égalités : {results['draw']}")
    print("Merci d'avoir joué !")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == "1":
            game = Game()
            result = game.play()
            results[result] += 1  # Mise à jour des scores

        elif choice == "2":
            print_results(results)

        elif choice == "3":
            print_results(results)
            break

if __name__ == "__main__":
    main()
