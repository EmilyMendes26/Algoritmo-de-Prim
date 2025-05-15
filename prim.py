import heapq
from heapq import heappop, heappush

grafo = {
    'A': [('B', 1), ('D', 3)],
    'B': [('A', 1), ('C', 2), ('D', 4)],
    'C': [('B', 2), ('D', 5), ('E', 1)],
    'D': [('A', 3), ('B', 4), ('C', 5), ('E', 2)],
    'E': [('C', 1), ('D', 2)]
}

def prim(grafo,pai):
    folhas = []
    visitados = []
    mst = []
    custo = 0

    visitados.append(pai)
    for pai in grafo:
        for no, peso in grafo[pai]:
            aresta = (peso, pai, no)
            heappush(folhas,aresta)

    while folhas:
        peso, pai, no = heappop(folhas)

        if no not in visitados:
            visitados.append(no)
            mst.append((peso,pai,no))
            custo += peso

            for prox_no, heuristica in grafo[no]:
                if prox_no not in visitados:
                    nova_folha = (heuristica, no, prox_no)
                    heappush(folhas,nova_folha)
    return mst, custo, visitados


mst,custo,visitados = prim(grafo,'D')

print("Arvore geradora minima:")
print(mst)

for aresta in mst:
    peso, pai, no = aresta
    print(f"No visitado: {pai} | Proximo no: {no} | Peso: {peso}")

print (f"Custo total: {custo}")
print (visitados)




