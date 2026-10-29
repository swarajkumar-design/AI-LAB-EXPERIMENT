
# Program to solve the 8-Queens Problem using Backtracking

N = 8

# Create an N x N chessboard
board = [["." for _ in range(N)] for _ in range(N)]


def is_safe(row, col):
    # Check the same column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < N:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


def solve_queens(row):
    if row == N:
        return True

    for col in range(N):
        if is_safe(row, col):
            board[row][col] = "Q"

            if solve_queens(row + 1):
                return True

            # Backtracking
            board[row][col] = "."

    return False


if solve_queens(0):
    print("Solution for 8-Queens Problem:")
    for row in board:
        print(" ".join(row))
else:
    print("No solution exists.")