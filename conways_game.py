import numpy as np
import pygame
import json
import os

import pygame.image

# Configurações básicas
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
FPS_MIN, FPS_MAX = 1, 60
SAVE_FILE = "saved_pattern.json"

# Cores
BACKGROUND_COLOR = (10, 10, 10)
GRID_LINE_COLOR = (50, 50, 50)
ALIVE_COLOR = (0, 220, 0)

class GameOfLife:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Conway's Game of Life")
        icon = pygame.image.load("icon.png")
        pygame.display.set_icon(icon)
        self.clock = pygame.time.Clock()
        self.grid = np.zeros((ROWS, COLS), dtype=int)
        self.running = False
        self.fps = 10
        self.show_grid = True

    def draw_grid(self):
        self.screen.fill(BACKGROUND_COLOR)
        for row in range(ROWS):
            for col in range(COLS):
                if self.grid[row, col] == 1:
                    pygame.draw.rect(self.screen, ALIVE_COLOR,
                                     (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE-1, CELL_SIZE-1))
        if self.show_grid:
            for x in range(0, WIDTH, CELL_SIZE):
                pygame.draw.line(self.screen, GRID_LINE_COLOR, (x, 0), (x, HEIGHT))
            for y in range(0, HEIGHT, CELL_SIZE):
                pygame.draw.line(self.screen, GRID_LINE_COLOR, (0, y), (WIDTH, y))

    def update_generation(self):
        next_grid = np.zeros((ROWS, COLS), dtype=int)
        for row in range(ROWS):
            for col in range(COLS):
                alive_neighbors = np.sum(self.grid[max(0, row-1):min(ROWS, row+2),
                                                   max(0, col-1):min(COLS, col+2)]) - self.grid[row, col]
                if self.grid[row, col] == 1 and alive_neighbors in [2, 3]:
                    next_grid[row, col] = 1
                elif self.grid[row, col] == 0 and alive_neighbors == 3:
                    next_grid[row, col] = 1
        self.grid = next_grid

    def toggle_cell(self, pos):
        col, row = pos[0] // CELL_SIZE, pos[1] // CELL_SIZE
        self.grid[row, col] = 0 if self.grid[row, col] else 1

    def clear_grid(self):
        self.grid = np.zeros((ROWS, COLS), dtype=int)

    def save_pattern(self):
        with open(SAVE_FILE, "w") as f:
            json.dump(self.grid.tolist(), f)

    def load_pattern(self):
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, "r") as f:
                self.grid = np.array(json.load(f), dtype=int)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.running = not self.running
                    elif event.key == pygame.K_c:
                        self.clear_grid()
                    elif event.key == pygame.K_s:
                        self.save_pattern()
                    elif event.key == pygame.K_l:
                        self.load_pattern()
                    elif event.key == pygame.K_g:
                        self.show_grid = not self.show_grid
                    elif event.key == pygame.K_UP:
                        self.fps = min(self.fps + 5, FPS_MAX)
                    elif event.key == pygame.K_DOWN:
                        self.fps = max(self.fps - 5, FPS_MIN)
                elif pygame.mouse.get_pressed()[0]:
                    self.toggle_cell(pygame.mouse.get_pos())

            if self.running:
                self.update_generation()

            self.draw_grid()
            pygame.display.flip()
            self.clock.tick(self.fps)

if __name__ == "__main__":
    GameOfLife().run()
