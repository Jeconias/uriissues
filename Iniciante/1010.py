a1, a2, a3 = input().split(' ')
b1, b2, b3 = input().split(' ')

a1 = int(a1)
a2 = int(a2)
a3 = float(a3)
b1 = int(b1)
b2 = int(b2)
b3 = float(b3)

print('VALOR A PAGAR: R$ {:2.2f}'.format(a2 * a3 + b2 * b3))
