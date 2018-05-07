N = int(input())
while N > 0:
    texto = input().lower().replace(' ', '')
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    contador = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    result = ''
    a, i, count, maior = 0, 0, 0, 0
    break_ = True
    while count < 52:
        if break_ == True:
            contador[i] = texto.count(alfabeto[i])
            if contador[i] > maior:
                maior = contador[i]
            i += 1
            if i == 26:
                break_ = False
        else:
            if maior == texto.count(alfabeto[a]):
                result += alfabeto[a]
            a += 1
        count += 1
    print(result)
    N -= 1
