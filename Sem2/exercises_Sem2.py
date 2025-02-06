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
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

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
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

print(brand)
# Update the number of stores
brand["number_stores"] = 2

# Use the 'type_of_clothes' key to print a sentence about Zara's clients
clients = ", ".join(brand["type_of_clothes"])
print(f"Zara's clients are people who shop for {clients}.")

# Add the new key 'country_creation'
brand["country_creation"] = "Spain"

# Print the updated dictionary to see the change
print(brand)

# Check if 'international_competitors' key is in the dictionary
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# Print the updated dictionary to see the change
print(brand)

# Delete the key 'creation_date' from the dictionary
del brand["creation_date"]

# Print the updated dictionary to confirm the change
print(brand)
