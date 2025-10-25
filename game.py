import sys
import time

import pygame
from pygame.locals import *

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 1000, 800
screen = pygame.display.set_mode((width, height))

#text specifications
font = pygame.font.Font(None, 74)

text = font.render("Immune Battle", True, (123, 252, 3))
textRect = text.get_rect()
textRect.center = (width // 2, height // 2)

text_char = font.render("Choose Your Character", True, (0,0,0))
textRect_char = text.get_rect()
textRect_char.center = (width // 2.5, height // 10)

text_path_choice = font.render("You are the PATHOGEN!", True, (0,0,0))
textRect_path = text.get_rect()
textRect_path.center = (width // 3, height // 1.5)

text_imm_choice = font.render("You are the IMMUNE SYSTEM!", True, (0,0,0))
textRect_imm = text.get_rect()
textRect_imm.center = (width // 3, height // 1.5)

#load images
gen_pathogen = pygame.image.load('HIV0001.png')
immune_sys = pygame.image.load('BIOART-409/PlasmaBCell0001-blue.png')

#create character classes
#clickable initial characters
class ClickableSprite(pygame.sprite.Sprite):
    def __init__(self,image_path,x,y):
        super().__init__()
        self.image = image_path
        self.image = pygame.transform.scale(self.image, (300,300))
        self.rect = self.image.get_rect(topleft=(x, y))
    def when_clicked(self):
        screen.blit(text_path_choice, textRect_path)

#clickable options for pathogens

#clickable options for immune system

#pathogen classes

#immune system classes


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

character_screen = True
current_choice = ''
while character_screen:
    screen.fill((255,255,255))
    screen.blit(text_char, textRect_char)
    pathogen = ClickableSprite(gen_pathogen,100,200)
    immune_system = ClickableSprite(immune_sys, 500, 200)
    screen.blit(pathogen.image,pathogen.rect)
    screen.blit(immune_system.image,immune_system.rect)
    if current_choice == 'pathogen':
        screen.blit(text_path_choice, textRect_path)
    if current_choice == 'immune':
        screen.blit(text_imm_choice, textRect_path)
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pathogen.rect.collidepoint(event.pos):
                    pathogen.when_clicked()
                    current_choice = 'pathogen'
                if immune_system.rect.collidepoint(event.pos):
                    immune_system.when_clicked()
                    current_choice = 'immune'
            if event.type == KEYDOWN:
                character_screen = False
    
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
