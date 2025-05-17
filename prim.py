#Importado heappop e heappush para determinar o nó com menor custo para adicionar à folha
from heapq import heappop, heappush

#grafo conexo e ponderado de exemplo para a implementação
grafo = {
    'A': [('B', 1), ('D', 3)],
    'B': [('A', 1), ('C', 2), ('D', 4)],
    'C': [('B', 2), ('D', 5), ('E', 1)],
    'D': [('A', 3), ('B', 4), ('C', 5), ('E', 2)],
    'E': [('C', 1), ('D', 2)]
}

#definindo o algoritmo
def prim(grafo,pai):
    #lista de folhas da árvore
    folhas = []

    #controle de ciclo, pois é um algoritmo guloso de minimização e precisa de uma lista para controles de ciclos
    visitados = []

    #sub árvore gerada de minimização, tem que ser o mesmo resultado independente do nó visitado
    mst = []

    #custo total da mst
    custo = 0

    #adicionando o nó inicial à lista de visitados
    visitados.append(pai)

    #pega o nó conectado ao nó "pai" do grafo
    for no, peso in grafo[pai]:
        #adiciona todas as conexões na aresta
        aresta = (peso, pai, no) 
        #adiciona nas folhas do grafo as arestas conectadas ao nó pai para processamento
        heappush(folhas,aresta) 

    #Repete o código enquanto tiver nó na lista de folhas
    while folhas:
        #pega o peso, pai e o no relacionado à menor folha da tupla e atribui as variaveis
        peso, pai, no = heappop(folhas)

        #verifica se o no com menor custo não foi visitado ainda, se o nó já tiver sido visitado; pegará o próximo nó com menor custo
        if no not in visitados:
            #adiciona o novo nó à lista de visitados
            visitados.append(no)

            #adiciona também à mst
            mst.append((peso,pai,no))

            #soma o custo na varíavel
            custo += peso

            #pega as conexões do nó adicionado à mst
            for prox_no, heuristica in grafo[no]:
                #verifica se as próximas conexões não foram visitadas
                if prox_no not in visitados:
                    #a nova folha sera uma tupla com todos os nós conectados com o novo nó
                    nova_folha = (heuristica, no, prox_no)
                    #adiciona na lista de folhas essa nova tupla
                    heappush(folhas,nova_folha)
    #Quando o while acabar, retorna a mst gerada, o custo final e a lista de visitados
    return mst, custo, visitados


mst,custo,visitados = prim(grafo,'B')

print("Arvore geradora minima:")
print(mst)

for aresta in mst:
    peso, pai, no = aresta
    print(f"No visitado: {pai} | Proximo no: {no} | Peso: {peso}")

print (f"Custo total: {custo}")
print (visitados)




