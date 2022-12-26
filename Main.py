from copy import deepcopy
from colorama import Fore
import os
from Problema import Problema
from Menu import printMenu
from Mapa import Mapa
import time

def printMapa(mapa):
    os.system("clear")
    
    MAXX = len(mapa[0])
    
    print((len(str(len(mapa)))+1) * " ", end="")
    
    for x in range(0, MAXX):
        print(f"{x:<{len(str(MAXX))}}", end="")
    print()

    for y, linha in enumerate(mapa):
        print(y, end=(len(str(len(mapa)))+1-len(str(y))) * " ")
        for val in linha:
            print(f"{val:{len(str(MAXX))}}", end="")
        print()

def printCaminhoMapa(caminho, custo, mapa):
    aux = deepcopy(mapa.m)

    posAnt = [-1,-1]
    parede = False
    for node in caminho:
        if parede:
            aux[posAnt[1]][posAnt[0]] = "#"
        pos = node.getPos()
        if (pos[0] < 0 or pos[0] > len(aux[0])) or (pos[1] < 0 or pos[1] > len(aux)):
            continue
        if aux[pos[1]][pos[0]] == "#":
            parede = True
        else:
            parede = False
        aux[pos[1]][pos[0]] = "o"

        printMapa(aux)
        time.sleep(1)

        posAnt = pos
    
    print(f"Custo = {custo}")
    input("Pressione alguma tecla para voltar...")

def printCaminhoComp(caminho1, caminho2, custo1, custo2, mapa):
    aux1 = deepcopy(mapa.m)
    
    caracter = {1:"O", 2:"o"}
    caminhos = {1:caminho1, 2:caminho2}

    posAnt = {1:[-1,-1], 2:[-1,-1]}
    parede = {1:False, 2:False}
    finished = 0

    while finished != 2:
        for j, caminho in caminhos.items():
            if len(caminho) == 0:
                continue
            node = caminho.pop(0)
            if parede[j]:
                aux1[posAnt[j][1]][posAnt[j][0]] = "#"
            pos = node.getPos()
            if (pos[0] < 0 or pos[0] > len(aux1[0])) or (pos[1] < 0 or pos[1] > len(aux1)):
                continue
            if aux1[pos[1]][pos[0]] == "#":
                parede[j] = True
            else:
                parede[j] = False
            aux1[pos[1]][pos[0]] = caracter[j]
        
        finished = 0
        for c in caminhos.values():
            if len(c)==0:
                finished += 1
        printMapa(aux1)
        time.sleep(1)
        # os.system("sleep 1")

    # posAnt1 = [-1,-1]
    # posAnt2 = [-1,-1]
    # parede = False

    # for node in caminho1:
    #     if parede:
    #         aux1[posAnt1[1]][posAnt1[0]] = "#"
    #     pos1 = node.getPos()
    #     if (pos1[0] < 0 or pos1[0] > len(aux1[0])) or (pos1[1] < 0 or pos1[1] > len(aux1)):
    #         continue
    #     if aux1[pos1[1]][pos1[0]] == "#":
    #         parede = True
    #     else:
    #         parede = False
    #     aux1[pos1[1]][pos1[0]] = "O"

    #     printMapa(aux1)
    #     os.system("sleep 1")

    #     posAnt1 = pos1

    # for node in caminho2:
    #     if parede:
    #         aux1[posAnt2[1]][posAnt2[0]] = "#"
    #     pos2 = node.getPos()
    #     if (pos2[0] < 0 or pos2[0] > len(aux1[0])) or (pos2[1] < 0 or pos2[1] > len(aux1)):
    #         continue
    #     if aux1[pos2[1]][pos2[0]] == "#":
    #         parede = True
    #     else:
    #         parede = False
    #     aux1[pos2[1]][pos2[0]] = "C"

    #     printMapa(aux1)
    #     os.system("sleep 1")

    #     posAnt2 = pos2

    print(f"Custo Jogador 1 = {custo1}")
    print(f"Custo Jogador 2 = {custo2}")

    input("Pressione alguma tecla para voltar...")

def printMenuPrincipal():
    printMenu()
    print("1 -> Mostrar Mapa")
    print("2 -> Construir Grafo")
    print("3 -> Procura DFS")
    print("4 -> Procura BFS")
    print("5 -> Procura A*")
    print("6 -> Procura Greedy")
    print("7 -> Modo Competitivo")
    print("0 -> Sair")

def printAlgoritmos():
    print("1 -> Procura DFS")
    print("2 -> Procura BFS")
    print("3 -> Procura A*")
    print("4 -> Procura Greedy")

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
    problema = None
    mapa = None
    problema1 = None
    problema2 = None

    sair = False
    while not sair:
        os.system("clear")
        printMenuPrincipal()
        opção = leropção(10)

        if opção == 1:           
            if mapa is None:
                largura = int(input("LARGURA -> "))
                altura = int(input("ALTURA -> "))
                mapa = Mapa()
                mapa.mapaAleatorio(largura, altura)
            mapa.printMapa()
            input("Pressione alguma tecla para voltar...")
        elif opção == 2: 
            if mapa is None:
                print("Mapa deve ser criado primeiro...")
                input("Pressione uma tecla para continuar...")
                continue
            if problema is None:
                problema = Problema(mapa)
                print("A construir grafo...")
                problema.constroiGrafo()
            input("Pressione alguma tecla para voltar...")
        elif opção == 3: # DFS
            if problema is None:
                print("Problema deve ser construido primeiro...")
                input("Pressione alguma tecla para continuar...")
            else: 
                caminho,custo = problema.solucaoDFS()
                printCaminhoMapa(caminho, custo, mapa)
        elif opção == 4: # BFS
            if problema is None:
                print("Problema deve ser construido primeiro...")
                input("Pressione alguma tecla para continuar...")
            else:
                caminho,custo = problema.solucaoBFS()
                printCaminhoMapa(caminho, custo, mapa)
        elif opção == 5: # A*
            if problema is None:
                print("Problema deve ser construido primeiro...")
                input("Pressione alguma tecla para continuar...")
            else:
                caminho, custo = problema.solucaoAStar()
                printCaminhoMapa(caminho, custo, mapa)            
        elif opção == 6: # Greedy
            if problema is None:
                print("Problema deve ser construido primeiro...")
                input("Pressione alguma tecla para continuar...")
            else: 
                caminho, custo = problema.solucaoGreedy()
                printCaminhoMapa(caminho, custo, mapa)        
        elif opção == 7:
                if mapa is None:
                    print("Mapa deve ser criado primeiro...")
                    input("Pressione uma tecla para continuar...")
                    continue
                if problema1 or problema2 is None:
                    problema1 = Problema(mapa)
                    problema2 = Problema(mapa)
                    print("A construir grafo...")
                    problema1.constroiGrafo()
                    problema2.constroiGrafo()
                    input("Pressione alguma tecla para voltar...")
                
                printAlgoritmos()
                
                player1 = int(input("Escolha um algoritmo de procura para o jogador 1 -> "))
                player2 = int(input("Escolha um algoritmo de procura para o jogador 2 -> "))

                if player1 == 1:
                    caminho1,custo1 = problema1.solucaoDFS()
                elif player1 == 2:
                    caminho1,custo1 = problema1.solucaoBFS()
                elif player1 == 3:
                    caminho1,custo1 = problema1.solucaoAStar()
                elif player1 == 4:
                    caminho1,custo1 = problema1.solucaoGreedy()

                if player2 == 1:
                    caminho2,custo2 = problema2.solucaoDFS()
                elif player2 == 2:
                    caminho2,custo2 = problema2.solucaoBFS()
                elif player2 == 3:
                    caminho2,custo2 = problema2.solucaoAStar()
                elif player2 == 4:
                    caminho2,custo2 = problema2.solucaoGreedy()
                
                printCaminhoComp(caminho1, caminho2, custo1, custo2, mapa)
        else:
            print("A sair...")
            sair = True

if __name__ == "__main__":
    main()      
