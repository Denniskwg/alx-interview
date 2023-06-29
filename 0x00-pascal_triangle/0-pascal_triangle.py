#!/usr/bin/python3
"""0-pascal_triangle

This module defines a method pascal_triangle
that returns a list of lists representing the Pascal’s
triangle
"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n
    n: number of lists to return
    """
    if n <= 0:
        return []
    arr = [[1]]
    for i in range(n - 1):
        arr2 = [1]
        for j in range(len(arr[i])):
            if j == (len(arr[i]) - 1):
                break
            else:
                value = arr[i][j] + arr[i][j+1]
                arr2.append(value)
        arr2.append(1)
        arr.append(arr2)
    return arr
