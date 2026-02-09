from dataclasses import dataclass


@dataclass
class InputState:
    left: bool
    right: bool
    jump_pressed: bool
    fire_pressed: bool
    fire_held: bool


class InputHandler:
    def __init__(self):
        self.prev_space = False

    def build(self):
        from game import keyboard
        
        space = keyboard.space
        state = InputState(
            left=keyboard.left,
            right=keyboard.right,
            jump_pressed=keyboard.up,
            fire_pressed=space and not self.prev_space,
            fire_held=space
        )
        self.prev_space = space
        return state
