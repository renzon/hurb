import requests

print('Começando Download')
resp = requests.get('https://s3.amazonaws.com/xml-parceiros-hu/prod/inventory_package_pt.json')
print('Terminado Download')
print(resp.status_code)
