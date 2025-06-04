#!/usr/bin/python3
"""
Module for rotating a 2D matrix 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list): A 2D list representing an n x n matrix.
                      The matrix is modified in-place.

    Returns:
        None: The function modifies the matrix in-place.

    Example:
        >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> rotate_2d_matrix(matrix)
        >>> print(matrix)
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    """
    n = len(matrix)

    # Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to complete the 90-degree clockwise rotation
    for i in range(n):
        matrix[i].reverse()
