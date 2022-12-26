import random
import sys
class Mapa:
    def __init__(self):
        self.m = []
        
    def randomLinha(self, largura):
        lista = []
        for i in range(largura):
            if(i==0):
                lista.append("#")
            elif(i==largura-1):
                lista.append("#")
            elif(random.randint(1,200) < 70):
                lista.append("#")
            else:
                lista.append("-")
        self.m.append(lista)
        return None

    def linhaPartida(self,largura):
        random_number = random.randint(1, largura-2)
        lista = []
        for i in range(largura):
            if(i==random_number):
                lista.append("P")
            else:
                lista.append("#")
        self.m.append(lista)
        return None

    def linhaVazia(self, largura):
        lista = []
        for i in range(largura):
            if(i==0):
                lista.append("#")
            elif(i==largura-1):
                lista.append("#")
            else:
                lista.append("-")
        self.m.append(lista)

    def linhasMeio(self, largura, altura):
        for i in range(altura-4):
            self.randomLinha(largura)
        return None
    
    def linhaMeta(self, largura):
        random_number = random.randint(1, largura-2)
        lista = []
        for i in range(largura):
            if(i==random_number):
                lista.append("F")
            else:
                lista.append("#")
        self.m.append(lista)
        return None
    
    def mapaAleatorio(self, largura, altura):
        self.linhaPartida(largura)
        self.linhaVazia(largura)
        self.linhasMeio(largura, altura)
        self.linhaVazia(largura)
        self.linhaMeta(largura)
        return None

    def printMapa(self):
        for linha in self.m:
            for c in linha:
                print(c, end=" ")

            print()