import pygame  # Import the Pygame library for game development
from pygame.locals import *  # Import constants for ease of use


def tutorial_screen():
    pygame.init()  # Initialize Pygame modules for use
    clock = pygame.time.Clock()  # Create a clock to manage frame rate
    fps = 60  # Set frames per second for the game loop

    # Define the screen dimensions
    screen_width = 936
    screen_height = 864

    # Set tutorial button dimensions
    tc_width = 500
    tc_height = 500

    # Create the game window
    screen = pygame.display.set_mode((screen_width, screen_height))  # Set up the display
    pygame.display.set_caption("The Fishing Mystery")  # Set the window title

    # Define the font for text rendering
    font = pygame.font.SysFont('Baus 93', 30)

    # Initialize audio mixer
    pygame.mixer.init()
    pygame.mixer.music.stop()  # Stop any playing music

    # Load and play background music
    pygame.mixer.music.load('sound.mp3/tutorial_screen_sound.mp3')
    pygame.mixer.music.play(-1)  # Play music in a loop

    # Set the initial volume level
    pygame.mixer.music.set_volume(1.0)  # Full volume

    # Load and resize the background image
    bg = pygame.image.load('img/th.png')
    bg = pygame.transform.scale(bg, (screen_width, screen_height))

    # Main game loop
    run = True
    while run:
        clock.tick(fps)  # Maintain the frame rate
        screen.blit(bg, (0, 0))  # Draw the background

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check for close event
                run = False  # Exit the loop

        # Check key presses
        keys = pygame.key.get_pressed()  # Get current key states
        current_volume = pygame.mixer.music.get_volume()  # Get current volume

        # Volume adjustment
        if keys[K_i]:  # Decrease volume with 'I'
            new_volume = max(0.0, current_volume - 0.1)  # Ensure it doesn't go below 0
            pygame.mixer.music.set_volume(new_volume)  # Set new volume
        if keys[K_o]:  # Increase volume with 'O'
            new_volume = min(1.0, current_volume + 0.1)  # Ensure it doesn't exceed 1
            pygame.mixer.music.set_volume(new_volume)  # Set new volume

        # Render tutorial instructions (The words written, setting it to true, and setting its color to black)
        t_text1 = font.render("The goal of this game is to catch as many fish as possible!", True, (0, 0, 0))
        screen.blit(t_text1, (60, 50))  # Display first line of text
        t_text2 = font.render("Press [F] to fish for experience and money!", True, (0, 0, 0))
        screen.blit(t_text2, (60, 100))  # Second instruction
        t_text3 = font.render("Press [1], [2], [3] to purchase upgrades, [S] for attributes", True, (0, 0, 0))
        screen.blit(t_text3, (60, 150))  # Third instruction
        t_text4 = font.render("Use arrow keys to move", True, (0, 0, 0))
        screen.blit(t_text4, (60, 200))  # Fourth instruction
        t_text5 = font.render("Press [I] to mute, [O] to unmute", True, (0, 0, 0))
        screen.blit(t_text5, (60, 250))  # Fifth instruction
        t_text6 = font.render("Enjoy the game! Feedback? Check the settings page.", True, (0, 0, 0))
        screen.blit(t_text6, (60, 300))  # Sixth instruction
        t_text7 = font.render("Restart the game to return to the home page!", True, (0, 0, 0))
        screen.blit(t_text7, (60, 350))  # Seventh instruction

        pygame.display.update()  # Update the display

    pygame.quit()  # Clean up and close the window


pass