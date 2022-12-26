from Grafo import Grafo
from Nodo import Nodo
from Mapa import Mapa

class Problema:
    
    def __init__(self, mapa):

        self.mapa = mapa.m
        self.posInicial = [-1, -1]
        self.posFinal = [-1, -1]

        for y, linha in enumerate(self.mapa):
            for x, c in enumerate(linha):
                if c == "P":
                    self.posInicial = [x, y]
                elif c == "F":
                    self.posFinal = [x, y]

        self.grafo = Grafo(mapa.m)

    def constroiGrafo(self):

        estadoInicial = (self.posInicial[0], self.posInicial[1], 0, 0)
        paraExpandir = []
        paraExpandir.append(estadoInicial)
        self.grafo.m_nodos.append(Nodo(*estadoInicial))
        self.grafo.m_grafo[str(Nodo(*estadoInicial))] = list()
        expandidos = set()

        while len(paraExpandir) > 0:

            estado = paraExpandir.pop(0)
            expandir = self.expande(estado)
            expandidos.add(estado)

            if len(expandir) == 0:
                continue

            for est, peso in expandir:
                self.grafo.adicionaAresta(estado, est, peso)
                if est not in expandidos and est not in paraExpandir:
                    paraExpandir.append(est)
                    expandidos.add(est)

        self.grafo.heuristica(Nodo(self.posFinal[0], self.posFinal[1], 0, 0))

    def expande(self, estado):

        pos = [estado[0], estado[1]]
        vel = [estado[2], estado[3]]

        if pos[0] < 0 or pos[0] >= len(self.mapa[0]) or pos[1] < 0 or pos[1] >= len(self.mapa) or self.mapa[pos[1]][pos[0]] == "#":
            return [((pos[0]-vel[0], pos[1]-vel[1], 0, 0), 25)]

        jogadasPossiveis = []
        if vel != [0, 0]:
            jogadasPossiveis.append([0, 0])

        for ax in [-1, 0, 1]:
            for ay in [-1, 0, 1]:
                if ax == 0 and ay == 0:
                    continue
                jogadasPossiveis.append([ax, ay])

        return list(filter(lambda x: x is not None, map(lambda x: self.aplicaAceleracao(estado, x), jogadasPossiveis)))

    def aplicaAceleracao(self, estado, aceleracao):

        pos = [estado[0], estado[1]]
        vel = [estado[2], estado[3]]

        vel[0] += aceleracao[0]
        vel[1] += aceleracao[1]

        newPos = [pos[0]+vel[0], pos[1]+vel[1]]

        if newPos[0] < 0 or newPos[0] >= len(self.mapa[0]) or newPos[1] < 0 or newPos[1] >= len(self.mapa) or self.mapa[newPos[1]][newPos[0]] == "#":
            return ((newPos[0], newPos[1], vel[0], vel[1]), 1)

        valido = False

        xMenor, xMaior = pos[0], newPos[0]
        if xMenor > xMaior:
            xMenor, xMaior = xMaior, xMenor
        yMenor, yMaior = pos[1], newPos[1]
        if yMenor > yMaior:
            yMenor, yMaior = yMaior, yMenor

        if "#" not in self.mapa[yMenor][xMenor:xMaior+1] and "#" not in list(map(lambda l: l[xMaior], self.mapa))[yMenor:yMaior+1]:
            valido = True

        if "#" not in list(map(lambda l: l[xMenor], self.mapa))[yMenor:yMaior+1] and "#" not in self.mapa[yMaior][xMenor:xMaior+1]:
            valido = True

        if valido:
            return ((newPos[0], newPos[1], vel[0], vel[1]), 1)

        return None

    def solucaoDFS(self):
        nodoInicial = self.grafo.getNodo((self.posInicial[0], self.posInicial[1], 0, 0))
        return self.grafo.procuraDFS(nodoInicial, self.posFinal)

    def solucaoBFS(self):
        nodoInicial = self.grafo.getNodo((self.posInicial[0], self.posInicial[1], 0, 0))
        return self.grafo.procuraBFS(nodoInicial, self.posFinal)

    def solucaoAStar(self):
        nodoInicial = self.grafo.getNodo((self.posInicial[0], self.posInicial[1], 0, 0))
        return self.grafo.procura_aStar(nodoInicial, self.posFinal)

    def solucaoGreedy(self):
        nodoInicial = self.grafo.getNodo((self.posInicial[0], self.posInicial[1], 0, 0))
        return self.grafo.procuraGreedy(nodoInicial, self.posFinal)
