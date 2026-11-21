def Floyd(n, E):
    D = [[0] * n for _ in range(n)]
    VCM = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if E[i][j] == 0 and i != j:
                D[i][j] = float('inf')
            else:
                D[i][j] = E[i][j]
            VCM[i][j] = i
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    VCM[i][i] = VCM[k][i]
    return D, VCM


n = 4
E = [
    [0, 3, 0, 7],
    [8, 0, 2, 0],
    [0, 5, 0, 1],
    [2, 0, 0, 0],
]

D, VCM = Floyd(n, E)
for linha in D:
    print(linha)