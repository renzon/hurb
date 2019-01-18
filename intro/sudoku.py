"""
>>> esta_correto(sudoku_certo)
True
>>> esta_correto(sudoku_errado_sub_jogo)
False
>>> esta_correto(sudoku_errado_linha)
False
>>> esta_correto(sudoku_errado_coluna)
False
"""
from itertools import product

sudoku_errado_coluna = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
]
sudoku_errado_linha = [
    [1, 2, 3, 4, 5, 6, 7, 8, 1],
    [9, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
]

sudoku_errado_sub_jogo = [
    [5, 1, 7, 6, 9, 8, 2, 3, 4],
    [2, 8, 9, 1, 3, 4, 7, 5, 6],
    [3, 4, 6, 2, 7, 5, 8, 9, 1],
    [6, 7, 2, 8, 4, 9, 3, 1, 5],
    [1, 3, 8, 5, 2, 6, 9, 4, 7],
    [4, 9, 5, 3, 6, 2, 1, 7, 8],
    [9, 5, 4, 7, 1, 3, 6, 8, 2],
    [7, 2, 3, 4, 8, 1, 5, 6, 9],
    [8, 6, 1, 9, 5, 7, 4, 2, 3]
]
sudoku_certo = [
    [5, 1, 7, 6, 9, 8, 2, 3, 4],
    [2, 8, 9, 1, 3, 4, 7, 5, 6],
    [3, 4, 6, 2, 7, 5, 8, 9, 1],
    [6, 7, 2, 8, 4, 9, 3, 1, 5],
    [1, 3, 8, 5, 2, 6, 9, 4, 7],
    [9, 5, 4, 7, 1, 3, 6, 8, 2],
    [4, 9, 5, 3, 6, 2, 1, 7, 8],
    [7, 2, 3, 4, 8, 1, 5, 6, 9],
    [8, 6, 1, 9, 5, 7, 4, 2, 3]
]


def validar_conjunto(lista):
    conjunto_certo = set(range(1, 10))
    return conjunto_certo == set(lista)


def validar_todas_linhas(jogo):
    for linha in jogo:
        if not validar_conjunto(linha):
            return False
    return True


def validar_todas_colunas(jogo):
    for coluna in zip(*jogo):
        if not validar_conjunto(coluna):
            return False
    return True


def validar_todas_subjogos(jogo):
    for i, j in product(range(0, 7, 3), range(0, 7, 3)):
        subjogo = set()
        for x, y in product(range(i, i + 3), range(j, j + 3)):
            subjogo.add(jogo[x][y])
        if not validar_conjunto(subjogo):
            return False
    return True


def esta_correto(jogo):
    """
    Função que retorna verdadeiro se for uma solução válida para sudoku_errado
    :param jogo: Matrix 9x9
    :return: booleano
    """

    return all([
        validar_todas_linhas(jogo),
        validar_todas_colunas(jogo),
        validar_todas_subjogos(jogo)
    ])
