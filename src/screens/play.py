from game import Game, Player, draw_status


class PlayScreen:
    def __init__(self, app):
        self.app = app
        self.game = Game(Player())
        self.paused = False

    def update(self, input_state):
        # Import game module to access global game reference
        import game as game_module
        game_module.game = self.game
        
        # Toggle pause when P is pressed
        if input_state.pause_pressed:
            self.paused = not self.paused
        
        # If paused, freeze simulation
        if self.paused:
            return
        
        # Update game logic with input state
        self.game.update(input_state)

        # Check if player is dead
        if self.game.player.lives < 0:
            self.game.play_sound("over")
            from src.screens.game_over import GameOverScreen
            # Switch to game over screen
            game_over_screen = GameOverScreen(self.app, self.game)
            self.app.change_screen(game_over_screen)

    def draw(self):
        import game as game_module
        game_module.game = self.game
        
        self.game.draw()

        draw_status()
        
        # Draw pause overlay if paused
        if self.paused:
            game_module.screen.draw.text("PAUSED", center=(400, 240), fontsize=60, color="white")
            game_module.screen.draw.text("Press P to resume", center=(400, 320), fontsize=30, color="white")
