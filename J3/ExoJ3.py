#Exercise 1:
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


# Création de trois objets Chat
chat1 = Cat("Milo", 3)
chat2 = Cat("Whiskers", 7)
chat3 = Cat("Luna", 5)

# Fonction pour trouver le chat le plus âgé
def trouver_chat_plus_age(*chats):
    return max(chats, key=lambda chat: chat.age)


# Trouver le chat le plus âgé et afficher son nom et son âge
chat_plus_age = trouver_chat_plus_age(chat1, chat2, chat3)
print(f"Le chat le plus âgé est {chat_plus_age.name}, et il a {chat_plus_age.age} ans.")


#Exercise 2 :
# Définition de la classe Dog
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} aboie !")

    def jump(self):
        print(f"{self.name} saute {self.height * 2} cm de haut !")


# Création des objets chien
chien_david = Dog("Rex", 50)
chien_sarah = Dog("Teacup", 20)

# Affichage des détails et appel des méthodes
print(f"Le chien de David s'appelle {chien_david.name} et mesure {chien_david.height} cm.")
chien_david.bark()
chien_david.jump()

print(f"Le chien de Sarah s'appelle {chien_sarah.name} et mesure {chien_sarah.height} cm.")
chien_sarah.bark()
chien_sarah.jump()

# Vérification du chien le plus grand
if chien_david.height > chien_sarah.height:
    print(f"Le chien le plus grand est {chien_david.name}.")
else:
    print(f"Le chien le plus grand est {chien_sarah.name}.")



#Exercise 3 : 
# Définition de la classe Song
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


# Création d'un objet Song
chanson = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

# Affichage des paroles
chanson.sing_me_a_song()


#Exercise 4:
# Définition de la classe Zoo
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(f"Animaux dans le zoo {self.name} : {', '.join(self.animals)}")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()
        groupes = {}
        for animal in self.animals:
            lettre = animal[0].upper()  #Maj
            if lettre not in groupes:
                groupes[lettre] = []
            groupes[lettre].append(animal)
        return groupes

    def get_groups(self):
        groupes = self.sort_animals()
        for lettre, animaux in groupes.items():
            print(f"{lettre}: {', '.join(animaux)}")


# Création d'un objet Zoo
ramat_gan_safari = Zoo("Ramat Gan Safari")

# Ajout des animaux
ramat_gan_safari.add_animal("Girafe")
ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Tigre")
ramat_gan_safari.add_animal("Zèbre")
ramat_gan_safari.add_animal("Éléphant")
ramat_gan_safari.add_animal("Léopard")

# Affichage des animaux
ramat_gan_safari.get_animals()

# Vente d'un animal
ramat_gan_safari.sell_animal("Tigre")

# Affichage après vente
ramat_gan_safari.get_animals()

# Affichage des groupes d'animaux triés
ramat_gan_safari.get_groups()
