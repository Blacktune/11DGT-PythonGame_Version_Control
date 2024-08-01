import pygame
from pygame.locals import *
import random

def settings_screen():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60

    # Set screen width and height
    screen_width = 936
    screen_height = 864

    #Set Tutorial screen width and height
    sc_width = 500
    sc_height = 500


    # Create the screen with titels
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("The Fishing Mystery")

    # Define the font for the game
    font = pygame.font.SysFont('Baus 93', 60)


    pygame.mixer.init()  # initialize the mixer
    pygame.mixer.music.stop()  # stop the previous song muisic

    # Load and play the song
    pygame.mixer.music.load('sound.mp3/settings_screen_sound.mp3')
    pygame.mixer.music.play(-1)

    # Create our background image for our game
    bg = pygame.image.load('img/th.png')
    bg = pygame.transform.scale(bg, (screen_width, screen_height))  # resizes the image to fill the screen

    #create our tutorial screen
    sc = pygame.image.load('img/settings_button.png')
    sc = pygame.transform.scale(sc,(sc_width,sc_height))


    # Create a screen that our game will be running on
    run = True
    while run:
        clock.tick(fps)
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()

pass