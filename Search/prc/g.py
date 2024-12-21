import pygame
import random

# Initialize Pygame
pygame.init()

# Define constants
GRID_SIZE = 3
TILE_SIZE = 100
WINDOW_SIZE = TILE_SIZE * GRID_SIZE
FONT_SIZE = 40

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the display
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Sliding Puzzle")

# Font for numbers
font = pygame.font.Font(None, FONT_SIZE)

def create_puzzle():
    """
    Create a solvable shuffled puzzle.
    """
    tiles = list(range(1, GRID_SIZE * GRID_SIZE)) + [0]  # Numbers 1-8 + empty space (0)
    while True:
        random.shuffle(tiles)
        if is_solvable(tiles) and not is_solved(tiles):
            break
    return [tiles[i:i + GRID_SIZE] for i in range(0, len(tiles), GRID_SIZE)]

def is_solvable(tiles):
    """
    Check if the puzzle is solvable.
    """
    inversion_count = 0
    flat_tiles = [t for t in tiles if t != 0]  # Exclude the empty tile
    for i in range(len(flat_tiles)):
        for j in range(i + 1, len(flat_tiles)):
            if flat_tiles[i] > flat_tiles[j]:
                inversion_count += 1
    return inversion_count % 2 == 0

def is_solved(puzzle):
    """
    Check if the puzzle is in a solved state.
    """
    target = list(range(1, GRID_SIZE * GRID_SIZE)) + [0]
    return sum(puzzle, []) == target

def draw_puzzle(puzzle):
    """
    Draw the puzzle on the screen.
    """
    screen.fill(BLACK)  # Clear the screen with black
    for i, row in enumerate(puzzle):
        for j, tile in enumerate(row):
            if tile != 0:  # Skip the empty tile
                rect = pygame.Rect(j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, WHITE, rect)  # Draw the tile
                pygame.draw.rect(screen, BLACK, rect, 2)  # Border
                # Draw the tile number
                text = font.render(str(tile), True, BLACK)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)

def find_empty_tile(puzzle):
    """
    Find the position of the empty tile (0).
    """
    for i, row in enumerate(puzzle):
        for j, tile in enumerate(row):
            if tile == 0:
                return i, j

def move_tile(puzzle, row, col):
    """
    Move a tile to the empty space if possible.
    """
    empty_row, empty_col = find_empty_tile(puzzle)
    if (abs(empty_row - row) == 1 and empty_col == col) or (abs(empty_col - col) == 1 and empty_row == row):
        puzzle[empty_row][empty_col], puzzle[row][col] = puzzle[row][col], puzzle[empty_row][empty_col]

def get_tile_at_pos(x, y):
    """
    Get the grid position based on mouse click coordinates.
    """
    row, col = y // TILE_SIZE, x // TILE_SIZE
    return row, col

def main():
    """
    Main game loop.
    """
    puzzle = create_puzzle()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row, col = get_tile_at_pos(x, y)
                move_tile(puzzle, row, col)

        # Draw the current state of the puzzle
        draw_puzzle(puzzle)
        pygame.display.flip()

        # Check if the puzzle is solved
        if is_solved(puzzle):
            print("Congratulations! You solved the puzzle.")
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()
