#!/usr/bin/python3
"""0-island_perimeter
"""


def island_perimeter(grid):
    """that returns the perimeter of the island
    described in grid
    grid is a list of list of integers:
    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically
    """
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            num = 0
            if grid[i][j] == 1:
                if grid[i - 1][j] == 0 and i > 0:
                    num = num + 1
                if grid[i][j - 1] == 0 and j > 0:
                    num = num + 1
                if j < (len(grid[i]) - 1) and grid[i][j + 1] == 0:
                    num = num + 1
                if i < (len(grid) - 1) and grid[i + 1][j] == 0:
                    num = num + 1
                total = total + num

    return total
