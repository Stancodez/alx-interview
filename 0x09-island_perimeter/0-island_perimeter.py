#!/usr/bin/python3
"""
This module contains a function that calculates
the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    Args:
        grid (list of list of int): A 2D grid where 0 represents water
        and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Each land cell has an initial perimeter of 4
                perimeter += 4

                # Check for adjacent land cells to subtract the common sides
                if i > 0 and grid[i - 1][j] == 1:  # Up
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Left
                    perimeter -= 2

    return perimeter

