# 🐍 Snake Game (Python & Pygame)

A classic **Snake game** implemented in **Python using Pygame**, focused on clean game logic, state management, and simple UI elements such as pause, restart, and score display.

This project was built as a learning exercise to practice game loops, event handling, and basic game architecture.

---

## 🎮 Features

- Classic Snake gameplay
- Movement using **WASD**
- Score system
- **Pause / Resume** functionality
- Restart after Game Over
- Collision detection (walls & self)
- Clean and readable code structure
- Game state handled through a dedicated `GameState` class

---

## 🕹 Controls

| Key | Action |
|----|-------|
| **W** | Move up |
| **A** | Move left |
| **S** | Move down |
| **D** | Move right |
| **P** | Pause / Resume |
| **R** | Restart (after Game Over) |

---

## 🧠 How the Game Works

- The snake is represented as a list of `pygame.Rect` objects
- The apple is randomly repositioned on the grid after being eaten
- Game state (score, pause, direction, game over) is managed using a `GameState` class
- During pause, the game logic is frozen while the last frame remains visible
- Rendering and game logic are separated for better readability

---

## 🛠 Requirements

- Python **3.9+** (recommended)
- Pygame

Install Pygame with:

```bash
pip install pygame
