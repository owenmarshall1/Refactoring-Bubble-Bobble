from game import draw_status


class GameOverScreen:
    def __init__(self, app, game):
        self.app = app
        self.game = game

    def update(self, input_state):
        # Import game module to access global reference
        import game as game_module
        game_module.game = self.game
        
        # Check if space is pressed to transition back to menu
        if input_state.fire_pressed:
            # Import here to avoid circular imports
            from src.screens.menu import MenuScreen
            # Switch to menu state
            menu_screen = MenuScreen(self.app)
            self.app.change_screen(menu_screen)

    def draw(self):
        # Import game module to access screen and game reference
        import game as game_module
        game_module.game = self.game
        
        # Draw game
        self.game.draw()

        # Draw status bar
        draw_status()
        
        # Display "Game Over" image
        game_module.screen.blit("over", (0, 0))
