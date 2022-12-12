import math
from queue import Queue
from Nodo import Nodo

class Grafo:

    def __init__(self):
        self.m_nodos = []
        self.m_grafo = {}
    
    def __str__(self):
        r = ""
        for key in self.m_grafo.keys():
            r = r + "Nodo: " + str(key) + ": " + str(self.m_grafo[key]) + "\n"

        return r

    def getNodo(self, nodo):
        nodoTeste = Nodo(*nodo)

        for n in self.m_nodos:
            if n == nodoTeste:
                return n

        return None

    def adicionaAresta(self, nodo1, nodo2, peso):
        n1 = Nodo(*nodo1)
        n2 = Nodo(*nodo2)

        if n1 not in self.m_nodos:
            self.m_nodos.append(n1)
            self.m_grafo[str(n1)] = list()
        else:
            n1 = self.getNodo(nodo1)
        
        if n2 not in self.m_nodos:
            self.m_nodos.append(n2)
            self.m_grafo[str(n2)] = list()
        else:
            n2 = self.getNodo(nodo2)
    
        self.m_grafo[str(n1)].append((n2, peso))

    def getCustoArco(self, nodo1, nodo2):
        custoT = math.inf
        a = self.m_grafo[str(nodo1)]
        for nodo,custo in a:
            if nodo==nodo2:
                custoT=custo

        return custoT
        

    def calculaCusto(self, caminho):
        custo = 0
        i = 0

        while i+1 < len(caminho):
            custo = custo + self.getCustoArco(caminho[i], caminho[i+1])
            i+=1

        return custo

    def procuraBFS(self, nodoInicial, posFinal):
        pai = {}
        for nodo in self.m_nodos:
            pai[str(nodo)] = (False,None)
        pai[str(nodoInicial)] = (True, None)

        queue = Queue()
        queue.put(nodoInicial)

        while not queue.empty():
            nodo = queue.get()
            for (adj, _) in self.m_grafo[str(nodo)]:
                if adj.getPos() == posFinal:
                    caminho = []
                    pai[str(adj)] = (True, nodo)

                    while adj != None:
                        caminho.append(adj)
                        _, adj = pai[str(adj)]

                    caminho.reverse()
                    return caminho, self.calculaCusto(caminho)
                visited, _ = pai[str(adj)]
                if not visited:
                    pai[str(adj)] = (True, nodo)
                    queue.put(adj)

        return (None, None)
