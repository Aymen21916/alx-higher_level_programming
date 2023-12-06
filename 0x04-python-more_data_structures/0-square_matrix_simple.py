#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_square = []
    for i in range(len(matrix)):
        inner_list = []
        for j in range(len(matrix[i])):
            inner_list.append(matrix[i][j] * matrix[i][j])
        matrix_square.append(inner_list)
    return matrix_square
