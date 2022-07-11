#!/usr/bin/python3
'''File that contains the function island_perimeter'''


def island_perimeter(grid):
    '''
    Function that returns the perimeter of the island
    described in grid
    Args:
        grid is a list of list of integers:
        0 represents water
        1 represents land
        Each cell is square, with a side length of 1
        Cells are connected horizontally/vertically (not diagonally).
        grid is rectangular, with its width and height not exceeding 100
    '''

    perimeter = 0
    length = len(grid) - 1
    width = len(grid[0]) - 1

    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i == length or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j == width or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
