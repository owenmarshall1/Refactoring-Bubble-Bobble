# Refactoring-Bubble-Bobble

This project is a refactored version of Bubble Bobble a small arcade-style platformer built using Pygame Zero. The game includes a menu, gameplay screen, game over screen, and pause feature. It uses a simple screen/state system to manage flow.

## Features
- Menu, play, and game over screens
- Player movement, jumping, and shooting
- Enemies and basic level layouts
- Pause functionality during gameplay
- Centralized input handling

## Project Structure
- `main.py` – Entry point and game loop
- `app.py` – Manages screen transitions
- `game.py` – Core game logic and simulation
- `screens/` – Menu, play, and game over screens
- `entities/` – Player, enemies, and other game objects
- `input.py` – Input state handling

## Controls
- **Left / Right Arrow** – Move
- **Up Arrow** – Jump
- **Space** – Shoot / Select
- **P** – Pause (during gameplay)

## Running the Game
Make sure you have Pygame Zero installed, then run:

```bash
pgzrun main.py
```
If you do not have Pygame Zero installed, then run:
```bash
pip install pgzero
```