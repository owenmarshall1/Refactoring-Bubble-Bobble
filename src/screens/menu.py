from game import Game, Player, space_pressed


class MenuScreen:
    def __init__(self, app):
        self.app = app
        self.game = Game()

    def update(self, input_state):
        # Import game module to access global reference
        import game as game_module
        game_module.game = self.game
        
        # Update game logic even on menu screen
        self.game.update()

        # Check if space is pressed to transition to play screen
        if space_pressed():
            # Import here to avoid circular imports
            from src.screens.play import PlayScreen
            # Switch to play state, and create a new Game object with a Player
            play_screen = PlayScreen(self.app)
            self.app.change_screen(play_screen)

    def draw(self):
        # Import screen here to access pgzero's screen object
        import game as game_module
        
        self.game.draw()

        # Draw title screen
        game_module.screen.blit("title", (0, 0))

        # Draw "Press SPACE" animation, which has 10 frames numbered 0 to 9
        anim_frame = min(((self.game.timer + 40) % 160) // 4, 9)
        game_module.screen.blit("space" + str(anim_frame), (130, 280))
