import pygame  # Import Pygame for game development
from pygame.locals import *  # Import constants for easier access
import random  # Import random for future use


def settings_screen():
    pygame.init()  # Initialize Pygame modules
    clock = pygame.time.Clock()  # Create a clock to manage frame rate
    fps = 60  # Set frames per second

    # Set dimensions for the game window
    screen_width = 936
    screen_height = 864

    # Create the main game window
    screen = pygame.display.set_mode((screen_width, screen_height))  # Set display size
    pygame.display.set_caption("The Fishing Mystery")  # Set window title

    # Define font for text rendering
    font = pygame.font.SysFont('Baus 93', 40)

    # Initialize audio mixer
    pygame.mixer.init()
    pygame.mixer.music.stop()  # Stop any playing music

    # Load and play background music
    pygame.mixer.music.load('sound.mp3/settings_screen_sound.mp3')
    pygame.mixer.music.play(-1)  # Loop the music

    # Set initial music volume
    pygame.mixer.music.set_volume(1.0)  # Full volume

    # Load and resize background image
    bg = pygame.image.load('img/th.png')
    bg = pygame.transform.scale(bg, (screen_width, screen_height))

    # Main game loop
    run = True
    while run:  # For while the loop is True the code inside will be running forever unless it is set to false
        clock.tick(fps)  # Limit to the set FPS
        screen.blit(bg, (0, 0))  # Draw background

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check for quit event
                run = False  # Exit loop

        # Handle key presses
        keys = pygame.key.get_pressed()
        current_volume = pygame.mixer.music.get_volume()  # Get current volume

        # Adjust volume with key presses
        if keys[K_i]:  # Decrease volume with 'I'
            new_volume = max(0.0, current_volume - 0.1)  # Ensure it doesn't go below 0
            pygame.mixer.music.set_volume(new_volume)  # Update volume
        if keys[K_o]:  # Increase volume with 'O'
            new_volume = min(1.0, current_volume + 0.1)  # Ensure it doesn't exceed 1
            pygame.mixer.music.set_volume(new_volume)  # Update volume

        # Display instructions on the settings screen
        s_text1 = font.render("There are no current changeable settings :(", True, (255, 255, 255))
        screen.blit(s_text1, (60, 50))
        s_text2 = font.render("To report any bugs or suggestions, please email me at:", True, (255, 255, 255))
        screen.blit(s_text2, (60, 100))
        s_text3 = font.render("dnv.gaming.industries@gmail.com (All support welcome!)", True, (255, 255, 255))
        screen.blit(s_text3, (60, 150))

        pygame.display.update()  # Refresh the display

    pygame.quit()  # Close the game window

pass