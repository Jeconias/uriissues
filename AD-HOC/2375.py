N = int(input())
A, L, P = map(int, input().split(' '))

if (N > A or N > L or N > P):
    print('N')
else:
    print('S')
