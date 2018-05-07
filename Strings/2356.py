while True:
    try:
        D = input()
        S = input()
        if len(D.split(S)) > 1:
            print('Resistente')
        else:
            print('Nao resistente')
    except EOFError as e:
        break
