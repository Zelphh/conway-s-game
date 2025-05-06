# Conway's Game of Life - Enhanced Version

#### Video Demo: <URL HERE>

#### Description:

This project is an enhanced implementation of **Conway’s Game of Life** using Python and the `pygame` library. It simulates a two-dimensional cellular automaton where cells evolve based on a set of simple rules. While the core logic follows Conway’s original rules, this version includes several **interactive features** that allow for dynamic user input, real-time control over simulation speed, pattern saving/loading, and toggling the grid visibility.

Conway’s Game of Life is a zero-player game: its evolution is determined by its initial state, requiring no further input. However, we have added interactive capabilities so that users can experiment and build complex structures in an intuitive and visual way.

---

## 🎮 Features and Functionality

### 🔁 Simulation Control (Start/Pause)
By pressing the `SPACEBAR`, users can toggle the simulation between "running" and "paused". While paused, users can freely draw or erase cells to prepare or modify their own custom patterns before letting them evolve. This real-time toggling helps users iterate quickly and observe cause-effect relationships in their cellular designs.

### 🖱️ Grid Interaction with Mouse
Users can click directly on the screen using the **left mouse button** to activate or deactivate cells. This makes it easy to:
- Draw your own initial conditions.
- Add live cells during the simulation.
- Fix or modify errors in real time.

### ⏱️ FPS (Speed) Control
To offer fine-grained control over the simulation speed, we implemented keyboard-based FPS (Frames Per Second) adjustment:
- Press `UP ARROW` to **increase FPS** (max: 60).
- Press `DOWN ARROW` to **decrease FPS** (min: 1).

This allows users to slow down the simulation to observe detailed transitions or speed it up when watching stable patterns evolve.

### 💾 Pattern Saving and Loading
A key addition is the ability to **save** the current grid state and **load** it later.

- Press `S` to save the current configuration into a file called `saved_pattern.json`. This file will store the entire grid state using Python’s JSON module.
- Press `L` to load this saved configuration at any time, effectively restoring your last saved simulation.

This feature is useful for creating, testing, and reusing complex patterns such as gliders, oscillators, or spaceships.

### 🧼 Grid Reset
If you want to start over, just press the `C` key. This **clears the entire grid**, setting all cells to dead. It's useful after a long simulation or when your pattern reaches a chaotic or undesired state.

### 🧮 Grid Visibility Toggle
Press `G` to toggle the visibility of grid lines. This visual adjustment can help focus on pattern formation without the distraction of lines or, conversely, better identify cell boundaries when needed.

---

## 💡 Conway’s Game of Life Rules

The game consists of a grid of cells which can be in two states: **alive (1)** or **dead (0)**. At each step in time, the following transitions occur based on the number of live neighbors:

- Any **live cell** with **fewer than two** live neighbors dies (underpopulation).
- Any **live cell** with **two or three** live neighbors lives on.
- Any **live cell** with **more than three** live neighbors dies (overpopulation).
- Any **dead cell** with **exactly three** live neighbors becomes a live cell (reproduction).

These simple rules can produce incredibly complex and unexpected patterns over time.

---

## 🛠️ Implementation Details

The simulation was developed in Python using `pygame` for the graphical interface and `numpy` for efficient grid handling.

- Grid Size: 60 rows × 80 columns.
- Cell Size: 10 × 10 pixels.
- Colors:
  - Background: dark gray/black
  - Alive cell: green
  - Dying cell (when running): darker green
  - Grid lines: gray

Each frame of the simulation calculates a new generation based on the current grid state and updates the screen accordingly.

The `update_generation()` function handles both the logic and rendering. It uses NumPy slicing to efficiently count neighbors and decide the next state for each cell. All visual rendering is done via `pygame.draw.rect`.

---

## 🧪 Design Decisions

- **Interactive Design**: Rather than running a static simulation, interactivity was prioritized to let users experiment with patterns hands-on.
- **FPS Tuning**: Some simulations evolve too quickly to observe. Including FPS control lets users step through slowly or speed through stable areas.
- **State Persistence**: Saving and loading patterns promotes experimentation. You can pause, save your grid, close the app, and return to the exact state later.
- **Minimal External Dependencies**: Only `pygame` and `numpy` are required, both of which are widely supported and easy to install.

---

## 📂 File Structure
