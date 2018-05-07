T = int(input())
Horas = T // 3600;
Minutos = (T % 3600) // 60;
Segundos = (T % 3600) % 60;
print('{}:{}:{}'.format(Horas, Minutos, Segundos))
