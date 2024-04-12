#!/usr/bin/python3

"""Defines a matrix function."""


def matrix_divided(matrix, div):
    """Divide all elements in the  matrix.
    Arguments:
        matrix: A list of lists of ints or floats.
        divide (int/float): The divisor.
    Raises:
        TypeError: If matrix not list or empty list.
        TypeError: If matrix not the same size.
        TypeError: If div not an integer or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix with div.
    """
    if (matrix == [] or not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
