P1,C1,P2, C2 = map(int, input().split(' '))
esquerda = int(P1 * C1)
direita = int(P2 * C2)
if (esquerda == direita):
    print(0)
elif (esquerda > direita):
    print(-1)
else:
    print(1)
