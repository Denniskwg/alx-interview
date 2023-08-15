#!/usr/bin/python3
"""0-rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    """rotates a 2d matrix 90 degrees clockwise
    """
    matrix2 = matrix[:]
    k = 0
    for _ in range(len(matrix2) - 1, -1, -1):
        arr = []
        for j in range(len(matrix2) - 1, -1, -1):
            arr.append(matrix2[j][k])
        matrix.insert(k, arr)
        matrix.pop()
        k = k + 1
