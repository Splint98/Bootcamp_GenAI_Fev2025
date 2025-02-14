#Exercise 1:
# Définition de la classe Pets, qui gère plusieurs animaux
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


# Définition de la classe Cat
class Cat():
    is_lazy = True  # Chats sont paresseux par défaut

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} est en train de se promener'


# Définition des différentes races de chats
class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# Création des instances de chats
chat1 = Bengal("Simba", 3)
chat2 = Chartreux("Luna", 5)
chat3 = Siamese("Milo", 2)

# Création de la liste de chats et de l'objet Pets
all_cats = [chat1, chat2, chat3]
sara_pets = Pets(all_cats)

# Faire marcher tous les chats
sara_pets.walk()


#Exercise 2:
# Définition de la classe Dog
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} aboie !"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if self_power > other_power:
            return f"{self.name} a gagné le combat !"
        elif self_power < other_power:
            return f"{other_dog.name} a gagné le combat !"
        else:
            return "C'est un match nul !"


# Création des instances de chiens
dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Bella", 3, 15)
dog3 = Dog("Rocky", 7, 25)

# Test des méthodes
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog3))


#Exercise 3:
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *dog_names):
        names = ", ".join(dog_names)
        print(f"{names} jouent tous ensemble !")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} fait un tonneau !",
                f"{self.name} se tient sur ses pattes arrière !",
                f"{self.name} te serre la main !",
                f"{self.name} fait le mort !"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} n'est pas encore entraîné.")

            #A finir

#Exercise 4 :

# Définition de la classe Family
class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Félicitations ! {kwargs['name']} est né(e) dans la famille {self.last_name}.")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"Famille {self.last_name}:")
        for member in self.members:
            print(member)


# Création d'une instance de la famille
membres = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]
famille = Family("Dupont", membres)

# Test des méthodes
famille.family_presentation()
famille.born(name="Emma", age=0, gender="Female", is_child=True)
famille.family_presentation()
