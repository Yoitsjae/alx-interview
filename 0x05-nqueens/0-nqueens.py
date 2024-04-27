#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens_util(board, row, N, result):
    # Base case: If all queens are placed, add the solution to the result
    if row == N:
        result.append([i[:] for i in board])  # Deep copy the board and add to result
        return

    # Consider this row and try placing this queen in all columns one by one
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1  # Place the queen
            solve_nqueens_util(board, row + 1, N, result)
            # Backtrack: Undo the queen placement
            board[row][col] = 0

def solve_nqueens(N):
    # Check if N is a valid integer
    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]  # Initialize an empty board
    result = []  # List to store solutions
    solve_nqueens_util(board, 0, N, result)  # Solve N queens problem recursively

    # Print all solutions
    for res in result:
        print(res)

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    # Solve N queens problem
    solve_nqueens(sys.argv[1])
