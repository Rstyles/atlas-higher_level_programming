#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    output = []
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix[i])):
            temp.append(matrix[i][j] ** 2)
        output.append(temp)
    return output
