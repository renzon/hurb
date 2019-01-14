import string

letras = string.ascii_lowercase
numeros = range(1,20, 2)

for i, n in enumerate(numeros):
    print(letras[i],n, sep=' - ')

