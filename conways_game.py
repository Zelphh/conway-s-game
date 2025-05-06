import numpy as np
import pygame
import time

# Colors
BACKGROUND_COLOR = (10, 10, 10)
GRID_LINE_COLOR = (50, 50, 50)
DYING_COLOR = (0, 75, 0)
ALIVE_COLOR = (0, 220, 0)


def update_generation(screen, current_grid, cell_size, is_running=False):
    next_grid = np.zeros((current_grid.shape[0], current_grid.shape[1]))

    for row, col in np.ndindex(current_grid.shape):
        alive_neighbors = np.sum(current_grid[row-1:row+2, col-1:col+2]) - current_grid[row, col]
        color = BACKGROUND_COLOR if current_grid[row, col] == 0 else ALIVE_COLOR

        if current_grid[row, col] == 1:
            if alive_neighbors < 2 or alive_neighbors > 3:
                if is_running:
                    color = DYING_COLOR
            else:
                next_grid[row, col] = 1
                if is_running:
                    color = ALIVE_COLOR
        else:
            if alive_neighbors == 3:
                next_grid[row, col] = 1
                if is_running:
                    color = ALIVE_COLOR

        pygame.draw.rect(screen, color, (col * cell_size, row *
                         cell_size, cell_size - 1, cell_size - 1))

    return next_grid


def main():
    pygame.init()

    pygame.display.set_caption("Conway's game of life")
    icon = pygame.image.load("icon.png")
    pygame.display.set_icon(icon)

    screen = pygame.display.set_mode((800, 600))

    grid = np.zeros((60, 80))
    cell_size = 10

    screen.fill(GRID_LINE_COLOR)
    update_generation(screen, grid, cell_size)

    pygame.display.flip()

    is_running = False

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_running = not is_running
                    update_generation(screen, grid, cell_size)
                    pygame.display.update()

            if pygame.mouse.get_pressed()[0]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                row = mouse_y // cell_size
                col = mouse_x // cell_size

                grid[row, col] = 1 if grid[row, col] == 0 else 0

                update_generation(screen, grid, cell_size)
                pygame.display.update()

        screen.fill(GRID_LINE_COLOR)

        if is_running:
            grid = update_generation(screen, grid, cell_size, is_running=True)
            pygame.display.update()

        # time.sleep(0.01)

        clock = pygame.time.Clock()
        fps = 45
        clock.tick(fps)


if __name__ == "__main__":
    main()
