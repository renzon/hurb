lista = range(20)

nova_lista = []

for n in lista:
    if n % 2 == 1:
        nova_lista.append(n ** 2)


def transformar(i):
    return i ** 2


nova_lista = [transformar(i) for i in lista if i % 2 == 1]
print(nova_lista)
