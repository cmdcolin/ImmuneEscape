import sys
import time
import csv
from dict_of_dict import *

import pygame
from pygame.locals import *

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 1200, 800
screen = pygame.display.set_mode((width, height))

#text specifications
font = pygame.font.Font(None, 74)

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (0,255,0)

#text that appears in the game
text = font.render("Immune Battle", True, (123, 252, 3))
textRect = text.get_rect()
textRect.center = (width // 2, height // 2)

text_char = font.render("Choose Your Character", True, (0,0,0))
textRect_char = text.get_rect()
textRect_char.center = (500, height // 10)

text_path_choice = font.render('You are the PATHOGEN!', True, (0,0,0))
textRect_path = text.get_rect()
textRect_path.center = (500, height // 1.5)

text_imm_choice = font.render('You are the IMMUNE SYSTEM!', True, (0,0,0))
textRect_imm = text.get_rect()
textRect_imm.center = (450, height // 1.5)

text_virus_choice = font.render('VIRUS', True, (255,255,255))
textRect_virus = text.get_rect()
textRect_virus = (150, 600)

text_bacteria_choice = font.render('BACTERIA', True, (255,255,255))
textRect_bacteria = text.get_rect()
textRect_bacteria = (500, 600)

text_parasite_choice = font.render('PARASITE', True, (255,255,255))
textRect_parasite = text.get_rect()
textRect_parasite = (900, 600)

text_p2 = font.render("Choose Player Two", True, (255,255,255))
textRect_p2 = text.get_rect()
textRect_p2.center = (500, height // 10)

text_p1 = font.render("Choose Player One", True, (255,255,255))
textRect_p1 = text.get_rect()
textRect_p1.center = (450, height // 10)

text_innate = font.render("INNATE", True, (0,0,0))
textRect_innate = text.get_rect()
textRect_innate.center = (200, 600)

text_adaptive = font.render("ADAPTIVE", True, (0,0,0))
textRect_adaptive = text.get_rect()
textRect_adaptive.center = (700, 600)


#import character dictionaries
immune_dict = create_dict_of_dict('immune.txt','Immune_Name')
pathogen_dict = create_dict_of_dict('pathogen.txt','Pathogen_Name')

#load images
gen_pathogen = pygame.image.load('data/HIV0001.png')
immune_sys = pygame.image.load('data/PlasmaBCell0001-blue.png')
bacteria_image = pygame.image.load('data/GramNegativeBacteria0001.png')
virus_image = pygame.image.load('data/SARSCoV20003-purple.png')
parasite_image = pygame.image.load('data/TrypanosomaCruzi0001.png')
pathogen_background = pygame.image.load('data/dark_image.jpg')
pathogen_background = pygame.transform.scale(pathogen_background, (width, height))
innate_image = pygame.image.load('data/NeutrophilNetosis0001.png')
adaptive_image = pygame.image.load('data/BCellWithIgM0001.png')
immune_background = pygame.image.load('data/light_blue_background.jpg')
immune_background = pygame.transform.scale(immune_background, (width,height))
fight_background = pygame.image.load('data/blood.jpeg')
fight_background = pygame.transform.scale(fight_background, (width,height))
for key in immune_dict:
    immune_dict[key]['Loaded_Image'] = pygame.image.load(immune_dict[key]['Image'])
    immune_dict[key]['Loaded_Image'] = pygame.transform.scale(immune_dict[key]['Loaded_Image'], (300,300))
for key in pathogen_dict:
    pathogen_dict[key]['Loaded_Image'] = pygame.image.load(pathogen_dict[key]['Image'])
    pathogen_dict[key]['Loaded_Image'] = pygame.transform.scale(pathogen_dict[key]['Loaded_Image'], (300,300))


#create character classes
#clickable characters
class ClickableSprite(pygame.sprite.Sprite):
    def __init__(self,image_path,x,y):
        super().__init__()
        self.image = image_path
        self.image = pygame.transform.scale(self.image, (300,300))
        self.rect = self.image.get_rect(topleft=(x, y))
    def when_clicked(self):
        screen.blit(text_path_choice, textRect_path.center)


#draw screen statuses
def draw_start_screen():
    screen.fill((0, 0, 0))
    screen.blit(text, textRect)

def draw_character_screen():
    screen.fill((255,255,255))
    screen.blit(text_char, textRect_char)

def draw_pathogen_screen():
    screen.blit(pathogen_background, (0, 0))
    screen.blit(text_virus_choice, textRect_virus)
    screen.blit(text_bacteria_choice, textRect_bacteria)
    screen.blit(text_parasite_choice, textRect_parasite)

def draw_immune_screen():
    screen.blit(immune_background, (0,0))
    screen.blit(text_innate, textRect_innate)
    screen.blit(text_adaptive, textRect_adaptive)

def draw_fight_screen():
    screen.blit(fight_background, (0,0))

#game states
start_screen = 0
character_screen = 1
pathogen_screen = 2
immune_screen = 3
fight_screen = 4

#choices to set blank
current_choice = ''

#starting game loop
running = True
current_state = start_screen
timer = pygame.time.get_ticks()
transition_time = 0
#start screen
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if current_state == start_screen:
        draw_start_screen()
        for event in events:
            if event.type == KEYDOWN:
                current_state = character_screen
    if current_state == character_screen:
        draw_character_screen()
        pathogen = ClickableSprite(gen_pathogen,200,200)
        immune_system = ClickableSprite(immune_sys, 700,200)
        screen.blit(pathogen.image,pathogen.rect)
        screen.blit(immune_system.image,immune_system.rect)
        if current_choice == 'pathogen':
            if pygame.time.get_ticks() - timer < 2000:
                screen.blit(text_path_choice, textRect_path)
            if pygame.time.get_ticks() - timer >= 2000:
                player_1_assigned = ''
                player_2_assigned = ''
                current_state = pathogen_screen
        if current_choice == 'immune':
            if pygame.time.get_ticks() - timer < 2000:
                screen.blit(text_imm_choice, textRect_imm)
            if pygame.time.get_ticks() - timer >= 2000:
                player_1_assigned = ''
                player_2_assigned = ''
                current_state = immune_screen
        for event in events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pathogen.rect.collidepoint(event.pos):
                        current_choice = 'pathogen'
                        pathogen.when_clicked
                        timer = pygame.time.get_ticks()
                    if immune_system.rect.collidepoint(event.pos):
                        immune_system.when_clicked()
                        current_choice = 'immune'
                        timer = pygame.time.get_ticks()
    if current_state == pathogen_screen:
        draw_pathogen_screen()
        virus = ClickableSprite(virus_image, 100, 300)
        bacteria = ClickableSprite(bacteria_image, 500, 300)
        parasite = ClickableSprite(parasite_image, 900,300)
        all_pathogen_sprites = virus, bacteria, parasite
        screen.blit(virus.image,virus.rect)
        screen.blit(bacteria.image,bacteria.rect)
        screen.blit(parasite.image,parasite.rect)
        if pygame.time.get_ticks() - transition_time < 50:
            continue
        if player_1_assigned == '':
            screen.blit(text_p1, textRect_p1)
        if player_1_assigned != '':
            screen.blit(text_p2, textRect_p2)
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for character in all_pathogen_sprites:
                    if character.rect.collidepoint(mouse_pos):
                        if player_1_assigned == '':
                            if character == virus:
                                player_1_assigned = pathogen_dict['Virus']
                            if character == bacteria:
                                player_1_assigned = pathogen_dict['Bacteria']
                            if character == parasite:
                                player_1_assigned = pathogen_dict['Parasite']
                            current_state = immune_screen
                            transition_time = pygame.time.get_ticks()
                        else:
                            if character == virus:
                                player_2_assigned = pathogen_dict['Virus']
                            if character == bacteria:
                                player_2_assigned = pathogen_dict['Bacteria']
                            if character == parasite:
                                player_2_assigned = pathogen_dict['Parasite']
                            current_state = fight_screen
    if current_state == immune_screen:
        draw_immune_screen()
        innate = ClickableSprite(innate_image, 200, 300)
        adaptive = ClickableSprite(adaptive_image, 700, 300)
        all_immune_sprites = innate, adaptive
        screen.blit(innate.image,innate.rect)
        screen.blit(adaptive.image,adaptive.rect)
        if pygame.time.get_ticks() - transition_time < 50:
            continue
        if player_1_assigned == '':
            screen.blit(text_p1, textRect_p1)
        if player_1_assigned != '':
            screen.blit(text_p2, textRect_p2)
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for character in all_immune_sprites:
                    if character.rect.collidepoint(mouse_pos):
                        if player_1_assigned == '':
                            if character == innate:
                                player_1_assigned = immune_dict['Innate']
                            if character == adaptive:
                                player_1_assigned = immune_dict['Adaptive']
                            current_state = pathogen_screen
                            transition_time = pygame.time.get_ticks()
                        else:
                            if character == innate:
                                player_2_assigned = immune_dict['Innate']
                            if character == adaptive:
                                player_2_assigned = immune_dict['Adaptive']
                            current_state = fight_screen
    if current_state == fight_screen:
        draw_fight_screen()
        player_1_rect = (100,300)
        player_2_rect = (800,300)
        screen.blit(player_1_assigned['Loaded_Image'],player_1_rect)
        screen.blit(player_2_assigned['Loaded_Image'],player_2_rect)


    
    pygame.display.flip()
    fpsClock.tick(fps)