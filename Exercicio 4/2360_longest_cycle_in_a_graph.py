from typing import List

class Solution:
    def longestCycle(self, arestas: List[int]) -> int:
        n = len(arestas)
        visitados = [False] * n
        resultado = -1
        
        for i in range(n):
            if visitados[i]:
                continue
            
            vertice_atual = i
            ciclo = []
            
            while vertice_atual != -1 and not visitados[vertice_atual]:
                visitados[vertice_atual] = True
                ciclo.append(vertice_atual)
                vertice_atual = arestas[vertice_atual]
            
            if vertice_atual == -1:
                continue
            
            tamanho_ciclo = len(ciclo)
            pos_ciclo = next((k for k in range(tamanho_ciclo) if ciclo[k] == vertice_atual), float('inf'))
            
            resultado = max(resultado, tamanho_ciclo - pos_ciclo)
        
        return resultado
