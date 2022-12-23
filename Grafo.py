import math
from queue import Queue
from Nodo import Nodo

import networkx as nx 
import matplotlib.pyplot as plt  

class Grafo:

    def __init__(self):
        self.m_nodos = []
        self.m_grafo = {}
        self.m_h = {} 
    
    #################################
    # Escrever o grafo como string
    #################################

    def __str__(self):
        r = ""
        for key in self.m_grafo.keys():
            r = r + "Nodo: " + str(key) + ": " + str(self.m_grafo[key]) + "\n"

        return r

    #################################
    # Encontrar o nodo
    #################################

    def getNodo(self, nodo):
        nodoTeste = Nodo(*nodo)

        for n in self.m_nodos:
            if n == nodoTeste:
                return n

        return None

    #################################
    # Adicionar aresta no grafo
    #################################

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

    #################################
    # Devolver o custo de uma aresta
    #################################

    def getCustoArco(self, nodo1, nodo2):
        custoT = math.inf
        a = self.m_grafo[str(nodo1)]
        for nodo,custo in a:
            if nodo==nodo2:
                custoT=custo

        return custoT
        
    #################################
    # Calcula o custo de um caminho
    #################################

    def calculaCusto(self, caminho):
        custo = 0
        i = 0

        while i+1 < len(caminho):
            custo = custo + self.getCustoArco(caminho[i], caminho[i+1])
            i+=1

        return custo
    
    #################################
    # Procura DFS
    #################################

    def procuraDFS(self, nodoInicial, posFinal, caminho=[], visited=set()):
        caminho.append(nodoInicial)
        visited.add(nodoInicial)

        if nodoInicial.getPos() == posFinal:
            custoT = self.calculaCusto(caminho)
            return (caminho, custoT)
        for (adj, peso) in self.m_grafo[str(nodoInicial)]:
            if adj not in visited:
                resultado,_ = self.procuraDFS(adj, posFinal, caminho, visited)
                if resultado is not None:
                    return resultado, None
        caminho.pop()
        return None, None

    #################################
    # Procura BFS
    #################################

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


    #################################
    # Devolve vizinhos de um nodo
    #################################

    def getNeighbours(self, nodo):
        lista = []
        for (adj, peso) in self.m_grafo[str(nodo)]:
            lista.append((adj, peso))
        return lista

    #################################
    # Define heurística para cada nodo
    #################################

    def adicionaHeuristica(self, n, estima):
        n1 = Nodo(n)
        if n1 in self.m_nodos:
            self.m_h[n] = estima

    #################################
    # Define heurística para cada nodo 1 por defeito
    #################################

    def heuristica(self, posFinal):
        nodos = self.m_graph.keys()
        for n in nodos:
            self.m_h[n] = math.sqrt((posFinal.x - n.x)**2 + (posFinal.y - n.y)**2)
        return (True)

    def calculaEst(self, estima):
        l = list(estima.keys())
        min_estima = estima[l[0]]
        node = l[0]
        for k, v in estima.items():
            if v < min_estima:
                min_estima = v
                node = k
        return node

    #################################
    # Procura A*
    #################################

    def procura_aStar(self, nodoInicial, posFinal):
        open_list = {nodoInicial}
        closed_list = set([])

        g = {}
        g[nodoInicial] = 0

        parents = {}
        parents[nodoInicial] = nodoInicial
        
        n = None
        
        while len(open_list) > 0:
            #n = None

            calc_heurist = {}
            flag = 0
            
            for v in open_list:
                if n == None:
                    n = v
                else:
                    flag = 1
                    calc_heurist[v] = g[v] + self.getH(v)
            
            if flag == 1:
                min_estima = self.calculaEst(calc_heurist)
                n = min_estima
            
            if n == None:
                print('O caminho não existe')
                return None

            if n == posFinal:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(nodoInicial)

                reconst_path.reverse()

                return (reconst_path, self.calculaCusto(reconst_path))

            for (adj, peso) in self.getNeighbours(n):
                if adj not in open_list and adj not in closed_list:
                    open_list.add(adj)
                    parents[adj] = n
                    g[adj] = g[n] + peso

                else:
                    if g[adj] > g[n] + peso:
                        g[adj] = g[n] + peso
                        parents[adj] = n

                        if adj in closed_list:
                            closed_list.remove(adj)
                            open_list.add(adj)

            open_list.remove(n)
            closed_list.add(n)

        print('O caminho não existe')
        return None

    #################################
    # Devolve heurística do nodo
    #################################

    def getH(self, nodo):
        if nodo not in self.m_h.keys():
            return 1000
        else:
            return (self.m_h[str(nodo)])

    #################################
    # Procura Greedy
    #################################

    def procuraGreedy(self, nodoInicial, posFinal):
        open_list = set([nodoInicial])
        closed_list = set([]) 

        parents = {}
        parents[nodoInicial] = nodoInicial

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n == None or self.m_h(v) < self.m_h(n):
                    n = v

            if n == None:
                print("O caminho não existe")
                return None

            if n == posFinal:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(nodoInicial)

                reconst_path.reverse()
                
                return (reconst_path, self.calculaCusto(reconst_path))

            for (adj, peso) in self.getNeighbours(n):
                if adj not in open_list and adj not in closed_list:
                    open_list.add(adj)
                    parents[adj] = n

            open_list.remove(n)
            closed_list.add(n)

        print('O caminho não existe!')
        return None

