N = int(input())
pokemons = []
while (N != 0):
  Name = input()
  pokemons.append(Name)
  N-= 1
print('Falta(m) {} pomekon(s).'.format(151 - len(set(pokemons))))
