def seqBin(seq, alternancia, size):
    binario = ''
    for i in range(size):
        if(seq[i] == 'X'):
            binario += '0'
        else:
            binario += '1'
    binario = binario[::-1]
    return int(binario, 2) + int(alternancia)

def decimalBin(soma, qntSeq):
    binario = ''
    while (True):
        binario += str(soma % 2)
        soma //= 2
        if len(binario) == qntSeq:
            break
    return binario[::-1]

def binXO(binary):
    XO = ''
    T = len(binary)
    for i in range(T):
        if(binary[i] == '0'):
            XO += 'X'
        else:
            XO += 'O'
    return XO[::-1]

N = int(input())
while N != 0:
    N -= 1
    seq, alternancia = input().split()
    seq = list(seq)
    qntSeq = len(seq)
    print(binXO(decimalBin(seqBin(seq, alternancia, qntSeq), qntSeq)))
