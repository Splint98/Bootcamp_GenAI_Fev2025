# Importation du module pour effacer la console à chaque tour
import os

class TicTacToe:
    def __init__(self):
        """Initialise le plateau de jeu vide."""
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"  # Le joueur "X" commence toujours

    def print_board(self):
        """Affiche le plateau de jeu."""
        os.system('cls' if os.name == 'nt' else 'clear')  # Efface la console
        print("\n  0   1   2")  # En-tête des colonnes
        for i, row in enumerate(self.board):
            print(i, "|".join(row))
            if i < 2:
                print("  ---------")  # Ligne de séparation

    def is_winner(self, player):
        """Vérifie si un joueur a gagné."""
        # Vérification des lignes et colonnes
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
               all(self.board[j][i] == player for j in range(3)):
                return True

        # Vérification des diagonales
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def is_draw(self):
        """Vérifie si la partie est un match nul (plateau plein sans gagnant)."""
        return all(self.board[i][j] != " " for i in range(3) for j in range(3))

    def play_turn(self):
        """Demande au joueur actuel de jouer un coup valide."""
        while True:
            try:
                row, col = map(int, input(f"Joueur {self.current_player}, entrez votre coup (ligne colonne) : ").split())
                if self.board[row][col] == " ":
                    self.board[row][col] = self.current_player
                    break
                else:
                    print("Case déjà occupée ! Essayez encore.")
            except (ValueError, IndexError):
                print("Entrée invalide, veuillez entrer deux nombres entre 0 et 2 séparés par un espace.")

    def switch_player(self):
        """Change le joueur actuel."""
        self.current_player = "O" if self.current_player == "X" else "X"

    def play_game(self):
        """Lance la partie de Tic Tac Toe."""
        while True:
            self.print_board()
            self.play_turn()

            if self.is_winner(self.current_player):
                self.print_board()
                print(f"Félicitations ! Le joueur {self.current_player} a gagné !")
                break

            if self.is_draw():
                self.print_board()
                print("Match nul !")
                break

            self.switch_player()  # Passe au joueur suivant

# Lancement du jeu
if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
