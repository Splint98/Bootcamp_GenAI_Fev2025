# Challenge

#     Ask a user for a word.
#     Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.
#         Make sure the letters are the keys.
#         Make sure the letters are strings.
#         Make sure the indexes are stored in a list, and those lists are values.

# Examples

#     “dodo” ➞ { “d”: [0, 2], “o”: [1, 3] }
#     “froggy” ➞ { “f”: [0], “r”: [1], “o”: [2], “g”: [3, 4], “y”: [5] }
#     “grapes” ➞ { “g”: [0], “r”: [1], “a”: [2], “p”: [3] }


# Demander un mot à l'utilisateur
word = input("Entrez un mot : ").strip()

# Initialiser un dictionnaire vide
letter_indexes = {}
# Initialiser un compteur d'index
index = 0

# Parcourir chaque lettre du mot
#for index, letter in enumerate(word): Possible avec enumerate sans index aussi, mais pas trouvé ça moi meme, je le note quand meme pour moi 
for letter in word:
    if letter in letter_indexes:  # Si la lettre est déjà dans le dictionnaire
        letter_indexes[letter].append(index)  # Ajouter l'index à la liste existante
    else:
        letter_indexes[letter] = [index]  # Créer une nouvelle liste avec l'index
    index += 1  # Incrémenter l'index à chaque itération

# Afficher le dictionnaire résultant
print(letter_indexes)
