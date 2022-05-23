#!/usr/bin/python3
"""File that conatins the function rotate_2d_matrix"""


def rotate_2d_matrix(matrix):
    """
    Function that rotate a 2D matrix 90 degrees clockwise
    return:
        Do not return anything. The matrix must be edited in-place
    """
    N = len(matrix)

    matrix_copy = []
    copy_row = 0
    for column in range(N):
        for row in range((N - 1), -1, -1):
            if column is 0:
                matrix_copy.append([])
            matrix_copy[copy_row].append(matrix[row][column])
        copy_row += 1

    for row in range(N):
        for column in range(N):
            matrix[row][column] = matrix_copy[row][column]
