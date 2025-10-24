#!/usr/bin/env python3

import sys

import pygame
from pygame.locals import *

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 1000, 800
screen = pygame.display.set_mode((width, height))

font = pygame.font.Font(None, 74)
text = font.render("Immune Battle", True, (123, 252, 3))
textRect = text.get_rect()
textRect.center = (width // 2, height // 2)

text2 = font.render("Choose your character", True, (123, 252, 3))
textRect2 = text2.get_rect()
textRect2.center = (width // 2, height // 10)

object_image = pygame.image.load('virus.png')
object_rect = object_image.get_rect(center=(width // 2, height // 2))

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

second_screen = True
while second_screen:
    screen.fill((250, 250, 250))
    screen.blit(text2, textRect2)
    screen.blit(object_image, object_rect)

    for event in pygame.event.get():
            if event.key == pygame.K_r:
                pygame.quit()
                
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            second_screen = False

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