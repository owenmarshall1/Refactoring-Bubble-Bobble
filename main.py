import sys
import pgzero
import pgzrun

# Check Python version number. sys.version_info gives version as a tuple, e.g. if (3,7,2,'final',0) for version 3.7.2.
# Unlike many languages, Python can compare two tuples in the same way that you can compare numbers.
if sys.version_info < (3,5):
    print("This game requires at least version 3.5 of Python. Please download it from www.python.org")
    sys.exit()

# Check Pygame Zero version. This is a bit trickier because Pygame Zero only lets us get its version number as a string.
# So we have to split the string into a list, using '.' as the character to split on. We convert each element of the
# version number into an integer - but only if the string contains numbers and nothing else, because it's possible for
# a component of the version to contain letters as well as numbers (e.g. '2.0.dev0')
# We're using a Python feature called list comprehension - this is explained in the Bubble Bobble/Cavern chapter.
pgzero_version = [int(s) if s.isnumeric() else s for s in pgzero.__version__.split('.')]
if pgzero_version < [1,2]:
    print("This game requires at least version 1.2 of Pygame Zero. You have version {0}. Please upgrade using the command 'pip3 install --upgrade pgzero'".format(pgzero.__version__))
    sys.exit()

from game import *

import game as game_module

# Pygame Zero calls the update and draw functions each frame

class State(Enum):
    MENU = 1
    PLAY = 2
    GAME_OVER = 3


def update():
    global state, game
    game_module.keyboard = keyboard
    game_module.screen = screen
    game_module.sounds = sounds
    game_module.music = music
    game_module.game = game

    if state == State.MENU:
        if space_pressed():
            # Switch to play state, and create a new Game object, passing it a new Player object to use
            state = State.PLAY
            game = Game(Player())
        else:
            game.update()

    elif state == State.PLAY:
        if game.player.lives < 0:
            game.play_sound("over")
            state = State.GAME_OVER
        else:
            game.update()

    elif state == State.GAME_OVER:
        if space_pressed():
            # Switch to menu state, and create a new game object without a player
            state = State.MENU
            game = Game()

def draw():
    game_module.screen = screen
    game_module.game = game

    game.draw()

    if state == State.MENU:
        # Draw title screen
        screen.blit("title", (0, 0))

        # Draw "Press SPACE" animation, which has 10 frames numbered 0 to 9
        # The first part gives us a number between 0 and 159, based on the game timer
        # Dividing by 4 means we go to a new animation frame every 4 frames
        # We enclose this calculation in the min function, with the other argument being 9, which results in the
        # animation staying on frame 9 for three quarters of the time. Adding 40 to the game timer is done to alter
        # which stage the animation is at when the game first starts
        anim_frame = min(((game.timer + 40) % 160) // 4, 9)
        screen.blit("space" + str(anim_frame), (130, 280))

    elif state == State.PLAY:
        draw_status()

    elif state == State.GAME_OVER:
        draw_status()
        # Display "Game Over" image
        screen.blit("over", (0, 0))

# Set up sound system and start music
try:
    pygame.mixer.quit()
    pygame.mixer.init(44100, -16, 2, 1024)

    music.play("theme")
    music.set_volume(0.3)
except:
    # If an error occurs, just ignore it
    pass



# Set the initial game state
state = State.MENU

# Create a new Game object, without a Player object
game = Game()

game_module.game = game

pgzrun.go()