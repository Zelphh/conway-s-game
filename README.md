# Conway's Game of Life – Pygame Simulation

#### Video Demo: <URL HERE>
#### Description:
This project is a graphical simulation of Conway's Game of Life using Python and the Pygame library. The Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning its evolution is determined by its initial state, requiring no further input. Players interact with the simulation by altering the initial state and observing how it evolves over time.

The simulation grid is rendered in a Pygame window, where each cell can be in one of two states: alive or dead. The state of each cell in the next generation depends on its number of live neighbors, following these rules:

- A live cell with fewer than two live neighbors dies (underpopulation).k
- A live cell with two or three live neighbors lives on.
- A live cell with more than three live neighbors dies (overpopulation).
- A dead cell with exactly three live neighbors becomes a live cell (reproduction).

Users can interact with the simulation by:
- Clicking on cells to toggle their state between alive and dead.
- Pressing the spacebar to start or pause the simulation.

The code initializes an 800x600 pixel grid composed of 60 rows and 80 columns, with each cell being 10x10 pixels. It also includes color-coded feedback to indicate the state of each cell:
- **Alive** cells appear in bright green.
- **Dying** cells (those that will die in the next generation) appear in a darker green.
- **Dead** cells remain black.

The project consists of the following components:
- `main()` function: Initializes the Pygame window and event loop.
- `update_generation()`: Computes and renders the next state of the grid based on Conway's rules.
- User input handling for mouse clicks and keyboard input.
- Frame rate regulation using `pygame.time.Clock()`.

This project was designed to demonstrate understanding of:
- Basic principles of cellular automata.
- Event-driven programming in Python.
- Use of NumPy for efficient grid manipulation.
- Pygame for graphical rendering and user interaction.

The code is structured in a single file for simplicity but can be extended with additional features such as saving/loading grid states, different rule sets, and UI controls for adjusting simulation speed and grid size.

Be proud of your work! This `README.md` aims to fully document the intent, structure, and interaction model of the project. If it feels sufficiently detailed and informative, then the project complexity is on the right track.
