#!/usr/bin/python3
"""0-making_change
"""


def makeChange(coins, total):
    """Given a pile of coins of different values
    determine the fewest number of coins needed
    to meet a given amount total
    """
    if total <= 0:
        return 0

    largest = coins[0]

    for num in coins:
        if num > largest:
            largest = num
    remainder = total - largest
    if remainder == 0:
        return 1
    steps = 0
    for i in range(len(coins)):
        if remainder % coins[i] == 0:
            j = int(remainder / coins[i])
            if steps == 0:
                steps = j
            if j < steps:
                steps = j
    if steps == 0:
        return -1
    return 1 + steps
