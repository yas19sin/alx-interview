#!/usr/bin/python3
"""
Island Perimeter Module

This module contains a function to calculate the perimeter of an island
represented in a 2D grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a 2D grid.

    Args:
        grid (list of list of int): A 2D grid where 0 represents water
                                   and 1 represents land.

    Returns:
        int: The perimeter of the island.

    The function works by:
    1. Iterating through each cell in the grid
    2. For each land cell (1), checking its 4 adjacent sides
    3. Adding 1 to perimeter for each side that borders water or grid edge
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Found a land cell
                # Check all 4 sides of the current land cell
                # Top side
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Bottom side
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Left side
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Right side
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
