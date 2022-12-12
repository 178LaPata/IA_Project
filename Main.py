from copy import deepcopy
import os
from Problema import Problema


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
    aux = deepcopy(mapa)

    for node in caminho:
        #  os.system("clear")
        pos = node.getPos()
        aux[pos[1]][pos[0]] = "o"
        printMapa(aux)
        os.system("sleep 1")
    
    print(f"Custo={custo}")
    input("presione alguma tecla para voltar...")

def printMenuPrincipal():
    print("----- Menu Principal -----")
    print("1) Mostrar Mapa")
    print("2) Procura BFS")
    print("0) Sair")

def lerOpcao(opcMax):
    opcao = -1
    try:
        opcao = int(input("Introduza uma opcao:"))
    except:
        print("Introduza um valor válido")

    while opcao < 0 or opcao > opcMax:
        try:
            opcao = int(input("Introduza uma opcao:"))
        except:
            print("Introduza um valor válido")        
    
    return opcao

def main ():
    mapastr =  "#######I#######\n#####     #####\n##           ##\n#     ###     #\n#   #######   #\n###  ####    ##\n##   ###    ###\n###   ###    ##\n####        ###\n#######F#######"
    mapastr = mapastr.split("\n")
    mapa = [[c for c in linha] for linha in mapastr]
    #  printMapa(mapa)
    problema = Problema(mapa)
    print("A construir grafo....")
    problema.constroiGrafo()
    
    sair = False
    while not sair:
        os.system("clear")
        printMenuPrincipal()
        opcao = lerOpcao(2)

        if opcao == 1:
            printMapa(mapa)
            input("presione alguma tecla para voltar...")
        elif opcao == 2:
            caminho,custo = problema.procuraBFS()
            printCaminhoMapa(caminho, custo, mapa)
        else:
            print("A sair..")
            sair = True

if __name__ == "__main__":
    main()
