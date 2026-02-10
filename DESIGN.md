# Design Overview
## Screens Architecture

The game uses a simple screen-based architecture instead of a global state enum. Each screen represents a distinct mode of the game and is responsible for its own update and draw logic.

The main screens are:
- MenuScreen – Displays the start menu and waits for player input to begin the game.
- PlayScreen – Runs the main gameplay loop and owns the active Game instance.
- GameOverScreen – Displays the game over screen and allows restarting.

An App class manages the currently active screen. The main `update()` and `draw()` functions delegate directly to the active screen through the App, making screen transitions explicit and easy to follow.

Screens are responsible for deciding when to transition to another screen (for example, when the player runs out of lives).

## Input Design

Input handling is centralized using an `InputState` object. Each frame, keyboard input is read once and converted into a snapshot of the current input state.

This snapshot is then passed down through the application:
- `App` builds the input state
- Screens receive the input state in their `update` method
- Gameplay logic (such as the player) reacts to the input state instead of reading from the keyboard directly

This approach avoids scattered keyboard access and makes the game logic easier to test and reason about. It also allows actions like “pressed” versus “held” to be handled consistently.

## Pause System

Pause functionality is handled entirely within the `PlayScreen`.

When the pause key is pressed, a `paused` flag is toggled. While paused:
- The game simulation (`Game.update`) is not called
- Rendering continues so the current frame remains visible
- A “PAUSED” message is drawn on top of the game

Because only the update step is skipped, all movement, timers, and enemy behavior are effectively frozen until the game is unpaused. This keeps the pause logic simple and avoids modifying individual game entities.
