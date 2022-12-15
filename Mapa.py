import random
class Mapa:
    def randomLinha(largura):
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
        print(string)
        return None

    def linhaPartida(largura):
        random_number = random.randint(1, largura-2)
        string = ""
        for i in range(largura):
            if(i==random_number):
                string += "P"
                string += " "
            else:
                string += "#"
                string += " "
        print(string)
        return None

    def linhaVazia(largura):
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
        print(string)

    def linhasMeio(largura, altura):
        for i in range(altura-4):
            Mapa.randomLinha(largura)
        return None
    
    def linhaMeta(largura):
        random_number = random.randint(1, largura-2)
        string = ""
        for i in range(largura):
            if(i==random_number):
                string += "F"
                string += " "
            else:
                string += "#"
                string += " "   
        print(string)
        return None
    
    def mapaAleatorio(largura, altura):
        Mapa.linhaPartida(largura)
        Mapa.linhaVazia(largura)
        Mapa.linhasMeio(largura, altura)
        Mapa.linhaVazia(largura)
        Mapa.linhaMeta(largura)
        return None

