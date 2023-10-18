# AI GENERATED CODE

import pygame
import random

pygame.font.init()

# Global variables
N = 5
WIDTH, HEIGHT = 500, 500
GRID_SIZE = WIDTH // N
font = pygame.font.Font(None, 36)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

# Initialize the Sudoku board with zeros
board = [[0 for _ in range(N)] for _ in range(N)]

# Variables to track the selected cells and filled values
selected_cells = []
filled_values = []

# Flag to indicate whether to visualize the solve function
visualize_solution = False


def valid(board, cell, guess):
    # list = []
    # for i in range(N)
    #     if guess != cell:
    #         list.append(True)
    #     list.append(False)

    # if False in list:
    #     return False
    # else:
    #     return True
    return (False if guess in board[cell[0]] else True) and all(
        board[i][cell[1]] != guess for i in range(N)
    )


# Function to draw the Sudoku board
def draw_board():
    for row in range(N):
        for col in range(N):
            cell_rect = pygame.draw.rect(
                screen,
                (255, 255, 255),
                (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE),
                2,
            )
            if (row, col) in selected_cells:
                pygame.draw.rect(
                    screen, (0, 255, 0), cell_rect, 0
                )  # Highlight selected cells
            if board[row][col] != 0:
                text_color = (0, 0, 0)
                text = font.render(str(board[row][col]), True, text_color)
                text_rect = text.get_rect()
                text_rect.center = (
                    col * GRID_SIZE + GRID_SIZE // 2,
                    row * GRID_SIZE + GRID_SIZE // 2,
                )
                screen.blit(text, text_rect)

    # Draw horizontal grid lines
    for row in range(N):
        pygame.draw.line(
            screen, (0, 0, 0), (0, row * GRID_SIZE), (WIDTH, row * GRID_SIZE), 2
        )

    # Draw vertical grid lines
    for col in range(N):
        pygame.draw.line(
            screen, (0, 0, 0), (col * GRID_SIZE, 0), (col * GRID_SIZE, HEIGHT), 2
        )


# Function to visualize the solve function
def visualize_solve(board, cell):
    if cell[0] == N - 1 and cell[1] == N:
        return True

    if cell[1] == N:
        cell[0], cell[1] = cell[0] + 1, 0

    if board[cell[0]][cell[1]] > 0:
        return visualize_solve(board, [cell[0], cell[1] + 1])

    for guess in range(1, N + 1):
        if valid(board, cell, guess):
            board[cell[0]][cell[1]] = guess
            draw_board()
            pygame.display.update()

            if visualize_solve(board, [cell[0], cell[1] + 1]):
                return True

            board[cell[0]][cell[1]] = 0
            draw_board()
            pygame.display.update()

    return False


# Main game loop
running = True
selected_count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if selected_count < 5:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // GRID_SIZE
                row = y // GRID_SIZE
                if 0 <= col < N and 0 <= row < N and (row, col) not in selected_cells:
                    selected_cells.append((row, col))
                    selected_count += 1
        if selected_count == 5 and not filled_values:
            filled_values = random.sample(range(1, N + 1), N)
            for i in range(5):
                row, col = selected_cells[i]
                board[row][col] = filled_values[i]
        if (
            selected_count == 5
            and event.type == pygame.KEYDOWN
            and event.key == pygame.K_SPACE
        ):
            visualize_solve(board, [0, 0])

    screen.fill((255, 255, 255))
    draw_board()
    pygame.display.update()

pygame.quit()
