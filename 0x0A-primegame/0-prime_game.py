#!/usr/bin/python3
"""0-prime_game
"""


def isWinner(x, nums):
    """determines the winner between two players playing
    by finding a prime number inside a list and removing
    the prime number and its multiples. nums is a list of
    numbers of maximum range for a list
    """
    Maria = 0
    Ben = 0
    player = 1
    dict_players = {'Ben': 0, 'Maria': 0}
    for i in nums:
        arr = [j for j in range(1, i + 1)]
        length = len(arr)
        while length > 1:
            for k in range(len(arr)):
                if is_prime(arr[k]):
                    if player % 2 == 0:
                        Ben = Ben + 1
                    else:
                        Maria = Maria + 1
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
                    player = player + 1
                    break
        if Maria > Ben:
            dict_players['Maria'] = dict_players['Maria'] + 1
        else:
            dict_players['Ben'] = dict_players['Ben'] + 1
        Maria = 0
        Ben = 0

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
