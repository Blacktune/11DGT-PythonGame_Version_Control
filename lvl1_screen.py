import pygame
from pygame.locals import *
import random
from pygame import *

#  Define the code, so I can import this code to my home_screen and make it possible for the buttons to work
def lvl1_screen():
    pygame.init()

    #  Import time into our game, so we can use the funtion later on to see if something has happened in the previous frame
    clock = pygame.time.Clock()
    fps = 60

    # Define the font for the game, by using system font it makes it universal
    font = pygame.font.SysFont('Baus 93', 60)

    #  Create and put all my variables in a global loop, so I can access it anywhere in the code
    global money
    money = 0
    global money_text
    money_text = font.render(f"{money}", True, (255, 255, 255))
    global exp
    exp = 0
    global exp_text
    exp_text = font.render(f"{exp}", True, (255, 255, 255))
    global leveling
    leveling = 0
    global leveling_text
    leveling_text = font.render(f"{leveling}", True, (255, 255, 255))
    global game_over_text
    game_over_text = font.render(f"You Lost! Your money went into a negative!", True, (255, 255, 255))
    global fish_probabilities
    fish_probabilities = [1000, 1000, 1000, 1000, 500, 500, 500, 20, 50, 500, 500, 1]
    global upgrade_1_text
    upgrade_1_text = font.render("Upgrade 1 (Cost: 1000)", True, (255, 255, 255))
    global upgrade_2_text
    upgrade_2_text = font.render("Upgrade 2 (Cost: 5000)", True, (255, 255, 255))
    global upgrade_3_text
    upgrade_3_text = font.render("Upgrade 3 (Cost: 10000)", True, (255, 255, 255))

    # Set screen width and height in pixels
    screen_width = 936
    screen_height = 864

    # Set character height and width in pixels
    ch_height = 50
    ch_width = 50

    # Set Merchant height and width in pixels
    ms_height = 100
    ms_width = 100

    # Set shop menu height and width in pixels
    sm_height = 500
    sm_width = 300

    # Set coin size in pixels
    coin_height = 40
    coin_width = 40

    # Display the screen which all the setting on the device with the given screen width and height
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Create the caption for our app, so it has a name
    pygame.display.set_caption("The Fishing Mystery")

    # Init the mixer so, I can use it to allow the music to play.
    pygame.mixer.init()  # initialize the mixer
    pygame.mixer.music.stop()  # stop the previous song muisic

    # Load and play the song
    pygame.mixer.music.load('sound.mp3/lvl1_song.mp3')  # tell the program what song file to use
    pygame.mixer.music.play(-1)  # Make it loop forever

    # Set initial volume to 1.0 (full volume)
    pygame.mixer.music.set_volume(1.0)

    # Create our background image for our game
    bg = pygame.image.load('img/th.png')
    bg = pygame.transform.scale(bg, (screen_width, screen_height))  # resizes the image to fill the screen

    # Create our playable character
    ch = pygame.image.load('img/Fishing_Character-removebg-preview.png')
    ch = pygame.transform.scale(ch, (ch_width, ch_height))  # resizer the image to fill the screen

    # create our coin image
    coin = pygame.image.load('img/coin.png')
    coin = pygame.transform.scale(coin, (coin_width, coin_height))  # resizer the image to fill the screen

    # create our Merchant
    ms = pygame.image.load('img/shop.png')
    ms = pygame.transform.scale(ms,(ms_width, ms_height))  # resizer the image to fill the screen

    # create our shop menu
    sm = pygame.image.load('img/download.png')
    sm = pygame.transform.scale(sm, (sm_width,sm_height))  # resizer the image to fill the screen

    # Set initial character position
    ch_x = screen_width // 2 - ch_width // 2  # Doing it by starting it in the middle using // 2
    ch_y = screen_height // 2 - ch_height // 2 + 135  # Doing it by starting it in the middle using // 2
    # Set the speed of the character
    speed = 2
    # Define the boundaries for obstacles
    house_rect = pygame.Rect(370, 350, 200, 200)  # x, y, width, height
    left_lake_rect = pygame.Rect(0, 400, 340, 500)  # x, y, width, height
    horizon_y = 500  # y-coordinate of the horizon line
    merchant_rect = pygame.Rect(648, 542, 50, 55)

    # Define where the merchant will be
    ms_x = screen_width // 2 - ms_width // 2 + 200  # Doing it by starting it in the middle using // 2
    ms_y = screen_height // 2 - ms_height // 2 + 150  # Doing it by starting it in the middle using // 2

    # Define where the shop menu will be
    sm_x = screen_width // 2 - sm_width // 2
    sm_y = screen_height // 2 - sm_height // 2

    # Create our main game function that our game will be running on
    run = True

    # Our shop function
    shop = False

    # All our upgrade functions
    upgrade_1 = True
    upgrade_2 = True
    upgrade_3 = True

    # Our games function that checks if we have fished in the last frame, so we can spam the fishing button.
    fished_last_frame = False
    while run:
        # Put all the images, background images, characters, shop onto the screen in the specified x, y pos
        clock.tick(fps)  # Int the clock
        screen.blit(bg, (0, 0))  # background image
        screen.blit(ch, (ch_x, ch_y))   # character spawn
        screen.blit(ms, (ms_x, ms_y))  # merchant shop location
        screen.blit(coin, (10,8))  # coin location

        # Define fish data, Define What fish it should be rolled
        lvl2_fish_types = ["Salmon", "Tuna", "Cod", "Trout", "Shark", "Bass", "Snapper", "Whale", "Marlin", "Ray", "Pike", "Grandpa"]
        # define how rare it is to catch it
        fish_probabilities = [1000,   1000,   1000,  1000,    500,     500,      500,      20,       50,     500,    500,       1]
        # Tell the game what to do when it wants to be quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # When the game is quit
                run = False  # stop the game loop

        # Get key states, so we can access the keystrokes
        keys = pygame.key.get_pressed()

        # Get current volume of our game
        current_volume = pygame.mixer.music.get_volume()
        # Check for volume adjustment keys
        if keys[K_i]:  # Press 'I' to decrease the volume
            new_volume = max(0.0, current_volume - 0.1)  # Ensure volume doesn't go below 0.0
            pygame.mixer.music.set_volume(new_volume)
        if keys[K_o]:  # Press 'O' to increase the volume
            new_volume = min(1.0, current_volume + 0.1)  # Ensure volume doesn't go above 1.0
            pygame.mixer.music.set_volume(new_volume)

        # Move left
        if keys[K_LEFT]:  # When the left arrow is pressed
            new_x = ch_x - speed  # Code the movement, by  changing
            if new_x >= 0 and not (house_rect.collidepoint(new_x, ch_y) or
                                   left_lake_rect.collidepoint(new_x, ch_y) or
                                    merchant_rect.collidepoint(new_x, ch_y)):  # Check if the character has it any borders
                ch_x = new_x

        # Move right
        if keys[K_RIGHT]:  # When the right arrow is pressed
            new_x = ch_x + speed  # Code the movement, by  changing
            if new_x <= screen_width - ch_width and not (house_rect.collidepoint(new_x + ch_width, ch_y) or
                                                         left_lake_rect.collidepoint(new_x + ch_width, ch_y) or
                                                            merchant_rect.collidepoint(new_x + ch_width, ch_y)): # Check if the character has it any borders
                ch_x = new_x

        # Move up
        if keys[K_UP]:  # When the up arrow is pressed
            new_y = ch_y - speed  # Code the movement, by  changing
            if new_y >= 0 and new_y >= horizon_y and not (house_rect.collidepoint(ch_x, new_y) or
                                                          left_lake_rect.collidepoint(ch_x, new_y) or
                                                            merchant_rect.collidepoint(ch_x, ch_y)): # Check if the character has it any borders
                ch_y = new_y

        # Move down
        if keys[K_DOWN]:  # When the down arrow is pressed
            new_y = ch_y + speed  # Code the movement, by  changing
            if new_y <= screen_height - ch_height and not (house_rect.collidepoint(ch_x, new_y + ch_height) or
                                                           left_lake_rect.collidepoint(ch_x, new_y + ch_height) or
                                                            merchant_rect.collidepoint(ch_x, new_y + ch_height)):  # Check if the character has it any borders
                ch_y = new_y

        # Shop logic
        if keys[K_s]:  # When S is pressed set the shop to True opens it
            shop = True
        if keys[K_q] and shop:  # When Q is pressed se the shop to False closes the shop
            shop = False

        # Start the shop items an the way they work check if they have enough money for the function to run and check if the upgrade has already been bought
        if keys[K_1] and money >= 1000 and upgrade_1:
            print(f"You just bough your First upgrade! It cost 1000, your current money is: {money}")
            money -= 1000  # Take the money away
            upgrade_1 = False  # set the upgrade to false so the player cant  buy it anymore
            money_text = font.render(f"{money}", True, (255, 255, 255))  # Update the text so to the changes are shown on screen

        # When the upgrade is true display it on screen
        if upgrade_1:
            screen.blit(upgrade_1_text, (10, 50))

        if keys[K_2] and money >= 5000 and upgrade_2:
            print(f"You just bough your First upgrade! It cost 1000, your current money is: {money}")
            money -= 5000  # Take the money away
            upgrade_2 = False # set the upgrade to false so the player cant  buy it anymore
            money_text = font.render(f"{money}", True, (230, 255, 255)) # Update the text so to the changes are shown on screen

        # When the upgrade is true display it on screen
        if upgrade_2:
            screen.blit(upgrade_2_text, (10, 100))

        if keys[K_3] and money >= 10000 and upgrade_3:
            print(f"You just bough your First upgrade! It cost 1000, your current money is: {money}")
            money -= 10000  # Take the money away
            upgrade_3 = False  # set the upgrade to false so the player cant  buy it anymore
            money_text = font.render(f"{money}", True, (200, 255, 255))  # Update the text so to the changes are shown on screen

        # when the upgrade is true display it on screen
        if upgrade_3:
            screen.blit(upgrade_3_text, (10, 150))

        if shop:
            screen.blit(sm, (sm_x, sm_y))  # Adjust sm_x and sm_y for correct positioning


        if shop:
            screen.blit(sm, (sm_x, sm_y))  # Adjust sm_x and sm_y for correct positioning

        if keys[K_f]:
            if not fished_last_frame:
                fished_last_frame = True # check if we have fished in the last frame

                # Roll from the table we supplied and makesure to consider the eights of the different choices
                fish_type = random.choices(lvl2_fish_types, weights = fish_probabilities, k = 1)[0]
                money -= 1  # Take away 1 coin for fishing

                if fish_type == "Cod":  # If the option is rolled we will do the following
                    money += 2  # Add or Minus money
                    exp += 2  # Add or Minus Money
                    print(f"You caught a Cod! Your money increced by +5! Your current Money is: {(money)} Your Exp increaced! Your currrent exp is {(exp)}! Your current Lvl is {(leveling)}") #Print the action

                elif fish_type == "Tuna":  # If the option is rolled we will do the following
                    money += 5  # Add or Minus money
                    exp += 2  # Add or Minus Money
                    print(f"You caught a Tuna! Your money increced by +10! Your current Money is: {(money)}! Your Exp increaced! Your currrent exp is {(exp)}! Your current Lvl is {(leveling)}")

                elif fish_type == "Salmon":  # If the option is rolled we will do the following
                    money += 3  # Add or Minus money
                    exp += 1  # Add or Minus Money
                    print(f"You caught a Salmon! Your money increced by +7! Your current Money is: {(money)} Your Exp increaced! Your currrent exp is {(exp)}! Your current Lvl is {(leveling)}")

                elif fish_type == "Trout":  # If the option is rolled we will do the following
                    money += 1  # Add or Minus money
                    exp += 4  # Add or Minus Money
                    print(f"You caught a Trout! Your money increced by +1! Your current Money is: {(money)} Your Exp increaced! Your currrent exp is {(exp)}! Your current Lvl is {(leveling)}")

                elif fish_type == "Shark":  # If the option is rolled we will do the following
                    money -= 10  # Add or Minus money
                    exp -= 10  # Add or Minus Money
                    print(f"You caught a Shark! Your money deacreased by -10! Your current Money is: {(money)} Your Exp decreaced! Your currrent exp is {(exp)}! Your current Lvl is {(leveling)}")

                elif fish_type == "Bass":  # If the option is rolled we will do the following
                    money += 7  # Add or Minus money
                    exp += 5  # Add or Minus Money
                    print(f"You caught a Bass! Your money increced by +10! Your current Money is: {(money)} Your Exp increaced! Your currrent exp is {(exp)}! Your current Lvl is {(leveling)}")

                elif fish_type == "Snapper":  # If the option is rolled we will do the following
                    money += 7  # Add or Minus money
                    exp += 2  # Add or Minus Money
                    print(f"You caught a Snapper! Your money increced by +7! Your current Money is: {(money)} Your Exp increaced! Your currrent exp is {(exp)}! Your current Lvl is {(leveling)}")

                elif fish_type == "Whale":  # If the option is rolled we will do the following
                    money += 50  # Add or Minus money
                    exp += 50  # Add or Minus Money
                    print(f"You caught a Trout! Your money decreaced by -50! Your current Money is: {(money)} Your Exp decraced! Your currrent exp is {(exp)}! Your current Lvl is {(leveling)}")

                elif fish_type == "Marlin":  # If the option is rolled we will do the following
                    money += 20  # Add or Minus money
                    exp += 10  # Add or Minus Money
                    print(f"You caught a Trout! Your money Increaced by 20! Your current Money is: {(money)} Your Exp increaced! Your currrent exp is {(exp)}! Your current Lvl is {(leveling)}")

                elif fish_type == "Ray":  # If the option is rolled we will do the following
                    money += 5  # Add or Minus money
                    exp += 4  # Add or Minus Money
                    print(f"You caught a Trout! Your money increaced by 5! Your current Money is: {(money)} Your Exp Increaced! Your currrent exp is {(exp)}! Your current Lvl is {(leveling)}")

                elif fish_type == "Pike":  # If the option is rolled we will do the following
                    money += 9  # Add or Minus money
                    exp += 3  # Add or Minus Money
                    print(f"You caught a Trout! Your money increaced by 30! Your current Money is: {(money)} Your Exp Increaced! Your currrent exp is {(exp)}! Your current Lvl is {(leveling)}")

                elif fish_type == "Grandpa":  # If the option is rolled we will do the following
                    money += 10000  # Add or Minus money
                    exp += 100  # Add or Minus Money
                    print(f"You caught your Grandpa! Your money increaced by by 10,000! Your current Money is: {(money)} Your Exp Increaced! Your currrent exp is {(exp)}! Your current Lvl is {(leveling)}")

                else:
                    money += 0  # make sure that if nothing happens for some reason nothing will crash
                # Check if we have enough expt to lvl up
                if exp >= 300:
                    exp = 0  # reset the exp
                    leveling += 1  # add 1 level

                # Update all the font renders to update the changes made
                money_text = font.render(f"{money}", True, (255, 255, 255))  # Money
                exp_text = font.render(f"EXP:{exp}", True, (255, 255, 255))  # Exp
                leveling_text = font.render(f"LVL:{leveling}", True, (255, 255, 255))  # Leveling

        else:
            fished_last_frame = False  # if we have fished then don't run the program

        screen.blit(money_text, (50, 10))  # Position the text at (10, 10) coordinates
        screen.blit(exp_text, (500, 10))  # Position the text at (10, 10) coordinates
        screen.blit(leveling_text, (700, 10))  # Position the text at (10, 10) coordinate

        pygame.display.update()

    pygame.display.update()

    pygame.quit()
pass