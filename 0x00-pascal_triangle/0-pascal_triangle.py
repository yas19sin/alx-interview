#!/usr/bin/python3
"""
Module for Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to n rows.

    Args:
        n (int): The number of rows of the triangle to generate.

    Returns:
        list: A list of lists of integers representing Pascal's triangle.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # Start with the first 1

        # Calculate the middle elements
        for j in range(len(prev_row) - 1):
            new_row.append(prev_row[j] + prev_row[j+1])

        new_row.append(1)  # End with the last 1
        triangle.append(new_row)

    return triangle
