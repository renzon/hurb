import csv

with open('bid.csv',mode='r', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        print(row)
