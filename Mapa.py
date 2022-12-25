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
                #  string += "#"
                #  string += " "
            elif(i==largura-1):
                lista.append("#")
                #  string += "#"
            elif(random.randint(1,200) < 70):
                lista.append("#")
                #  string += "#"
                #  string += " "
            else:
                lista.append("-")
                #  string += "-"
                #  string += " "
            #  self.m.append(string)
        self.m.append(lista)
        #  print(string)
        #  printLinhaFile(string)
        return None

    def linhaPartida(self,largura):
        random_number = random.randint(2, largura-3)
        #  string = ""
        lista = []
        for i in range(largura):
            if(i==random_number or i==(random_number+1) or i==(random_number-1)):
                lista.append("P")
                #  string += "P"
                #  string += " "
            else:
                lista.append("#")
                #  string += "#"
                #  string += " "
            #  self.m.append(string)
        self.m.append(lista)
        #  print(string)
        #  printLinhaFile(string)
        return None

    def linhaVazia(self, largura):
        #  string = ""
        lista = []
        for i in range(largura):
            if(i==0):
                lista.append("#")
                #  string += "#"
                #  string += " "
            elif(i==largura-1):
                lista.append("#")
                #  string += "#"
                #  string += " "
            else:
                lista.append("-")
                #  string += "-"
                #  string += " "
            #  self.m.append(string)
        self.m.append(lista)
        #  print(string)
        #  printLinhaFile(string)

    def linhasMeio(self, largura, altura):
        for i in range(altura-4):
            self.randomLinha(largura)
        return None
    
    def linhaMeta(self, largura):
        random_number = random.randint(2, largura-3)
        #  string = ""
        lista = []
        for i in range(largura):
            if(i==random_number  or i==(random_number+1) or i==(random_number-1)):
                lista.append("F")
                #  string += "F"
                #  string += " "
            else:
                lista.append("#")
                #  string += "#"
                #  string += " "   
            #  self.m.append(string)
        self.m.append(lista)
        #  print(string)
        #  printLinhaFile(string)
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

#def printLinhaFile(line):
#    original_stdout = sys.stdout
#    with open('Mapa.txt', 'a') as f:
#        sys.stdout = f
#        print(line)
#        sys.stdout = original_stdout


