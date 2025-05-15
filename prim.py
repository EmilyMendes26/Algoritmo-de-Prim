import heapq
from heapq import heappop, heappush

grafo = {
    'A': [('D',0),('B',1)],
    'B': [('D',1),('C',2)],
    'C': [('F',3)],
    'D': [('E',4), ('B',5)],
    'E': [('C',6)],
    'F': [('C',0),('E',5)]
}

folhas = []
mst = []
visitados = []

for pai in grafo:
    for destino, peso in grafo[pai]:
        folha = (peso, destino, pai)
        folhas.append(folha)

for folha in folhas:
    print(folha)

