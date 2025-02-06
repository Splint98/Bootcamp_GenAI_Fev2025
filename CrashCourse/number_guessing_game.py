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
