# Exercice 1 :
print("Hello world\nHello world\nHello world\nHello world")

# Exercice 2 :
result = (99**3) * 8
print(result)

# Exercice 3 :
my_name = "Jean"  # Remplace par ton prénom
user_name = input("Quel est ton nom ? ")
if user_name.lower() == my_name.lower():
    print("Wow, on a le même nom !")
else:
    print(f"Sympa de te rencontrer, {user_name} !")

# Exercice 4 :
height = int(input("Quelle est ta taille en cm ? "))
if height > 145:
    print("Tu es assez grand pour faire le manège !")
else:
    print("Désolé, tu dois encore grandir un peu...")

# Exercice 5 :
my_fav_numbers = {7, 14, 21}  # Exemple
my_fav_numbers.update([42, 99])  # Ajout de deux nombres
my_fav_numbers.remove(max(my_fav_numbers))  # Suppression du dernier
friend_fav_numbers = {5, 10, 42}  # Exemple
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)  # Fusion des ensembles
print(our_fav_numbers)

# Exercice 6 :
# Non, un tuple est immuable (on ne peut pas ajouter d'éléments après sa création).

# Exercice 7 :
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")  # Supprime "Banana"
basket.remove("Blueberries")  # Supprime "Blueberries"
basket.append("Kiwi")  # Ajoute "Kiwi" à la fin
basket.insert(0, "Apples")  # Ajoute "Apples" au début
print("Nombre de pommes :", basket.count("Apples"))  # Compte les "Apples"
basket.clear()  # Vide la liste
print(basket)

# Exercice 8 :

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", 
                   "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", 
                   "Pastrami sandwich"]

# Suppression de tous les "Pastrami sandwich" avec une boucle while
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []  # Liste des sandwichs terminés
index = 0  # Index pour parcourir la liste

# Préparation des sandwichs sans utiliser pop()
while index < len(sandwich_orders):
    sandwich = sandwich_orders[index]
    finished_sandwiches.append(sandwich)
    print(f"J'ai fait ton {sandwich.lower()}")
    index += 1

print("Tous les sandwichs ont été préparés !")

