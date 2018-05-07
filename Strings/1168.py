N = int(input())
while N > 0:
    value = input()
    leds = 0
    for i in range(len(value)):
        if value[i] == '2' or value[i] == '5' or value[i] == '3':
            leds += 5
        elif value[i] == '1':
            leds += 2
        elif value[i] == '6' or value[i] == '9' or value[i] == '0':
            leds += 6
        elif value[i] == '8':
            leds += 7
        elif value[i] == '4':
            leds += 4
        elif value[i] == '7':
            leds += 3
    N -= 1
    print('{} leds'.format(leds))
