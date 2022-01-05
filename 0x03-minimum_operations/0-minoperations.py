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

    operations = 0
    i = 2

    while(i <= n + 1):
        if (n % i == 0):
            operations += i
            n = n/i
        else:
            i += 1
    return operations
