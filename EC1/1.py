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

def faz():
    linha = input().split()
    n = int(linha[0])
    m = int(linha[1])
    inicia(n)
    for _ in range(m):
        u, v = map(int, input().split())
        uniao(u, v)
    componente = 0
    for i in range(1, n + 1):
        if pai[i] == i:
            componente = componente + 1
            print("Componente", componente, ":", end=' ')
            for j in range(1, n + 1):
                if busca(j) == i:
                    print(j, end=' ')
            print()

faz()
