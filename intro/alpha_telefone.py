"""
>>> calcular_telefone('1-HOME-SWEET-HOME')
'1-4663-79338-4663'
>>> calcular_telefone('MY-MISERABLE-JOB')
'69-647372253-562'
>>> calcular_telefone('6Y-MISERABLE-JOB')
'69-647372253-562'
>>> calcular_telefone('69-MISERABLE-JOB')
'69-647372253-562'
>>> calcular_telefone('6Y-M4SERABLE-JOB')
'69-647372253-562'
>>> calcular_telefone('6Y-M47ERABLE-JOB')
'69-647372253-562'
>>> calcular_telefone('6Y-M473RABLE-JOB')
'69-647372253-562'
>>> calcular_telefone('6Y-M473R2BLE-JOB')
'69-647372253-562'
"""

# http://dojopuzzles.com/problemas/exibe/encontre-o-telefone/
dct = {
    'A': '2', 'B': '2', 'C': '2', 'D': '3', 'E': '3', 'F': '3', 'G': '4', 'H': '4', 'I': '4', 'J': '5', 'K': '5',
    'L': '5', 'M': '6', 'N': '6', 'O': '6', 'P': '7', 'Q': '7', 'R': '7', 'S': '7', 'T': '8', 'U': '8', 'V': '8',
    'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
}


def calcular_telefone(numero):
    resultado = ''
    for n in numero:
        resultado += dct.get(n, n)
    return resultado
