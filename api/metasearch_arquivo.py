import json

with open('hotel_packages.json', 'r', encoding='utf-8') as arquivo:
    pacotes = json.load(arquivo)

print(len(pacotes))
print(pacotes[0].keys())
for pacote in pacotes:
    if 'Ibis' in pacote['name']:
        print(pacote)
    # break

print('Criando campo promo com desconto de 20%')

for pacote in pacotes:
    if 'price_before_discount' in pacote:
        desconto_porcentagem = round(pacote['price'] / pacote['price_before_discount'], ndigits=2)
    else:
        desconto_porcentagem = 0
    pacote['promo'] = f'{desconto_porcentagem:.2%}'
    print(pacote['name'], pacote['promo'], sep=':')
