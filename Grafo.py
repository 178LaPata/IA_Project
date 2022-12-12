import math
from queue import Queue
from Nodo import Nodo

import networkx as nx 
import matplotlib.pyplot as plt  

class Grafo:

    def __init__(self):
        self.m_nodos = []
        self.m_grafo = {}
    
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

    def procuraDFS(self, nodoInicial, posFinal, path=[], visited=set()):
        path.append(nodoInicial)
        visited.add(nodoInicial)

        if nodoInicial == posFinal:
            custoT = self.calculaCusto(path)
            return (path, custoT)
        for (adj, peso) in self.m_grafo[nodoInicial]:
            if adj not in visited:
                resultado = self.procuraDFS(adj, posFinal, path, visited)
                if resultado is not None:
                    return resultado
        path.pop()
        return None

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
        for (adj, peso) in self.m_grafo[nodo]:
            lista.append((adj, peso))
        return lista

    #################################
    # Desenha grafo
    #################################

    def desenhaGrafo(self):
        lista_v = self.m_nodos
        lista_a = []
        g = nx.Graph()
        for nodo in lista_v:
            n = nodo.getName()
            g.add_node(n)
            for (adj, peso) in self.m_grafo[n]:
                lista = (n, adj)
                g.add_edge(n, adj, weight=peso)

        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.draw()
        plt.show()

    #################################
    # Heurística
    #################################

    #################################
    # A*
    #################################
    def procuraAstar(self, nodoInicial, posFinal):
        return None
    #################################
    # Greedy
    #################################