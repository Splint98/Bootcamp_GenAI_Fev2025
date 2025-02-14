class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items if items is not None else []  # Liste des éléments
        self.pageSize = int(pageSize)  # Convertit en entier au cas où un flottant est donné
        # Calcule le nombre total de pages en arrondissant vers le haut
        self.totalPages = max(1, (len(self.items) + self.pageSize - 1) // self.pageSize)  
        self.currentPage = 1  # La pagination commence à la page 1

    def getVisibleItems(self):
        start = (self.currentPage - 1) * self.pageSize  # Indice de début
        end = start + self.pageSize  # Indice de fin
        return self.items[start:end]  # Retourne les éléments correspondants

    def prevPage(self):
        self.currentPage = max(1, self.currentPage - 1)  # S'assure que la page ne descend pas en dessous de 1
        return self  

    def nextPage(self):
        self.currentPage = min(self.totalPages, self.currentPage + 1)  # S'assure que la page ne dépasse pas le total
        return self  

    def firstPage(self):
        self.currentPage = 1
        return self  

    def lastPage(self):
        self.currentPage = self.totalPages
        return self  

    def goToPage(self, pageNum):
        pageNum = int(pageNum)  # Convertit en entier au cas où un flottant est donné
        self.currentPage = max(1, min(self.totalPages, pageNum))  # Ajuste si la page demandée est hors limites
        return self  


# TEST
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 3)  

print(p.getVisibleItems())  # ["a", "b", "c", "d"]
p.nextPage()
print(p.getVisibleItems())  # ["e", "f", "g", "h"]
p.lastPage()
print(p.getVisibleItems())  # ["y", "z"]
p.goToPage(2)
print(p.getVisibleItems())  # ["e", "f", "g", "h"]
p.prevPage().prevPage()
print(p.getVisibleItems())  # ["a", "b", "c", "d"]
