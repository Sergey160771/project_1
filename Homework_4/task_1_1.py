import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    result = matrix.T
    return result


print(transpose_matrix(matrix))
