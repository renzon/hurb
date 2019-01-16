import csv
from builtins import round

with open('bid.csv', mode='r', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=';')
    hoteis_com_roi_negativo = []
    for linha_dct in spamreader:
        roi_rec = 'ROI Rec'
        hotel_name = 'Hotel Name'
        hotel = linha_dct[hotel_name]
        roi = linha_dct[roi_rec]
        roi = roi.replace(',', '.')
        if 'R$ -' in roi:
            roi = .0
        else:
            roi = float(roi)
        if 0 < roi < 1:
            cpc = int(linha_dct['Bid 09/01'])
            sku = linha_dct['PartnerRef']
            hoteis_com_roi_negativo.append((roi, hotel, cpc, round(cpc * 0.8), sku))
    hoteis_com_roi_negativo.sort()
    with open('saida.csv', 'w', newline='') as saida_csv:
        spamwriter = csv.writer(saida_csv, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for hotel in hoteis_com_roi_negativo:
            linha = hotel[-2:]
            spamwriter.writerow(linha)
