entrada = open('bid.csv', mode='r', encoding='Windows-1252')
saida = open('saida.csv', mode='w')

for linha in entrada:
    colunas = linha.split(';')
    nova_linha = f'{colunas[0]};{colunas[1]}'
    saida.write(nova_linha+'\n')

entrada.close()
saida.close()
