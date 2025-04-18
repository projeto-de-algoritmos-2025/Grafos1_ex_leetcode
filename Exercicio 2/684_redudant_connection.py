from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        total_nos = len(edges)
        grafo = [[] for _ in range(total_nos + 1)]

        def tem_ciclo(no_atual, anterior, visitados):
            visitados[no_atual] = True
            for vizinho in grafo[no_atual]:
                if not visitados[vizinho]:
                    if tem_ciclo(vizinho, no_atual, visitados):
                        return True
                elif vizinho != anterior:
                    return True
            return False

        for a, b in edges:
            grafo[a].append(b)
            grafo[b].append(a)
            visitados = [False] * (total_nos + 1)
            if tem_ciclo(a, -1, visitados):
                return [a, b]

        return []