#!/usr/bin/python3
"""
N Queens
"""
import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True


def solve_nqueens(board, col, n):
    """
    Solve the N Queen problem using Backtracking
    """
    # Base case: If all queens are placed
    if col >= n:
        print_solution(board, n)
        return True

    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # recur to place rest of the queens
            if solve_nqueens(board, col + 1, n):
                return True

            # If placing queen in board[i][col
            # doesn't lead to a solution, then
            # queen from board[i][col]
            board[i][col] = 0

    # if the queen can not be placed in any row in
    # this column col then return false
    return False


def print_solution(board, n):
    """
    A utility function to print the solution in a
    N x N board
    """
    queens = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                queens.append([i, j])
    print(queens)


def main():
    """
    Main function to handle input and output
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board to 0
    board = [[0] * n for _ in range(n)]

    if not solve_nqueens(board, 0, n):
        print("No solution found")


if __name__ == "__main__":
    main()
