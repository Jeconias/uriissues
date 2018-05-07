N = int(input())
while N > 0:
    posicao_robo = 0
    comandos = []
    numero_instrucoes = int(input())
    for i in range(numero_instrucoes):
        comando = input()
        if comando == 'LEFT':
            posicao_robo -= 1
            comandos.append(comando)
        elif comando == 'RIGHT':
            posicao_robo += 1
            comandos.append(comando)
        else:
            same_as = comando.split()
            if comandos[int(same_as[2]) - 1] == 'LEFT':
                posicao_robo -= 1
                comandos.append('LEFT')
            elif comandos[int(same_as[2]) - 1] == 'RIGHT':
                posicao_robo += 1
                comandos.append('RIGHT')
    print(posicao_robo)
    N -= 1
