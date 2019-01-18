import csv


def processar_novo_bid():
    """
    Processe arquivo de realizção de bid e gera arquivo de saída com novo cpc para cada hotel
    :return:
    """
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
                qtd_pedidos = linha_dct['SumQtdPedidos']
                soma_faturamento = linha_dct[' SumFaturamentoTopline ']
                custo = linha_dct['Custo']
                novo_cpc = calcular_novo_cpc_para_roi_negativo(roi, cpc, qtd_pedidos,soma_faturamento, custo)
                hoteis_com_roi_negativo.append((roi, hotel, cpc, novo_cpc, sku))
        hoteis_com_roi_negativo.sort()
        with open('saida.csv', 'w', newline='') as saida_csv:
            spamwriter = csv.DictWriter(saida_csv, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for hotel in hoteis_com_roi_negativo:
                linha = hotel[-2:]
                spamwriter.writerow(linha)


def calcular_novo_cpc_para_roi_negativo(roi, cpc_parametro, qtd_pedidos,soma_faturamento, custo):
    return round(cpc_parametro * 0.8)


processar_novo_bid()
