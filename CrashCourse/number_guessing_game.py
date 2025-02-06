import random
def nmb_guess():
    random_number = random.randint(1, 100)
    max_attempts = 7
    attempt = 0

    for attempt in range(max_attempts):
        num = int(input(f"Trouve le nombre entre 1 et 100. Vous avez fait {attempt} tentative: "))
        if num < random_number:
            print("Trop bas!")
            attempt = attempt + 1
        elif num > random_number:
            print("Trop haut!")
            attempt = attempt + 1
        else: 
            print("Félicitation! Vous avez deviné le nombre!")
            return
    print("Vous avez épuisé toute vos tentative! Le nombre était le ", random_number)
nmb_guess()