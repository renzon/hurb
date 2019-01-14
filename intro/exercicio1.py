from itertools import cycle
from string import ascii_lowercase as minusculas

numeros = range(1, 30)
letras_ciclo = cycle(minusculas)

for letra, numero in zip(letras_ciclo, numeros):
    print(letra, numero, sep=' - ')
