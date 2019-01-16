import csv

with open('bid.csv', mode='r', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=';')
    for linha in spamreader:
        print(linha)
