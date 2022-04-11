#!/usr/bin/python3
"""File that contains the function rain"""


def rain(walls):
    """
    Funtcion that calculate how many square units of water
    will be retained after it rains
    Args:
        walls is a list of non-negative integers.
    Return: Integer indicating total amount of rainwater retained.
    """
    if type(walls) is not list or walls is []:
        return 0
    for i in walls:
        if i < 0:
            return 0

    water = 0
    for index, height in enumerate(walls):
        left_max = max(walls[:index + 1])
        right_max = max(walls[index:])
        shorter_wall = min(left_max, right_max)
        water += max(shorter_wall - height, 0)

    return water
