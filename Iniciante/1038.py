codigo, qtd = map(int, input().split(' '))
if codigo == 1:
    print('Total: R$ {:.2f}'.format(qtd * 4))
elif codigo == 2:
    print('Total: R$ {:.2f}'.format(qtd * 4.50))
elif codigo == 3:
    print('Total: R$ {:.2f}'.format(qtd * 5))
elif codigo == 4:
    print('Total: R$ {:.2f}'.format(qtd * 2))
elif codigo == 5:
    print('Total: R$ {:.2f}'.format(qtd * 1.50))
