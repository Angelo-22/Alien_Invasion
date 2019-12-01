import sys

import pygame

from settings import Settings

def run_game():
    # Initilize pygame, settings,  and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # set the background color, as RGB. (255, 0, 0) is red, (0, 255, 0) is green, and (0, 0, 255) is blue.
    #bg_color = (230, 230, 230)

    # start the main loop for the game
    while True:

        # watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)
        
        # make the most recently drawn screen visible
        pygame.display.flip()

run_game()
