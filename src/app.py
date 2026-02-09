from src.screens.menu import MenuScreen
from src.input import InputHandler


class App:
    def __init__(self):
        self.input = InputHandler()
        self.screen = MenuScreen(self)

    def change_screen(self, screen):
        self.screen = screen

    def update(self):
        input_state = self.input.build()
        self.screen.update(input_state)

    def draw(self):
        self.screen.draw()
