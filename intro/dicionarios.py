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

sku_dicionario = {
    'omn-2255':
        {
            'sku': '989354',
            'estabelecimento': '7565'
        },
    'omn-2256':
        {
            'sku': '989355',
            'estabelecimento': '7566'
        },
}
ids_dicionario = sku_dicionario['omn-2255']


# Acesso id do sku com método get
print(ids_dicionario.get('sku'))
print(sku_dicionario.get('omn-2255').get('sku'))

# Acesso id do estabelecimento com colchetes
print(ids_dicionario['estabelecimento'])
print(sku_dicionario['omn-2255']['estabelecimento'])
