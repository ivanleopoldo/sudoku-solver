import random

# global vars
N = 5


def display_board(board):
    print("   ", " ".join(map(str, [n for n in range(N)])))
    print("   ", " ".join(map(str, ["-" for _ in range(N)])))
    for idx, row in enumerate(board):
        print(f"{idx} |", " ".join(map(str, row)))


def valid(board, cell, guess):
    return (False if guess in board[cell[0]] else True) and all(
        board[i][cell[1]] != guess for i in range(N)
    )


def solve(board, cell):
    # check if function reached end of board
    if cell[0] == N - 1 and cell[1] == N:
        return True

    # check if column cell coords reached end of row
    # then move to next row
    if cell[1] == N:
        cell[0], cell[1] = cell[0] + 1, 0

    # check if specific cell already contains value
    # move to the next column
    if board[cell[0]][cell[1]] > 0:
        return solve(board, [cell[0], cell[1] + 1])

    # inputs guesses
    for num in range(1, N + 1):
        # if guess is valid change cell value to guess
        if valid(board, cell, num):
            board[cell[0]][cell[1]] = num

            # guess next column
            if solve(board, [cell[0], cell[1] + 1]):
                return True

        # if guess not valid change value to 0
        board[cell[0]][cell[1]] = 0

    return False


def main():
    # initialize
    numbers = random.sample(range(1, N + 1), N)
    board = [[0] * N for _ in range(N)]
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
    print("\n")
    if solve(board, [0, 0]):
        display_board(board)
    else:
        print("no solution")


if __name__ == "__main__":
    main()
