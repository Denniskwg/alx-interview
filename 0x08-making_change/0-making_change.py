#!/usr/bin/python3
"""0-making_change
"""


def makeChange(coins, total, idx=0):
    """Given a pile of coins of different values
    determine the fewest number of coins needed
    to meet a given amount total
    """
    if total <= 0:
        return 0
    if len(coins) == 0:
        return -1
    sorted_list = sorted(coins, reverse=True)

    if idx == len(sorted_list) and (total - sorted_list[idx - 1]) < 0:
        return -1 * (idx + 1)
    if total < sorted_list[len(sorted_list) - 1]:
        return -1
    largest = sorted_list[idx]
    remainder = total - (largest * int(total / largest))
    steps = int(total / largest) + makeChange(sorted_list, remainder, idx + 1)
    return steps
