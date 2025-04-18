class Solution:
    def cloneGraph(self, no):
        antigo_para_novo = {}

        def busca_profundidade(no):
            if no in antigo_para_novo:
                return antigo_para_novo[no]

            copia = Node(no.val)
            antigo_para_novo[no] = copia

            for vizinho in no.neighbors:
                copia.neighbors.append(busca_profundidade(vizinho))
            
            return copia

        return busca_profundidade(no) if no else None
