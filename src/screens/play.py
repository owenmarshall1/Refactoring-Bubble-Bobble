from game import Game, Player, draw_status


class PlayScreen:
    def __init__(self, app):
        self.app = app
        self.game = Game(Player())

    def update(self, input_state):
        # Import game module to access global game reference
        import game as game_module
        game_module.game = self.game
        
        # Update game logic with input state
        self.game.update(input_state)

        # Check if player is dead
        if self.game.player.lives < 0:
            self.game.play_sound("over")
            # Import here to avoid circular imports
            from src.screens.game_over import GameOverScreen
            # Switch to game over screen
            game_over_screen = GameOverScreen(self.app, self.game)
            self.app.change_screen(game_over_screen)

    def draw(self):
        # Import game module to set up for draw_status() function
        import game as game_module
        game_module.game = self.game
        
        # Draw game
        self.game.draw()

        # Draw status bar
        draw_status()
