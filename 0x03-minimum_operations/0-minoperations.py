#!/usr/bin/python3
"""File that contains the function minOperations"""


def minOperations(n):
    """
    function that calculates the minimun operations
    Args:
    n: number of character to acomplish
    return 0 the minimun operation or None
    """
    if type(n) is not int or n < 2:
        return 0

    min_iterations = n

    for i in range(int(n/2))[2:]:
        if n % i == 0:
            second = int(n/i)
            iterations = second + i

            if iterations < min_iterations:
                min_iterations = iterations

    return min_iterations
