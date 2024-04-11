#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of al integers of a matrix

    Args:
        matrix: A two dimensional array

    Returns: A new matrix, same size as matrix"""
    squares = []
    for x in range(len(matrix)):
        col = []
        for y in range(len(matrix[x])):
            col.append(matrix[x][y]**2)
        squares.append(col)
    return (squares)
