#!/usr/bin/env python3
import sys
"""0-nqueens
"""


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

n = sys.argv[1]
if not n.isdigit():
    print("N must be a number")
    exit(1)

n = int(n)
if n < 4:
    print("N must be at least 4")
    exit(1)


def is_safe(board, row, col, N):
    """checks if there is a queen in same column,
    vertically or diagonally
    """
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, row, N, lst):
    """moves through the board and adds a quuen and
    backtracks if solution is not found
    """
    if row == N:
        for i in range(len(board) - 1, -1, -1):
            for j in range(len(board[i])):
                if board[i][j] == 1:
                    lst.append([j, i])
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_n_queens(board, row + 1, N, lst)
            board[row][col] = 0


def n_queens_solver(N):
    """main function crates the board and calls other
    functions
    """
    lst = []
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_n_queens(board, 0, N, lst)
    lst2 = []
    for i in range(len(lst)):
        if i % n == 0 and i > 0:
            print(lst2)
            lst2 = [lst[i]]
        else:
            lst2.append(lst[i])
    print(lst2)


n_queens_solver(n)
