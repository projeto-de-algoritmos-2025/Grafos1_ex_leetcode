class Graph:
    def __init__(self, num_vertices: int, arestas: List[List[int]]):
        self.num_vertices = num_vertices
        self.matriz_adjacencia = [[float('inf')] * num_vertices for _ in range(num_vertices)]
        for origem, destino, peso in arestas:
            self.matriz_adjacencia[origem][destino] = peso

    def addEdge(self, aresta: List[int]) -> None:
        origem, destino, peso = aresta
        self.matriz_adjacencia[origem][destino] = peso

    def shortestPath(self, vertice_inicial: int, vertice_final: int) -> int:
        distancias = [float('inf')] * self.num_vertices
        distancias[vertice_inicial] = 0
        visitados = [False] * self.num_vertices
        
        for _ in range(self.num_vertices):
            proximo_vertice = -1
            for vertice in range(self.num_vertices):
                if not visitados[vertice] and (proximo_vertice == -1 or distancias[proximo_vertice] > distancias[vertice]):
                    proximo_vertice = vertice
            visitados[proximo_vertice] = True
            
            for vertice in range(self.num_vertices):
                if self.matriz_adjacencia[proximo_vertice][vertice] != float('inf'):
                    distancias[vertice] = min(distancias[vertice], distancias[proximo_vertice] + self.matriz_adjacencia[proximo_vertice][vertice])
        
        return -1 if distancias[vertice_final] == float('inf') else distancias[vertice_final]
