linguas = {
    'pt-br': 'Portugues Brasileiro',
    'en-us': 'Inglês Americano'
}

print(linguas['pt-br'])
print(linguas['en-us'])
if 'es' in linguas:
    print(linguas['es'])

print(linguas.get('es', 'Lingua não disponível'))
linguas['es'] = 'Espanhol'
print(linguas.get('es', 'Lingua não disponível'))
print(linguas.get('pt-br', 'Lingua não disponível'))

sku_dicionario={
    'omn-2255': ['989354', '7565'],
    'omn-2256': ['989355', '7566'],
}

lista_ids = sku_dicionario['omn-2255']
print(lista_ids[1])
