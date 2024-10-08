#!/usr/bin/python3
"""
Module for rotating a 2D matrix 90 degrees clockwise in place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): The n x n matrix to rotate.

    Returns:
        None: The function modifies the matrix in place.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            # Swap matrix[i][j] with matrix[j][i]
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to complete the rotation
    for i in range(n):
        matrix[i].reverse()

