#ChallJ3
# Définition de la classe Farm
class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, count=1):
        if animal in self.animals:
            self.animals[animal] += count
        else:
            self.animals[animal] = count

    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"
        info += "\nE-I-E-I-O!"
        return info


# Instanciation de la ferme
macdonald = Farm("McDonald")

# Ajout des animaux
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

# Affichage des informations de la ferme
print(macdonald.get_info())
