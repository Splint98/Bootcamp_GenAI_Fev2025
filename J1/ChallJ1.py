#Chall1
# Demande à l'utilisateur un nombre et une longueur
number = int(input("Entrez un nombre : "))
length = int(input("Entrez une longueur : "))

# Génère la liste des multiples
multiples = [number * i for i in range(1, length + 1)]

print(multiples)

#Chall2
# Demande un mot à l'utilisateur
word = input("Entrez un mot : ")

# Supprime les lettres consécutives en double
new_word = word[0]  # Premier caractère toujours inclus

for i in range(1, len(word)):
    if word[i] != word[i - 1]:  # Ajoute si différent du précédent
        new_word += word[i]

print(new_word)
