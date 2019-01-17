import json

import xmltodict

with open('inventory_hotel_pt.json', 'r', encoding='utf-8') as entrada:
    hoteis = json.load(entrada)

    items = []
    resultado = {
        'items':
            {
                'item': items

            }
    }
    for hotel in hoteis:
        items.append(
            {
                'id': hotel.get('sku', '-'),
                'name': hotel.get('name', '--'),
                'url': hotel.get('search_url', '---')
            }
        )

with open('saida.xml', 'w', encoding='utf-8') as saida:
    xmltodict.unparse(resultado, saida, pretty=True)
