while True:
    tautograma = True
    N = list(input().lower().split())
    if N[0] == '*':break
    T = len(N)
    for i in range(1, T):
        if N[i - 1][0] != N[i][0]:
            tautograma = False
    if tautograma == True:
        print('Y')
    else:
        print('N')
