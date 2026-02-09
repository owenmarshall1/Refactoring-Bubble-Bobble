from src.screens.menu import MenuScreen


class App:
    def __init__(self):
        self.screen = MenuScreen(self)

    def change_screen(self, screen):
        self.screen = screen

    def update(self):
        self.screen.update()

    def draw(self):
        self.screen.draw()
