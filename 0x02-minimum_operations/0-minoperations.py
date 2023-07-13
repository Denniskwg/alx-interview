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

    operations = 0

    while n % 6 == 0:
        n /= 6
        operations += 5

    while n % 3 == 0:
        n /= 3
        operations += 3

    while n % 2 == 0:
        n /= 2
        operations += 2

    print(n)
    if n <= 1:
        return operations
    else:
        return 0
