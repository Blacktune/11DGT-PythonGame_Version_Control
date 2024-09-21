import pygame
from pygame.locals import *  # so we can use all of pygame files

# Import the code from the other screens, so we can use it here
from lvl1_screen import (lvl1_screen)
from tutorial_screen import (tutorial_screen)
from settings_screen import (settings_screen)

# Init pygame and set up the fps that our game will be running at Teh refresh rate in seconds.
pygame.init()
clock = pygame.time.Clock()
fps = 60

# Set screen width and height for our game window
screen_width = 936
screen_height = 864


# Set play button size using 2 variables one for height and one for width
pb_width = 500
pb_height = 500

# Set tutorial button size using 2 variables one for height and one for width
tb_width = 500
tb_height = 500

# Set tutorial button size 2 variables one for height anf one for width
sb_width = 500
sb_height = 500

# Create the actual screen by using the set variables
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Fishing Mystery")

# Define the font for the game, choice of font, and font size
font = pygame.font.SysFont('Bauhaus 93', 40)

# init our home_page music my using the pygame.mixer
pygame.mixer.init()  # initialize the mixer
pygame.mixer.music.stop()  # stop the previous song music so the songs don't overlap

# Load and play the song we have chosen
pygame.mixer.music.load('sound.mp3/home_screen_sound.mp3')
pygame.mixer.music.play(-1)  # make it loop forever

# Set initial volume to 1.0 (full volume)
pygame.mixer.music.set_volume(1.0)

# Create our background image for our game (Note 1)
bg = pygame.image.load('img/th.png')
bg = pygame.transform.scale(bg, (screen_width, screen_height))  # resizes the image to fill the screen

# Create the play button "Note 1" (accessing it from out library we are making it a variable, we can access it later)
pb = pygame.image.load('img/pixilart-drawing.png')
pb = pygame.transform.scale(pb, (pb_width, pb_height)) # resizes the image to fill the screen

# Create the tutorial button (Note 1)
tb = pygame.image.load('img/tutorial_button.png')
tb = pygame.transform.scale(tb, (tb_width, tb_height))

# Create the settings button (Note 1)
sb = pygame.image.load('img/settings_button.png')
sb = pygame.transform.scale(sb,(sb_width, sb_height))


# Set play button x and y location (Note 1)
pb_x = (screen_width - screen_height) / 2
pb_y = 0

# Set tutorial button x and y location (Note 1)
tb_x = (screen_width - screen_height) / 1 + 100
tb_y = 0

# Set settings button x and y location (Note 1)
sb_x = (screen_width - screen_height) / 1 - 73
sb_y = 300


# Create a screen that our game will be running on, so we can visually see what's going on
# creating a while loop for our game to run in
run = True
while run:
    # Call and display all the functions that we have made and use them on the screen
    clock.tick(fps)
    screen.blit(bg, (0, 0))  # Background image called
    screen.blit(pb, (pb_y,pb_x))  # Play button called
    screen.blit(tb, (tb_y, tb_x))  # Tutorial button called
    screen.blit(sb, (sb_x,sb_y))  # Settings button called

    # Create a loop that checks if the game has been asked to quit and if it is to close the page
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # create a variable that will check if a key has been pressed
    keys = pygame.key.get_pressed()

    # Make the instructions on how to play the game appear at the top of the screen by rendering the font
    instructions_text = font.render("Press P to play! \n Press T for tutorial! \n Press S for settings!", True, (255, 255, 255))
    screen.blit(instructions_text,(60,50))  # Take the text and give it a place to sit on screen using x and y

    # Go to lvl1 page if "P" is pressed
    if keys[K_p]:
        lvl1_screen()  # switch to the new screen
        run = False  # quit current screen

    # Go to the Tutorial screen if "T" is pressed
    if keys[K_t]:
        tutorial_screen()  # switch to the new screen
        run = False  # quit current screen

    #  Go to the Settings screen if "S" is pressed
    if keys[K_s]:
        settings_screen()  # switch to the new screen
        run = False  # quit current screen

    # Get current volume and define it as current_volume, so we can use it as a variable
    current_volume = pygame.mixer.music.get_volume()

    # Check for volume adjustment keys
    if keys[K_i]:  # Press 'I' to decrease the volume
        new_volume = max(0.0, current_volume - 0.1)  # Ensure volume doesn't go below 0.0
        pygame.mixer.music.set_volume(new_volume)  # Make that the new volume
    if keys[K_o]:  # Press 'O' to increase the volume
        new_volume = min(1.0, current_volume + 0.1)  # Ensure volume doesn't go above 1.0
        pygame.mixer.music.set_volume(new_volume)  # Make that the new volume

    pygame.display.flip()
    pygame.display.update()
pygame.quit()

