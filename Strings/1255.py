N = int(input())
while N > 0:
    texto = input().lower().replace(' ', '')
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    contador = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    result = ''
    maior = 0

    for i in range(26):
        contador[i] = texto.count(alfabeto[i])
        if contador[i] > maior:
            maior = contador[i]
    for a in range(26):
        if maior == texto.count(alfabeto[a]):
            result += alfabeto[a]
    print(result)
    N -= 1
