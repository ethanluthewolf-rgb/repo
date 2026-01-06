# PGAME DRAWING
# Author: Lu Ethan
# Date: Jan 5, 2025

import pygame
import math

def game():
    pygame.init()

    # COLOURS - (R, G, B)
    # CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
    WHITE = (255, 255, 255)
    BLACK = (  0,   0,   0)
    RED   = (255,   0,   0)
    GREEN = (  0, 255,   0)
    BLUE  = (  0,   0, 255)
    GREY  = (128, 128, 128)

    # CONSTANTS
    WIDTH = 800
    HEIGHT = 600
    SIZE = (WIDTH, HEIGHT)

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Your Title Here")

    # Variables
    done = False
    clock = pygame.time.Clock()

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC

        # ------ DRAWING TO SCREEN
        screen.fill(WHITE) # background
        # Draw a circle
        pygame.draw.circle(screen, (255, 255, 0), (WIDTH / 2, HEIGHT / 2), 50)
        pygame.draw.arc(screen, BLACK, (WIDTH/2 - 20, HEIGHT/2, 40, 25), 3.14, 6.28, 3)
        pygame.draw.arc(screen, BLACK, (WIDTH/2 - 29, HEIGHT/2 - 20, 20, 10), 6.28, 3.14, 4)
        pygame.draw.arc(screen, BLACK, (WIDTH/2 + 12, HEIGHT/2 - 20, 20, 10), 6.28, 3.14, 4)
        pygame.draw.circle(screen, (240, 50, 110), (WIDTH / 2 - 30, HEIGHT / 2), 10)
        pygame.draw.circle(screen, (240, 50, 110), (WIDTH / 2 + 30, HEIGHT / 2), 10)
        # Update screen
        pygame.display.flip()

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60) # 60 fps

    pygame.quit()

if __name__ == "__main__":
    game()
