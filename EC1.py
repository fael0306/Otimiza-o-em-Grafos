pai = []

def inicia(n):
    global pai
    pai = list(range(n + 1))

def busca(x):
    while pai[x] != x:
        pai[x] = pai[pai[x]]
        x = pai[x]
    return x

def uniao(a, b):
    ra = busca(a)
    rb = busca(b)
    if ra != rb:
        pai[ra] = rb

def componentes():
    entrada = input().split()
    n = int(entrada[0])
    m = int(entrada[1])
    inicia(n)
    for _ in range(m):
        u, v = map(int, input().split())
        uniao(u, v)
    comp = 0
    for i in range(1, n + 1):
        if pai[i] == i:
            comp = comp + 1
            print("Componente", comp, ":", end=' ')
            for j in range(1, n + 1):
                if busca(j) == i:
                    print(j, end=' ')
            print()

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
