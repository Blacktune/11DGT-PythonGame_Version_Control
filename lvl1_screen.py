import pygame
from pygame.locals import *
import random
from pygame import *


def lvl1_screen():
    pygame.init()

    clock = pygame.time.Clock()
    fps = 60
    # Define the font for the game

    font = pygame.font.SysFont('Baus 93', 60)

    global money
    money = 16000
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





    # Set screen width and height
    screen_width = 936
    screen_height = 864

    # Set character height and width
    ch_height = 50
    ch_width = 50

    #Set Merchant height
    ms_height = 100
    ms_width = 100

    #set shop menu height
    sm_height = 500
    sm_width = 300

    #set coin size
    coin_height = 40
    coin_width = 40

    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("The Fishing Mystery")

    pygame.mixer.init()  # initialize the mixer
    pygame.mixer.music.stop()  # stop the previous song muisic

    # Load and play the song
    pygame.mixer.music.load('sound.mp3/lvl1_song.mp3')
    pygame.mixer.music.play(-1)

    # Set initial volume to 1.0 (full volume)
    pygame.mixer.music.set_volume(1.0)

    # Create our background image for our game
    bg = pygame.image.load('img/th.png')
    bg = pygame.transform.scale(bg, (screen_width, screen_height))  # resizes the image to fill the screen

    # Create our playable character
    ch = pygame.image.load('img/Fishing_Character-removebg-preview.png')
    ch = pygame.transform.scale(ch, (ch_width, ch_height))

    # create our coin image
    coin = pygame.image.load('img/coin.png')
    coin = pygame.transform.scale(coin, (coin_width, coin_height))

    # create our Merchant
    ms = pygame.image.load('img/shop.png')
    ms = pygame.transform.scale(ms,(ms_width, ms_height))

    # create our shop menu
    sm = pygame.image.load('img/download.png')
    sm = pygame.transform.scale(sm, (sm_width,sm_height))



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

    #define where the shop menue will be
    sm_x = screen_width // 2 - sm_width // 2
    sm_y = screen_height // 2 - sm_height // 2

    # Create a screen that our game will be running on
    run = True
    shop = False
    upgrade_1 = True
    upgrade_2 = True
    upgrade_3 = True


    fish_cooldown = 0
    fished_last_frame = False
    while run:
        clock.tick(fps)
        screen.blit(bg, (0, 0))
        screen.blit(ch, (ch_x, ch_y))
        screen.blit(ms, (ms_x, ms_y))
        screen.blit(coin, (10,8))


        # Define fish data
        lvl2_fish_types = ["Salmon", "Tuna", "Cod", "Trout", "Shark", "Bass", "Snapper", "Whale", "Marlin", "Ray", "Pike", "Goldfish"]
        fish_probabilities = [1000,   1000,   1000,  1000,    500,     500,      500,      20,       50,     500,    500,       1]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        # Get key states
        keys = pygame.key.get_pressed()

        # Get current volume
        current_volume = pygame.mixer.music.get_volume()
        # Check for volume adjustment keys
        if keys[K_i]:  # Press 'I' to decrease the volume
            new_volume = max(0.0, current_volume - 0.1)  # Ensure volume doesn't go below 0.0
            pygame.mixer.music.set_volume(new_volume)
        if keys[K_o]:  # Press 'O' to increase the volume
            new_volume = min(1.0, current_volume + 0.1)  # Ensure volume doesn't go above 1.0
            pygame.mixer.music.set_volume(new_volume)

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

                # Shop logic
        if keys[K_s]:
            shop = True
        if keys[K_q] and shop:
            shop = False


         #Start the shop items an the way they work check if they have enough money for the function to run and check if the upgrade has already been bought
        if keys[K_1] and money >= 1000 and upgrade_1:
            print(f"You just bough your First upgrade! It cost 1000, your current money is: {money}")
            money -= 1000
            upgrade_1 = False
            money_text = font.render(f"{money}", True, (255, 255, 255))

        if upgrade_1:
            screen.blit(upgrade_1_text, (10, 50))

        if keys[K_2] and money >= 5000 and upgrade_2:
            print(f"You just bough your First upgrade! It cost 1000, your current money is: {money}")
            money -= 5000
            upgrade_2 = False
            money_text = font.render(f"{money}", True, (230, 255, 255))

        if upgrade_2:
            screen.blit(upgrade_2_text, (10, 100))

        if keys[K_3] and money >= 10000 and upgrade_3:
            print(f"You just bough your First upgrade! It cost 1000, your current money is: {money}")
            money -= 10000
            upgrade_3 = False
            money_text = font.render(f"{money}", True, (200, 255, 255))

        if upgrade_3:
            screen.blit(upgrade_3_text, (10, 150))

        if shop:
            screen.blit(sm, (sm_x, sm_y))  # Adjust sm_x and sm_y for correct positioning


        if shop:
            screen.blit(sm, (sm_x, sm_y))  # Adjust sm_x and sm_y for correct positioning

        if keys[K_f]:
            if not fished_last_frame:
                fished_last_frame = True

                fish_type = random.choices(lvl2_fish_types, weights = fish_probabilities, k = 1)[0]
                money -= 1

                if fish_type == "Cod":
                    money += 2
                    exp += 2
                    print(f"You caught a Cod! Your money increced by +5! Your current Money is: {(money)} Your Exp increaced! Your currrent exp is {(exp)}! Your current Lvl is {(leveling)}")


                elif fish_type == "Tuna":
                    money += 5
                    exp += 2
                    print(f"You caught a Tuna! Your money increced by +10! Your current Money is: {(money)}! Your Exp increaced! Your currrent exp is {(exp)}! Your current Lvl is {(leveling)}")
                elif fish_type == "Salmon":
                    money += 3
                    exp += 1
                    print(f"You caught a Salmon! Your money increced by +7! Your current Money is: {(money)} Your Exp increaced! Your currrent exp is {(exp)}! Your current Lvl is {(leveling)}")
                elif fish_type == "Trout":
                    money += 1
                    exp += 4
                    print(f"You caught a Trout! Your money increced by +1! Your current Money is: {(money)} Your Exp increaced! Your currrent exp is {(exp)}! Your current Lvl is {(leveling)}")

                elif fish_type == "Shark":
                    money -= 10
                    exp -= 10
                    print(f"You caught a Shark! Your money deacreased by -10! Your current Money is: {(money)} Your Exp decreaced! Your currrent exp is {(exp)}! Your current Lvl is {(leveling)}")
                elif fish_type == "Bass":
                    money += 7
                    exp += 5
                    print(f"You caught a Bass! Your money increced by +10! Your current Money is: {(money)} Your Exp increaced! Your currrent exp is {(exp)}! Your current Lvl is {(leveling)}")
                elif fish_type == "Snapper":
                    money += 7
                    exp += 2
                    print(f"You caught a Snapper! Your money increced by +7! Your current Money is: {(money)} Your Exp increaced! Your currrent exp is {(exp)}! Your current Lvl is {(leveling)}")
                elif fish_type == "Whale":
                    money += 50
                    exp += 50
                    print(f"You caught a Trout! Your money decreaced by -50! Your current Money is: {(money)} Your Exp decraced! Your currrent exp is {(exp)}! Your current Lvl is {(leveling)}")
                elif fish_type == "Marlin":
                    money += 20
                    exp += 10
                    print(
                        f"You caught a Trout! Your money Increaced by 20! Your current Money is: {(money)} Your Exp increaced! Your currrent exp is {(exp)}! Your current Lvl is {(leveling)}")
                elif fish_type == "Ray":
                    money += 5
                    exp += 4
                    print(
                        f"You caught a Trout! Your money increaced by 5! Your current Money is: {(money)} Your Exp Increaced! Your currrent exp is {(exp)}! Your current Lvl is {(leveling)}")
                elif fish_type == "Pike":
                    money += 9
                    exp += 3
                    print(
                        f"You caught a Trout! Your money increaced by 30! Your current Money is: {(money)} Your Exp Increaced! Your currrent exp is {(exp)}! Your current Lvl is {(leveling)}")
                elif fish_type == "Goldfish":
                    money += 10000
                    exp += 100
                    print(
                        f"You caught a Goldfish! Your money Increaced by by 10,000! Your current Money is: {(money)} Your Exp Increaced! Your currrent exp is {(exp)}! Your current Lvl is {(leveling)}")

                else:
                    money += 0
                if exp >= 300:
                    exp = 0
                    leveling += 1

                money_text = font.render(f"{money}", True, (255, 255, 255))
                exp_text = font.render(f"EXP:{exp}", True, (255, 255, 255))
                leveling_text = font.render(f"LVL:{leveling}", True, (255, 255, 255))

        else:
            fished_last_frame = False

        screen.blit(money_text, (50, 10))  # Position the text at (10, 10) coordinates
        screen.blit(exp_text, (500, 10))  # Position the text at (10, 10) coordinates
        screen.blit(leveling_text, (700, 10))  # Position the text at (10, 10) coordinate

        pygame.display.update()

    pygame.display.update()

    pygame.quit()
pass