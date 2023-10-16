#!/usr/bin/python3
"""Divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    output = []
    if not isinstance(div, int) and not isinstance(div, float):
        raise
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        for i in range(len(matrix)):
            if not isinstance(matrix[i], list):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            elif len(matrix[i]) != len(matrix[0]):
                raise TypeError("Each row of the matrix must have the same size")
            x = []
            for j in range(len(matrix[i])):
                if not isinstance(matrix[i][j], int) and not isinstance(matrix[i][j], float):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                else:
                    x.append(round(matrix[i][j] / div, 2))
            output.append(x)
        return output
