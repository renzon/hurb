'''
>>> eh_palindromo('arara')
True
>>> eh_palindromo('roma me tem amor')
True
>>> eh_palindromo('ab')
False
'''


def eh_palindromo(palavra):
    palavra=palavra.replace(' ', '')
    palavra_revertida = palavra[::-1]
    return palavra == palavra_revertida
