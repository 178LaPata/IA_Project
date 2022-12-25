#import pygame
#from pygame.locals import *
from copy import deepcopy
from colorama import Fore
import os
from Problema import Problema
from Menu import printMenu
from Mapa import Mapa
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
            #  print(val, end="")
            print(f"{val:{len(str(MAXX))}}", end="")
        print()

def printCaminhoMapa(caminho, custo, mapa):
    aux = deepcopy(mapa.m)

    posAnt = [-1,-1]
    parede = False
    for node in caminho:
        if parede:
            aux[posAnt[1]][posAnt[0]] = "#"
        #os.system("clear")
        pos = node.getPos()
        if (pos[0] < 0 or pos[0] > len(aux[0])) or (pos[1] < 0 or pos[1] > len(aux)):
            continue
        if aux[pos[1]][pos[0]] == "#":
            parede = True
        else:
            parede = False
        aux[pos[1]][pos[0]] = "o"

        printMapa(aux)
        os.system("sleep 1")

        posAnt = pos
    
    print(f"Custo = {custo}")
    input("Pressione alguma tecla para voltar...")

def printMenuPrincipal():
    printMenu()
    print("1 -> Mostrar Mapa")
    print("2 -> Escolher Jogadores")
    print("3 -> Construir Problema")
    print("4 -> Procura DFS")
    print("5 -> Procura BFS")
    print("6 -> Procura A*")
    print("7 -> Procura Greedy")
    print("0 -> Sair")

def printJogadores():
    print("1 -> 1 Jogador")
    print("2 -> 2 Jogadores")

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
    # printMapa(mapa)
    # problema = Problema(mapa)
    # print("A construir grafo....")
    # problema.constroiGrafo()
    problema = None
    mapa = None
    player = None

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
                #open('Mapa.txt', "w").close() # da clean ao file antes de escrever ???
                mapa = Mapa()
                mapa.mapaAleatorio(largura, altura)
            mapa.printMapa()
            input("Pressione alguma tecla para voltar...")
        elif opção == 2: #Escolher jogadores
            if mapa is None:
                print("Mapa deve ser criado primeiro...")
                input("Pressione alguma tecla para continuar...")
                continue
            if player is None:
                printJogadores()
                opçãoJogador = leropção(2)
                if opçãoJogador == 1:
                    player = 1
                elif opçãoJogador == 2:
                    player = 2
                input("Pressione alguma tecla para continuar...")                      
        elif opção == 3: #Construir problema
            if mapa is None:
                print("Mapa deve ser criado primeiro...")
                input("Pressione alguma tecla para continuar...")
                continue
            if player is None:
                print("Número de jogadores deve ser selecionado primeiro")
                input("Pressione alguma tecla para continuar...")
                continue
            if problema is None:
                problema = Problema(mapa)
                print("A construir grafo...")
                if player == 1:
                    problema.constroiGrafo()
                elif player == 2:
                    problema.constroiGrafo()
                    problema.constroiGrafo2()
                #print(problema.grafo)
            input("Pressione alguma tecla para voltar...")
        elif opção == 4: # DFS
            if problema is None:
                print("Problema deve ser construido primeiro...")
                input("Pressione alguma tecla para continuar...")
            else: 
                caminho,custo = problema.solucaoDFS()
                printCaminhoMapa(caminho, custo, mapa)
        elif opção == 5: # BFS
            if problema is None:
                print("Problema deve ser construido primeiro...")
                input("Pressione alguma tecla para continuar...")
            else:
                caminho,custo = problema.solucaoBFS()
                printCaminhoMapa(caminho, custo, mapa)
        elif opção == 6: # A*
            if problema is None:
                print("Problema deve ser construido primeiro...")
                input("Pressione alguma tecla para continuar...")
            else:
                caminho, custo = problema.solucaoAStar()
                printCaminhoMapa(caminho, custo, mapa)            
        elif opção == 7: # Greedy
            if problema is None:
                print("Problema deve ser construido primeiro...")
                input("Pressione alguma tecla para continuar...")
            else: 
                caminho, custo = problema.solucaoGreedy()
                printCaminhoMapa(caminho, custo, mapa)        
        else:
            print("A sair...")
            sair = True

if __name__ == "__main__":
    main()      

