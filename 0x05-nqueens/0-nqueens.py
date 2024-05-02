#!/usr/bin/python3
""" N QUEENS ALGORITHM WITH BACKTRACKING (RECURSION INSIDE LOOP) """
import sys


class NQueenSolver:
    """ Class for solving the N Queens problem """

    def __init__(self, n):
        """ Initialize the NQueenSolver class """
        self.board_size = n
        self.columns = [0] * (n + 1)
        self.solutions = []

    def can_place_queen(self, row, column):
        """ Check if a queen can be placed at the specified position """
        for prev_row in range(1, row):
            prev_col = self.columns[prev_row]
            if prev_col == column or abs(prev_col - column) == abs(prev_row - row):
                return False
        return True

    def solve_n_queens(self, row):
        """ Recursively solve the N Queens problem """
        for col in range(1, self.board_size + 1):
            if self.can_place_queen(row, col):
                self.columns[row] = col
                if row == self.board_size:
                    self.add_solution()
                else:
                    self.solve_n_queens(row + 1)

    def add_solution(self):
        """ Add the current solution to the list of solutions """
        solution = [(row - 1, self.columns[row] - 1) for row in range(1, self.board_size + 1)]
        self.solutions.append(solution)

    def get_solutions(self):
        """ Return the list of solutions """
        return self.solutions


if __name__ == "__main__":
    # Validate command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens.py N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
        if board_size < 4:
            raise ValueError("N must be at least 4")
    except ValueError as e:
        print("Invalid input:", e)
        sys.exit(1)

    # Solve the N Queens problem
    solver = NQueenSolver(board_size)
    solver.solve_n_queens(1)
    solutions = solver.get_solutions()

    # Print solutions
    for solution in solutions:
        print(solution)
