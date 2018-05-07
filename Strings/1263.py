while True:
    try:
        aliteracoes = 0
        N = list(input().lower().split())
        T = len(N)
        for i in range(1, T):
            if N[i - 1][0] == N[i][0] and N[i][0] != N[i-2][0]:
                aliteracoes += 1
        print(aliteracoes)
    except EOFError as e:
        break
