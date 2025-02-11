# dans l'arbre : ~/Documents/Bootcamp_GenAI_Fev2025
# Git add .
# Git commit -m "chaine de commentaire"


#Exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

#Output expected : {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

zipped = zip(keys, values)
Output = dict(zipped)
print(Output)


#Exercise 2

# Dictionnaire initial de la famille
family = {"rick": 43, 'beth': 13, 'morty': 5, 'ete': 8}

# Fonction pour calculer le prix du billet selon l'âge
def calculate_ticket_price(age):
    if age < 3:
        return 0
    elif 3 <= age <= 12:
        return 10
    else:
        return 15

# Variable pour le coût total
total_cost = 0

# Calcul du coût pour chaque membre de la famille
for member, age in family.items():
    price = calculate_ticket_price(age)
    total_cost += price
    print(f"{member.capitalize()} has to pay ${price}")

# Affichage du coût total
print(f"\nTotal cost for the family: ${total_cost}")


#Exercice 3
#1 : Créer le dictionnaire brand
brand = {
    "name": "Zara",  # Nom de la marque
    "creation_date": 1975,  # Date de création
    "creator_name": "Amancio Ortega Gaona",  # Nom du créateur
    "type_of_clothes": ["men", "women", "children", "home"],  # Types de vêtements vendus
    "international_competitors": ["Gap", "H&M", "Benetton"],  # Concurrents internationaux
    "number_stores": 7000,  # Nombre de magasins
    "major_color": {  # Couleurs principales par pays
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

#2 : Modifier le nombre de magasins à 2
brand["number_stores"] = 2

#3 : Afficher qui sont les clients de Zara
print(f"Les clients de Zara incluent {', '.join(brand['type_of_clothes'])}.")

#4 : Ajouter la clé country_creation avec la valeur "Spain"
brand["country_creation"] = "Spain"

#5 : Vérifier si la clé international_competitors existe et ajouter "Desigual" si c'est le cas
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

#6 : Supprimer la date de création
del brand["creation_date"]

#7 : Afficher le dernier concurrent international
print(brand["international_competitors"][-1])

#8 : Afficher les couleurs principales aux États-Unis
print(brand["major_color"]["US"])

#9 : Afficher le nombre de paires clé-valeur dans le dictionnaire
print(len(brand))

#10 : Afficher les clés du dictionnaire
print(brand.keys())

#11 : Créer un autre dictionnaire more_on_zara
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

#12 : Fusionner le dictionnaire more_on_zara avec brand
brand.update(more_on_zara)

#13 : Afficher la valeur de number_stores
print(brand["number_stores"])

#Exercise 4 :
# Fonction describe_city
def describe_city(city, country="France"):
    print(f"{city} est en {country}.")

# Appel de la fonction avec une ville en France (valeur par défaut)
describe_city("Paris")

# Appel de la fonction avec une ville dans un autre pays
describe_city("Tokyo", "Japon")
describe_city("New York", "États-Unis")

#Exercice 5 :
import random  # Importation du module random

# Définition de la fonction
def guess_number(user_number):
    if 1 <= user_number <= 100:  # Vérif entre 1 et 100
        random_number = random.randint(1, 100)  # aléatoire entre 1 et 100

        # Comparaison
        if user_number == random_number:
            print("Vous avez deviné le bon nombre !")
        else:
            print(f"Votre nombre: {user_number}, Nombre généré: {random_number}. Fail !")
    else:
        print("Erreur : Veuillez entrer un nombre entre 1 et 100.")

# Test 
guess_number(26) 

#Exercise 6 :
def make_shirt(size="Large", message="I love Python"):
    print(f"La taille du t-shirt est {size} et le message imprimé est : \"{message}\"")

make_shirt()

make_shirt("Medium")

make_shirt("Small", "Code is Life!")

make_shirt(message="Keep Calm and Code On", size="XL")

#Exercice 7 :
import random 

def get_random_temp(season):

    if season.lower() == "hiver":
        return random.randint(-10, 16)  # Température entre -10 et 16°C en hiver
    elif season.lower() == "printemps":
        return random.randint(5, 22)  # Température entre 5 et 22°C au printemps
    elif season.lower() == "ete":
        return random.randint(20, 40)  # Température entre 20 et 40°C en été
    elif season.lower() == "automne":
        return random.randint(5, 25)  # Température entre 5 et 25°C en automne
    else:
        print("Saison invalide, génération d'une température par défaut entre -10 et 40°C.")
        return random.randint(-10, 40)

# Étape 2 : Définition de la fonction principale
def main():
    season = input("Entrez une saison (hiver, printemps, ete, automne) : ").strip().lower()

    temperature = get_random_temp(season)

    print(f"La température actuelle est de {temperature}°C.")

    if temperature < 0:
        print("Brrr, il fait froid ! Mettez plusieurs couches de vêtements ! ")
    elif 0 <= temperature <= 16:
        print("Il fait plutôt frais ! N'oubliez pas votre manteau. ")
    elif 16 < temperature <= 23:
        print("La température est agréable, profitez de la journée !")
    elif 24 <= temperature <= 32:
        print("Il fait chaud ! Pensez à bien vous hydrater.")
    else:
        print("Il fait très chaud ! Restez à l'ombre et buvez beaucoup d'eau.")

main()
