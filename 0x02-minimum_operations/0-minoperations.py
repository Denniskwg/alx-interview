#!/usr/bin/python3
"""0-minoperations defines a function minOperations
that takes one integer argument
"""


def minOperations(n):
    """calculates the fewest number of operations
    needed to result in exactly n H characters in a file
    the available operations are copy all and paste
    """
    if n == 0:
        return 0

    elif n % 6 == 0:
        return 5 + minOperations(n / 6)
    elif n % 3 == 0:
        return 3 + minOperations(n / 3)
    elif n % 2 == 0:
        return 2 + minOperations(n / 2)
    else:
        return 0
