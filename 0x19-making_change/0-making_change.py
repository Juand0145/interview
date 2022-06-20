#!/usr/bin/python3
"""File that contains the function"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number of
    coins needed to meet a given amount total
    Args:
      coins is a list of the values of the coins in your possession
      total: the total value to achive
    Return: fewest number of coins needed to meet total
      If total is 0 or less, return 0
      If total cannot be met by any number of coins you have, return -1
    """
    if total <= 0:
        return 0
    if len(coins) is 0:
        return -1

    coins = sorted(coins)
    dynamic = [total + 1] * (total + 1)
    dynamic[0] = 0

    for i in range(total + 1):
        for coin in coins:
            if coin > i:
                break
            if dynamic[i - coin] != -1:
                dynamic[i] = min(dynamic[i - coin] + 1, dynamic[i])

    if dynamic[total] == float(total + 1):
        return -1
    return dynamic[total]
