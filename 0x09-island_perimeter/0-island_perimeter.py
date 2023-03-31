#!/usr/bin/python3
"""
0-main
"""
from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    """
    Returns the perimeter of the island described in grid

    Args:
        grid: a list of list of integers where 0 represents water and 1 represents land

    Returns:
        The perimeter of the island
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4
                if row > 0 and grid[row-1][col] == 1:
                    perimeter -= 2
                if col > 0 and grid[row][col-1] == 1:
                    perimeter -= 2
    return perimeter