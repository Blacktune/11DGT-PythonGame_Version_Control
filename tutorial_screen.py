import pygame
from pygame.locals import *
import random

def tutorial_screen():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60

    # Set screen width and height
    screen_width = 936
    screen_height = 864


    #set play button size
    pb_width = 500
    pb_height = 500

    #set tutorial button size
    tb_width = 500
    tb_height = 500

    #set tutorial button size
    sb_width = 500
    sb_height = 500

    # Create the screen with titels
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("The Fishing Mystery")

    # Define the font for the game
    font = pygame.font.SysFont('Baus 93', 60)


    pygame.mixer.init()  # initialize the mixer
    pygame.mixer.music.stop()  # stop the previous song muisic

    # Load and play the song
    pygame.mixer.music.load('sound.mp3/home_screen_sound.mp3')
    pygame.mixer.music.play(-1)

    # Create our background image for our game
    bg = pygame.image.load('img/th.png')
    bg = pygame.transform.scale(bg, (screen_width, screen_height))  # resizes the image to fill the screen

    #Create the play button
    pb = pygame.image.load('img/pixilart-drawing.png')
    pb = pygame.transform.scale(pb, (pb_width, pb_height))

    #create the tutorial button
    tb = pygame.image.load('img/tutorial_button.png')
    tb = pygame.transform.scale(tb, (tb_width, tb_height))

    #create the settings button
    sb = pygame.image.load('img/settings_button.png')
    sb = pygame.transform.scale(sb,(sb_width, sb_height))


    #Set playbutton location
    pb_x = (screen_width - screen_height) / 2
    pb_y = 0

    #set tutorial button location
    tb_x = (screen_width - screen_height) / 1 + 100
    tb_y = 0

    #set settings button loaction
    sb_x = (screen_width - screen_height) / 1 - 73
    sb_y = 300


    # Create a screen that our game will be running on
    run = True
    while run:
        clock.tick(fps)
        screen.blit(bg, (0, 0))
        screen.blit(pb, (pb_y,pb_x))
        screen.blit(tb, (tb_y, tb_x))
        screen.blit(sb, (sb_x,sb_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()

pass

