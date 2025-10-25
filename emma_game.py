import sys
import time

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

text_pathogen = font.render("Choose Your PATHOGEN", True, (255,255,255))
textRect_pathogen = text.get_rect()
textRect_pathogen.center = (500, height // 10)

text_immune = font.render("Choose Your IMMUNE SYSTEM", True, (0,0,0))
textRect_immune = text.get_rect()
textRect_immune.center = (450, height // 10)

text_innate = font.render("INNATE", True, (0,0,0))
textRect_innate = text.get_rect()
textRect_innate.center = (200, 600)

text_adaptive = font.render("ADAPTIVE", True, (0,0,0))
textRect_adaptive = text.get_rect()
textRect_adaptive.center = (700, 600)


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

#create character classes
#clickable initial characters
class ClickableSprite(pygame.sprite.Sprite):
    def __init__(self,image_path,x,y):
        super().__init__()
        self.image = image_path
        self.image = pygame.transform.scale(self.image, (300,300))
        self.rect = self.image.get_rect(topleft=(x, y))
    def when_clicked(self):
        screen.blit(text_path_choice, textRect_path.center)

#clickable options for pathogens

#clickable options for immune system

#pathogen classes
class Virus:
    def __init__(self,image_path,x,y):
        super().__init__()
        self.image = image_path
        self.image = pygame.transform.scale(self.image, (300,300))
        self.rect = self.image.get_rect(topleft=(x,y))
        self.name = 'Virus'
        self.health = 80
        self.max_health = 80
        self.x = x
        self.y = y
    def draw(self,surface):
        #display name and health
        name_text = font.render(self.name, True,BLACK)
        health_text = font.render(f'{self.health} / {self.max_health}', True, BLACK)
        surface.blit(name_text,self.x,self.y)
        surface.blit(health_text,self.x,self.y+40)
        #display a rectangle visual showing health
        pygame.draw.rect(surface, RED,self.x,self.y+70,200,20)
        current_health_width = (self.health/self.max_health)*200
        pygame.draw.rect(surface, BLUE, (self.x, self.y + 70, current_health_width, 20))


#immune system classes

#draw screen statuses
def draw_start_screen():
    screen.fill((0, 0, 0))
    screen.blit(text, textRect)

def draw_character_screen():
    screen.fill((255,255,255))
    screen.blit(text_char, textRect_char)

def draw_pathogen_screen():
    screen.blit(pathogen_background, (0, 0))
    virus = ClickableSprite(virus_image, 100, 300)
    bacteria = ClickableSprite(bacteria_image, 500, 300)
    parasite = ClickableSprite(parasite_image, 900,300)
    screen.blit(virus.image,virus.rect)
    screen.blit(bacteria.image,bacteria.rect)
    screen.blit(parasite.image,parasite.rect)
    screen.blit(text_virus_choice, textRect_virus)
    screen.blit(text_bacteria_choice, textRect_bacteria)
    screen.blit(text_parasite_choice, textRect_parasite)
    screen.blit(text_pathogen, textRect_pathogen)

def draw_immune_screen():
    screen.blit(immune_background, (0,0))
    innate = ClickableSprite(innate_image, 200, 300)
    adaptive = ClickableSprite(adaptive_image, 700, 300)
    screen.blit(innate.image,innate.rect)
    screen.blit(adaptive.image,adaptive.rect)
    screen.blit(text_immune, textRect_immune)
    screen.blit(text_innate, textRect_innate)
    screen.blit(text_adaptive, textRect_adaptive)

#game states
start_screen = 0
character_screen = 1
pathogen_screen = 2
immune_screen = 3

#start screen
current_state = start_screen
while current_state == start_screen:
    draw_start_screen()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            current_state = character_screen

    pygame.display.flip()
    fpsClock.tick(fps)

#character screen
character_screen = True
current_choice = ''
timer = pygame.time.get_ticks()
while current_state == character_screen:
    draw_character_screen()
    pathogen = ClickableSprite(gen_pathogen,200,200)
    immune_system = ClickableSprite(immune_sys, 700,200)
    screen.blit(pathogen.image,pathogen.rect)
    screen.blit(immune_system.image,immune_system.rect)
    if current_choice == 'pathogen':
        if pygame.time.get_ticks() - timer < 2000:
            screen.blit(text_path_choice, textRect_path)
        if pygame.time.get_ticks() - timer >= 2000:
            current_state = pathogen_screen
    if current_choice == 'immune':
        if pygame.time.get_ticks() - timer < 2000:
            screen.blit(text_imm_choice, textRect_imm)
        if pygame.time.get_ticks() - timer >= 2000:
            current_state = immune_screen
    for event in pygame.event.get():
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


    pygame.display.flip()
    fpsClock.tick(fps)

#pathogen screen
while current_state == pathogen_screen:
    draw_pathogen_screen()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.flip()
    fpsClock.tick(fps)

#immune system screen
while current_state == immune_screen:
    draw_immune_screen()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.flip()
    fpsClock.tick(fps)



fight_screen = True
while fight_screen:
    screen.fill((YELLOW))
    player_1 = Virus(gen_pathogen,50,200)
    player_1.draw(screen)

    
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    
    pygame.display.flip()
    fpsClock.tick(fps)
