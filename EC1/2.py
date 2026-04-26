def ciclo_euleriano(grafo, inicio):
    pilha = []
    pilha.append(inicio)

    while len(pilha) > 0:
        v = pilha[-1]

        if len(grafo[v]) > 0:
            u = grafo[v].pop()
            grafo[u].remove(v)
            pilha.append(u)
        else:
            atual = pilha.pop()
            print(atual)

grafo = {0: [1, 2], 1: [0, 2], 2: [1, 0]}
ciclo_euleriano(grafo, 0)
