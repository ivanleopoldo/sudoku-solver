# references
#       https://github.com/bgrohman/Brute-Force-Sudoku-Solver/blob/master/SudokuSolver.py


import random

# global vars
N = 5


def init_board():
    """initializes 5x5 board

    Returns:
        list: a 5x5 matrix with initial values "x"
    """
    return [["x" for _ in range(N)] for _ in range(N)]


def display_board(board):
    """displays 5x5 board

    Args:
        board list: 5x5 matrix
    """
    print("   ", " ".join(map(str, [n for n in range(N)])))
    print("   ", " ".join(map(str, ["-" for _ in range(N)])))
    for idx, row in enumerate(board):
        print(f"{idx} |", " ".join(map(str, row)))


def find_empty(board):
    """finds next empty cell in board

    Args:
        board list: 5x5 matrix

    Returns:
        tuple: cell coordinates
    """
    for i in range(N):
        for j in range(N):
            if board[i][j] == "x":
                return (i, j)


def valid_for_row(board, cell):
    return True


def valid_for_col(board, cell):
    return True


def valid(board, cell):
    return valid_for_row(board, cell) and valid_for_col(board, cell)


def main():
    numbers = [1, 2, 3, 4, 5]
    random.shuffle(numbers)
    board = init_board()
    display_board(board)

    user_list = []
    for i in range(N):
        cell = [
            int(x)
            for x in list(input(f"Enter number in (x,x) format {i+1}/{N}: ").split(","))
        ]
        user_list.append(cell)

    for i, j in zip(user_list, numbers):
        board[i[0]][i[1]] = j

    display_board(board)
    valid_for_row(board, [0, 1])


if __name__ == "__main__":
    main()
