import string

letras = string.ascii_lowercase
numeros = range(1, 30)

for i, n in enumerate(numeros):
    i = i % len(letras)
    print(letras[i], n, sep=' - ')
