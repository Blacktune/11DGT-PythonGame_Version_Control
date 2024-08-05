import pygame
from pygame.locals import *
import random

def lvl1_screen():
    pygame.init()

    clock = pygame.time.Clock()
    fps = 60

    # Set screen width and height
    screen_width = 936
    screen_height = 864

    # Set character height and width
    ch_height = 50
    ch_width = 50

    #Set Merchant height
    ms_height = 100
    ms_width = 100


    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("The Fishing Mystery")

    pygame.mixer.init()  # initialize the mixer
    pygame.mixer.music.stop()  # stop the previous song muisic

    # Load and play the song
    pygame.mixer.music.load('sound.mp3/lvl1_song.mp3')
    pygame.mixer.music.play(-1)

    # Define the font for the game
    font = pygame.font.SysFont('Baus 93', 60)

    # Create our background image for our game
    bg = pygame.image.load('img/th.png')
    bg = pygame.transform.scale(bg, (screen_width, screen_height))  # resizes the image to fill the screen

    # Create our playable character
    ch = pygame.image.load('img/Fishing_Character-removebg-preview.png')
    ch = pygame.transform.scale(ch, (ch_width, ch_height))

    # create our Merchant
    ms = pygame.image.load('img/shop.png')
    ms = pygame.transform.scale(ms,(ms_width, ms_height))

    # Set initial character position
    ch_x = screen_width // 2 - ch_width // 2
    ch_y = screen_height // 2 - ch_height // 2 + 135
    # Set the speed of the character
    speed = 2
    # Define the boundaries for obstacles
    house_rect = pygame.Rect(370, 350, 200, 200) # x, y, width, height
    left_lake_rect = pygame.Rect (0,400,340,500) #x, y, width, height
    horizon_y = 500 # y-coordinate of the horizon line
    merchant_rect = pygame.Rect(648, 542, 50,55)

    #define where the merchant will be
    ms_x = screen_width // 2 - ms_width // 2 + 200
    ms_y = screen_height // 2 - ms_height // 2 + 150

    # Create a screen that our game will be running on
    run = True
    while run:
        clock.tick(fps)
        screen.blit(bg, (0, 0))
        screen.blit(ch, (ch_x, ch_y))
        screen.blit(ms, (ms_x, ms_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Get key states
        keys = pygame.key.get_pressed()

        # Move left
        if keys[K_LEFT]:
            new_x = ch_x - speed
            if new_x >= 0 and not (house_rect.collidepoint(new_x, ch_y) or
                                   left_lake_rect.collidepoint(new_x, ch_y) or
                                    merchant_rect.collidepoint(new_x, ch_y)):
                ch_x = new_x

        # Move right
        if keys[K_RIGHT]:
            new_x = ch_x + speed
            if new_x <= screen_width - ch_width and not (house_rect.collidepoint(new_x + ch_width, ch_y) or
                                                         left_lake_rect.collidepoint(new_x + ch_width, ch_y) or
                                                            merchant_rect.collidepoint(new_x + ch_width, ch_y)):
                ch_x = new_x

        # Move up
        if keys[K_UP]:
            new_y = ch_y - speed
            if new_y >= 0 and new_y >= horizon_y and not (house_rect.collidepoint(ch_x, new_y) or
                                                          left_lake_rect.collidepoint(ch_x, new_y) or
                                                            merchant_rect.collidepoint(ch_x, ch_y)):
                ch_y = new_y

        # Move down
        if keys[K_DOWN]:
            new_y = ch_y + speed
            if new_y <= screen_height - ch_height and not (house_rect.collidepoint(ch_x, new_y + ch_height) or
                                                           left_lake_rect.collidepoint(ch_x, new_y + ch_height) or
                                                            merchant_rect.collidepoint(ch_x, new_y + ch_height)):
                ch_y = new_y

        pygame.display.update()

    pygame.quit()
pass
