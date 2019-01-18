sudoku_errado = [
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
sudoku_certo = [
    [5, 1, 7, 6, 9, 8, 2, 3, 4],
    [2, 8, 9, 1, 3, 4, 7, 5, 6],
    [3, 4, 6, 2, 7, 5, 8, 9, 1],
    [6, 7, 2, 8, 4, 9, 3, 1, 5],
    [1, 3, 8, 5, 2, 6, 9, 4, 7],
    [9, 5, 4, 7, 1, 3, 6, 8, 2],
    [4, 9, 5, 3, 6, 2, 1, 7, 8],
    [7, 2, 3, 4, 8, 1, 5, 6, 9],
    [8, 6, 1, 9, 5, 7, 4, 2, 3]]

print(sudoku_errado[0][1])


def esta_correto(jogo):
    """
    Função que retorna verdadeiro se for uma solução válida para sudoku_errado
    :param jogo: Matrix 9x9
    :return: booleano
    """


print(esta_correto(sudoku_errado))
