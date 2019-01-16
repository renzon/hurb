def dividir(x, denominador):
    if denominador == 0:
        return 'Não pode dividir'
    return x / denominador


print(dividir(3, 2))
print(dividir(4, 0))
print(dividir(denominador=9, x=4))
print('Acabou o programa')
