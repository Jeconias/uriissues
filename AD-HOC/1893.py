A, B = map(int, input().split(' '))

if(A > B):
    if(B >= 0 and B < 3):
        print('nova')
    elif(B >= 3 and B < 97):
        print('minguante')
    elif(B >= 97 and B < 101):
        print('cheia')
else:
    if(B >= 0 and B < 3):
        print('nova')
    elif(B >= 3 and B < 97):
        print('crescente')
    elif(B >= 97 and B < 101):
        print('cheia')
