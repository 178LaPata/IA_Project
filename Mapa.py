import random
import sys
class Mapa:
    def __init__(self):
        self.m = []
        
    def randomLinha(self, largura):
        string = ""
        for i in range(largura):
            if(i==0):
                string += "#"
                string += " "
            elif(i==largura-1):
                string += "#"
            elif(random.randint(1,200) < 70):
                string += "#"
                string += " "
            else:
                string += "-"
                string += " "
            self.m.append(string)
        print(string)
        printLinhaFile(string)
        return None

    def linhaPartida(self,largura):
        random_number = random.randint(1, largura-2)
        string = ""
        for i in range(largura):
            if(i==random_number):
                string += "P"
                string += " "
            else:
                string += "#"
                string += " "
            self.m.append(string)
        print(string)
        printLinhaFile(string)
        return None

    def linhaVazia(self, largura):
        string = ""
        for i in range(largura):
            if(i==0):
                string += "#"
                string += " "
            elif(i==largura-1):
                string += "#"
                string += " "
            else:
                string += "-"
                string += " "
            self.m.append(string)
        print(string)
        printLinhaFile(string)

    def linhasMeio(self, largura, altura):
        for i in range(altura-4):
            self.randomLinha(largura)
        return None
    
    def linhaMeta(self, largura):
        random_number = random.randint(1, largura-2)
        string = ""
        for i in range(largura):
            if(i==random_number):
                string += "F"
                string += " "
            else:
                string += "#"
                string += " "   
            self.m.append(string)
        print(string)
        printLinhaFile(string)
        return None
    
<<<<<<< HEAD
    def mapaAleatorio(self, largura, altura):
        self.linhaPartida(largura)
        self.linhaVazia(largura)
        self.linhasMeio(largura, altura)
        self.linhaVazia(largura)
        self.linhaMeta(largura)
        return None
=======
    def mapaAleatorio(largura, altura):
        Mapa.linhaPartida(largura)
        Mapa.linhaVazia(largura)
        Mapa.linhasMeio(largura, altura)
        Mapa.linhaVazia(largura)
        Mapa.linhaMeta(largura)
        return Mapa
>>>>>>> 30397a17b14f5ac4957f7712c5a5b3bded6a018d


def printLinhaFile(line):
    original_stdout = sys.stdout
    with open('Mapa.txt', 'a') as f:
        sys.stdout = f
        print(line)
        sys.stdout = original_stdout


