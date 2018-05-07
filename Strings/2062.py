Qtd = int(input())
palavras = list(map(str, input().upper().split()))
for i in range(Qtd):
    if len(palavras[i]) < 4:
        if palavras[i][0] == 'U' and palavras[i][1] == 'R':
            print('URI', end=' ') if i != (Qtd - 1) else print('URI')
        elif palavras[i][0] == 'O' and palavras[i][1] == 'B':
            print('OBI', end=' ') if i != (Qtd - 1) else print('OBI')
        else:
            print(palavras[i], end=' ') if i != (Qtd - 1) else print(palavras[i])
    else:
        print(palavras[i], end=' ') if i != (Qtd - 1) else print(palavras[i])
