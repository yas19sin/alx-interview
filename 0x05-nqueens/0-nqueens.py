#!/usr/bin/python3
"""
N Queens Problem Solver
Solves the N queens puzzle using backtracking algorithm
"""
import sys


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed at board[row][col]
    """
    # Check this column on upper rows
    for i in range(row):
        if board[i] == col:
            return False
    
    # Check upper diagonal on left side
    for i in range(row):
        if board[i] == col - (row - i):
            return False
    
    # Check upper diagonal on right side
    for i in range(row):
        if board[i] == col + (row - i):
            return False
    
    return True


def solve_nqueens(n):
    """
    Solve N Queens problem using backtracking
    Returns list of all possible solutions
    """
    solutions = []
    board = [-1] * n
    
    def backtrack(row):
        if row == n:
            # Found a solution, convert to required format
            solution = [[i, board[i]] for i in range(n)]
            solutions.append(solution)
            return
        
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1
    
    backtrack(0)
    return solutions


def main():
    # Check number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    # Check if N is a number
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    # Solve N Queens problem
    solutions = solve_nqueens(n)
    
    # Print all solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
