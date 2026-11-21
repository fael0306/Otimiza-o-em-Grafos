def Kosaraju(n, arestas):
    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]
    for u, v in arestas:
        adj[u].append(v)
        radj[v].append(u)

    marcado = [False] * n
    ot = [0] * n
    os = n

    def OT(u, v):
        nonlocal os
        marcado[v] = True
        for w in adj[v]:
            if not marcado[w]:
                OT(v, w)
        os -= 1
        ot[os] = v

    for i in range(n):
        if not marcado[i]:
            OT(i, i)

    comp = 0

    def BPT(u, v):
        marcado[v] = False
        print(v, end=' ')
        for w in radj[v]:
            if marcado[w]:
                BPT(v, w)

    for i in range(n):
        if marcado[ot[i]]:
            comp += 1
            print(f'\nComponente {comp}:', end=' ')
            BPT(ot[i], ot[i])


n = 6
arestas = [
    (0, 1),
    (0, 2),
    (1, 4),
    (2, 4),
    (3, 1),
    (4, 3),
    (4, 5),
]

Kosaraju(n, arestas)