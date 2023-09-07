#!/usr/bin/python3
"""0-prime_game
"""


def isWinner(x, nums):
    """determines the winner between two players playing
    by finding a prime number inside a list and removing
    the prime number and its multiples. nums is a list of
    numbers of maximum range for a list
    """
    if x < 1 or not nums:
        return None
    turn = 1
    dict_players = {'Ben': 0, 'Maria': 0}
    for i in nums:
        arr = [j for j in range(1, i + 1)]
        length = len(arr)
        player = ''
        while length > 1:
            for k in range(len(arr)):
                if is_prime(arr[k]):
                    if turn % 2 == 0:
                        player = 'Ben'
                    else:
                        player = 'Maria'
                    element = arr[k]
                    arr.pop(k)
                    length = length - 1
                    indexes = []
                    for num in range(len(arr)):
                        if arr[num] % element == 0:
                            indexes.append(num)
                            length = length - 1
                    for num in indexes:
                        arr.pop(num)
                    turn = turn + 1
                    break
        if player == 'Ben' or player == '':
            dict_players['Ben'] = dict_players['Ben'] + 1
        if player == 'Maria':
            dict_players['Maria'] = dict_players['Maria'] + 1
    if dict_players['Maria'] > dict_players['Ben']:
        return 'Maria'
    elif dict_players['Ben'] > dict_players['Maria']:
        return 'Ben'
    else:
        return None


def is_prime(number):
    """retuns True if number is prime else returns
    False
    """
    if number <= 1:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
