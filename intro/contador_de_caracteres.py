'''
>>> contar_palavras(linha)
{'renzo': 1}
>>> contar_palavras('renzo renzo')
{'renzo': 2}
>>> contar_palavras('renzo renzo nuccitelli')
{'renzo': 2, 'nuccitelli': 1}
>>> contar_palavras('renzo renzo nuccitelli santos')
{'renzo': 2, 'nuccitelli': 1, 'santos': 1}
>>> contar_palavras('renzo renzo nuccitelli santos santos')
{'renzo': 2, 'nuccitelli': 1, 'santos': 2}
'''


def contar_palavras(texto):
    frequencias = {}
    palavras = texto.split()
    for word in palavras:
        frequencias[word] = frequencias.get(word, 0) + 1

    return frequencias
