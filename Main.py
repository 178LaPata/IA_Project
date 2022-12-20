from copy import deepcopy
import os
from Problema import Problema
from Menu import Menu
from Mapa import Mapa


def printMapa(mapa):
    os.system("clear")
   
    MAXX = len(mapa[0])
    print(len(str(len(mapa))) * " ", end="")
    for x in range(0, MAXX):
        print(f"{x:<{len(str(MAXX))}}", end="")
    print()
    for y, linha in enumerate(mapa):
        print(y, end=" ")
        for val in linha:
            #  print(val, end="")
            print(f"{val:{len(str(MAXX))}}", end="")
        print()

def printCaminhoMapa(caminho, custo, mapa):
    aux = deepcopy(mapa.m)

    for node in caminho:
        #  os.system("clear")
        pos = node.getPos()
        aux[pos[1]][pos[0]] = "o"
        printMapa(aux)
        os.system("sleep 1")
    
    print(f"Custo = {custo}")
    input("Pressione alguma tecla para voltar...")

def printMenuPrincipal():
    print(Menu().printMenu())
    print("1 -> Mostrar Mapa")
    print("2 -> Construir problema e desenhar Grafo") # mudar nome
    print("3 -> Procura DFS")
    print("4 -> Procura BFS")
    print("5 -> Procura A*")
    print("6 -> Procura Greedy")
    print("0 -> Sair")

def leropção(opcMax):
    opção = -1
    try:
        opção = int(input("Introduza uma opção: "))
    except:
        print("Introduza um valor válido")

    while opção < 0 or opção > opcMax:
        try:
            opção = int(input("Introduza uma opção: "))
        except:
            print("Introduza um valor válido")        
    
    return opção

def main ():
    # mapastr =  "#######I#######\n#####     #####\n##           ##\n#     ###     #\n#   #######   #\n###  ####    ##\n##   ###    ###\n###   ###    ##\n####        ###\n#######F#######"
    # mapastr = mapastr.split("\n")
    # mapa = [[c for c in linha] for linha in mapastr]
    #  printMapa(mapa)
    # problema = Problema(mapa)
    #  print("A construir grafo....")
    # problema.constroiGrafo()
   
    problema = None
    mapa = None

    sair = False
    while not sair:
        os.system("clear")
        printMenuPrincipal()
        opção = leropção(10)

        if opção == 1:           
            #printMapa(mapa)
            if mapa is None:
                largura = int(input("LARGURA -> "))
                altura = int(input("ALTURA -> "))
            #  open('Mapa.txt', "w").close() # da clean ao file antes de escrever ???
                mapa = Mapa()
                mapa.mapaAleatorio(largura, altura)
            mapa.printMapa()
            input("Pressione alguma tecla para voltar...")
        elif opção == 2: 
            if mapa is None:
                print("Mapa deve ser criado primeiramente...")
                input("Pressione uma tecla para continuar..")
                continue
            if problema is None:
                problema = Problema(mapa)
                print("A construir grafo....")
                problema.constroiGrafo()
            print(problema.grafo)
            input("Pressione alguma tecla para voltar...")
        elif opção == 3: # DFS
            if problema is None:
                print("Problema deve ser construido primeiro....")
                input("Pressione alguma tecla para continuar...")
            else:
                caminho,custo = problema.solucaoDFS()
                printCaminhoMapa(caminho, custo, mapa)
        elif opção == 4: # BFS
            if problema is None:
                print("Problema deve ser construido primeiro....")
                input("Pressione alguma tecla para continuar...")
            else:
                caminho,custo = problema.solucaoBFS()
                printCaminhoMapa(caminho, custo, mapa)
        elif opção == 5: # A*
            if problema is None:
                print("Problema deve ser construido primeiro....")
                input("Pressione alguma tecla para continuar...")
            else:
                caminho, custo = problema.solucaoAStar()
                printCaminhoMapa(caminho, custo, mapa)            
        elif opção == 6: # Greedy
            if problema is None:
                print("Problema deve ser construido primeiro....")
                input("Pressione alguma tecla para continuar...")
            else: 
                caminho, custo = problema.solucaoGreedy()
                printCaminhoMapa(caminho, custo, mapa)        
        else:
            print("A sair...")
            sair = True

if __name__ == "__main__":
    main()      

