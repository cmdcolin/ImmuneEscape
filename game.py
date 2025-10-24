import sys

import pygame
from pygame.locals import *

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

font = pygame.font.Font(None, 74)
text = font.render("Immune Battle", True, (255, 255, 255))
textRect = text.get_rect()
textRect.center = (width // 2, height // 2)

start_screen = True
while start_screen:
    screen.fill((0, 0, 0))
    screen.blit(text, textRect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            start_screen = False

    pygame.display.flip()
    fpsClock.tick(fps)


# Game loop.
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update.

    # Draw.

    pygame.display.flip()
    fpsClock.tick(fps)
