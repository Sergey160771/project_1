# ✔ Напишите функцию для транспонирования матрицы

matrix = ([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[j][i] = matrix[i][j]
    return matrix


print(transpose_matrix(matrix))
