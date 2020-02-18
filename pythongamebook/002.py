# -*- coding: utf-8 -*-

"""The following program simplifies gimmicks and enhances unicorns."""

import os
import pygame
os.chdir('/Users/adamstrick/Documents/pythongamebook')
print(os.getcwd())
pygame.init()

# Set screen size of pygame window
screen = pygame.display.set_mode((640,480))
# Create empty pygame surface
background = pygame.Surface(screen.get_size())
# Fill the background white (RGB)
background.fill((255,255,255))
# Convert surface to make blitting faster
background = background.convert()
# Copy background to screen (position (0, 0) is upper left corner)
screen.blit(background, (0,0))
# Create Pygame clock object
clock = pygame.time.Clock()

mainloop = True
# Desired framerate in FPS.
FPS = 30
# How many seconds the "game" is played
playtime = 0.0

while mainloop:
    # Do not go faster than this framerate
    milliseconds = clock.tick(FPS)
    playtime += milliseconds / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # pygame window closed by user
            mainloop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # user pressed ESC
                mainloop = False

    # Print framerate and playtime in titlebar
    text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime)
    pygame.display.set_caption(text)

    # Update pygame display
    pygame.display.flip()

# finish pygame
pygame.quit()

# last line
print("This game was played for {0:.2f} seconds".format(playtime))