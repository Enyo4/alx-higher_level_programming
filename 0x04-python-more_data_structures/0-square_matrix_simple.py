def square_matrix_simple(matrix=[]):
    """ computes the square value of all integers of a matrix."""
    new_matrix = []
    for col in matrix:
        element = []
        for i in range(len(col)):
            element.append(col[i] ** 2)
        new_matrix.append(element)
    return new_matrix