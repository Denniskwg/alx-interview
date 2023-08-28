#!/usr/bin/python3
"""0-making_change
"""


def makeChange(coins, total, idx=0, num=0):
    """Given a pile of coins of different values
    determine the fewest number of coins needed
    to meet a given amount total
    """
    if total <= 0:
        return 0
    if len(coins) == 0:
        return -1
    lst = sorted(coins, reverse=True)

    if idx == len(lst) and (total - lst[-1]) < 0:
        return -1 * (num + 1)
    if total < lst[-1]:
        return -1
    largest = lst[idx]
    remainder = total - (largest * int(total / largest))
    new_num = num + int(total / largest)
    steps = int(total / largest) + makeChange(lst, remainder, idx + 1, new_num)
    return steps
