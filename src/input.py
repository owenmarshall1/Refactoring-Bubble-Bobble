from dataclasses import dataclass


@dataclass
class InputState:
    left: bool
    right: bool
    jump_pressed: bool
    fire_pressed: bool
    fire_held: bool
    pause_pressed: bool


class InputHandler:
    def __init__(self):
        self.prev_space = False
        self.prev_p = False

    def build(self):
        from game import keyboard
        
        space = keyboard.space
        p = keyboard.p
        state = InputState(
            left=keyboard.left,
            right=keyboard.right,
            jump_pressed=keyboard.up,
            fire_pressed=space and not self.prev_space,
            fire_held=space,
            pause_pressed=p and not self.prev_p
        )
        self.prev_space = space
        self.prev_p = p
        return state
