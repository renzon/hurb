entrada = open('bid.csv', mode='r', encoding='utf-8')
saida = open('saida.csv', mode='w')

for linha in entrada:
    linha=linha.replace('|', ';')

    saida.write(linha)

entrada.close()
saida.close()
