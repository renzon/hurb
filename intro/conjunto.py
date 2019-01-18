conjunto = {'banana', 'caju', 'cereja'}
conjunto_2 = {'banana', 'morango', 'jaca'}

conjunto = set()
print(conjunto)
conjunto.add('banana')
print(conjunto)
print('banana' in conjunto)
print('maça' in conjunto)
print(conjunto.union(conjunto_2))
print(conjunto.intersection(conjunto_2))
print(conjunto.difference(conjunto_2))
