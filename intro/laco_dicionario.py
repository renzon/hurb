linguas = {
    'pt-br': 'Portugues Brasileiro',
    'en-us': 'Inglês Americano'
}


# iteração pelas chaves
for chave in linguas:
    print(chave)

for chave in linguas.keys():
    print(chave, linguas[chave])

print(list(linguas.keys()))

# Iteraçao pelos valores
for valor in linguas.values():
    print(valor)

# Iteraçao pelos items
for chave, valor in linguas.items():
    print(chave, valor)