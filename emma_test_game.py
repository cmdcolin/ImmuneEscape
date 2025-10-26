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

#import character dictionaries
immune_dict = create_dict_of_dict('immune.txt','Immune_Name')
pathogen_dict = create_dict_of_dict('pathogen.txt','Pathogen_Name')

#text specifications
font = pygame.font.Font(None, 74)

font_large=pygame.font.SysFont(None, 60)
font_medium = pygame.font.SysFont(None,40)
font_small = pygame.font.SysFont(None, 30)

button_font = pygame.font.SysFont(None, 50)

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (0,255,0)


#text that appears in the game
text = font.render("Immune Battle", True, (123, 252, 3))
textRect = text.get_rect()
textRect.center = (width // 2, height // 2)

text_char = font.render("Player One: Choose Your Character", True, (0,0,0))
textRect_char = text.get_rect()
textRect_char.center = (350, height // 10)

text_path_choice = font.render('You are the PATHOGEN!', True, (0,0,0))
textRect_path = text.get_rect()
textRect_path.center = (500, height // 1.3)

text_imm_choice = font.render('You are the IMMUNE SYSTEM!', True, (0,0,0))
textRect_imm = text.get_rect()
textRect_imm.center = (450, height // 1.3)

text_virus_choice = font.render('VIRUS', True, (255,255,255))
textRect_virus = text.get_rect()
textRect_virus = (150, 650)

text_bacteria_choice = font.render('BACTERIA', True, (255,255,255))
textRect_bacteria = text.get_rect()
textRect_bacteria = (500, 650)

text_parasite_choice = font.render('PARASITE', True, (255,255,255))
textRect_parasite = text.get_rect()
textRect_parasite = (900, 650)

text_p2 = font.render("Choose Player Two", True, (255,255,255))
textRect_p2 = text.get_rect()
textRect_p2.center = (550, height // 10)

text_p1 = font.render("Choose Player One", True, (255,255,255))
textRect_p1 = text.get_rect()
textRect_p1.center = (550, height // 10)

text_innate = font.render("INNATE", True, (255,255,255))
textRect_innate = text.get_rect()
textRect_innate.center = (450, 650)

text_adaptive = font.render("ADAPTIVE", True, (255,255,255))
textRect_adaptive = text.get_rect()
textRect_adaptive.center = (900, 650)

# Multi-line text to display
text = "\nWelcome to ImmuneEscape!\n\n\n\n\n\n\n\n\n\n\n\nWhere the outcomes is literally life or death\n PLAY AT YOUR OWN RISK"
path_text = "Pathogen Wins!\n\nCongratulations you've\nsurvived ImmuneEscape!\nThank you for playing\n\nThis was as an Anastasia, Emma\nWalter, & Colin Production"
imm_text = "Immune System Wins!\n\nCongratulations you've\nsurvived ImmuneEscape!\nThank you for playing\n\nThis was as an Anastasia, Emma,\nWalter, & Colin Production"

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
immune_background = pygame.image.load('data/Immunity2.jpg')
immune_background = pygame.transform.scale(immune_background, (width,height))
fight_background = pygame.image.load('data/blood.jpeg')
fight_background = pygame.transform.scale(fight_background, (width,height))
background_image = pygame.image.load('data/Immune battle.jpg').convert()
background_image = pygame.transform.scale(background_image, (width, height))
for key in immune_dict:
    immune_dict[key]['Loaded_Image'] = pygame.image.load(immune_dict[key]['Image'])
    immune_dict[key]['Loaded_Image'] = pygame.transform.scale(immune_dict[key]['Loaded_Image'], (300,300))
for key in pathogen_dict:
    pathogen_dict[key]['Loaded_Image'] = pygame.image.load(pathogen_dict[key]['Image'])
    pathogen_dict[key]['Loaded_Image'] = pygame.transform.scale(pathogen_dict[key]['Loaded_Image'], (300,300))


# We can add sound to play in
sound = pygame.mixer.Sound('data/dramatic.wav')
doomsound = pygame.mixer.Sound('data/doom.wav')
Success_sound = pygame.mixer.Sound('data/Success.mp3')

sound.play(-1, 0)


#create character classes
#clickable characters
class ClickableSprite(pygame.sprite.Sprite):
    def __init__(self,image_path,x,y):
        super().__init__()
        self.image = image_path
        self.image = pygame.transform.scale(self.image, (300,300))
        self.rect = self.image.get_rect(topleft=(x, y))


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
    

#add a label here
def render_text_button(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if x is None:
        text_rect.center = (screen.get_width() // 2, y)
    else:
        text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

#function for handling player turns and drawing the fight screen (defines the fight screen)
message = ''
message_timer = 0
MESSAGE_DURATION = 200
clock = pygame.time.Clock()
def handle_player_turn(player,opponent):
    global player1_health, player2_health, total_turns, message_timer, message
    #defining the appearance of the screen
    screen.blit(fight_background, (0,0))
    render_text_button(f" {player_1_assigned['Name']}: {player1_health}", font_small, (255, 255, 255), 20, 120)
    render_text_button(f"{player_2_assigned['Name']}: {player2_health}", font_small, (255, 255, 255), 800, 120)
    render_text_button("Choose your action:", font_medium, (255, 255, 255), 450, 200)
    player1_first_rect = render_text_button(f"a:{player_1_assigned['Action'][0]}", font_medium, (255, 0, 0), 100, 600) # Red
    player1_second_rect = render_text_button(f"s:{player_1_assigned['Action'][1]}", font_medium, (0, 255, 0), 100, 650) # Green
    player1_thrid_rect = render_text_button(f"d:{player_1_assigned['Action'][2]}", font_medium,(0,200,255), 100, 700)
    player2_first_rect = render_text_button(f"UP:{player_2_assigned['Action'][0]}", font_medium, (255, 0, 0), 700, 600) # Red
    player2_second_rect = render_text_button(f"DOWN:{player_2_assigned['Action'][1]}", font_medium, (0, 255, 0), 700, 650) # Green
    player2_thrid_rect = render_text_button(f"LEFT:{player_2_assigned['Action'][2]}", font_medium,(0,200,255), 700, 700)
    screen.blit(player_1_assigned['Loaded_Image'],player_1_rect)
    screen.blit(player_2_assigned['Loaded_Image'],player_2_rect)
    pygame.display.flip()

    #turn based loops
    isturnover = False
    while not isturnover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if current_turn == 1:
                    if event.key == pygame.K_a:
                        damage = int(player_1_assigned['Damage'][0])
                        if damage >= 1:
                            if total_turns < 5:
                                player2_health -= damage
                            if 5 <= total_turns < 11:
                                if player_1_assigned['Name'] == 'Adaptive Immune System':
                                    damage = damage + 2
                                    player2_health -= damage
                                else:
                                    damage = damage - 1
                                    player2_health -= damage
                            if total_turns >= 11:
                                if player_1_assigned['Name'] == 'Adaptive Immune System':
                                    damage = damage +3
                                    player2_health -= damage
                                else:
                                    damage = damage - 2
                                    player2_health -= damage
                            message = f"{player_1_assigned['Name']} dealt {damage} damage!"
                        else:
                            player1_health -= damage
                            message = f"{player_1_assigned['Name']} healed {abs(damage)} HP!"
                        message_timer = pygame.time.get_ticks()
                        isturnover = True
                    elif event.key == pygame.K_s:
                        damage = int(player_1_assigned['Damage'][1])
                        if damage >= 1:
                            if total_turns < 5:
                                player2_health -= damage
                            if 5 <= total_turns < 11:
                                if player_1_assigned['Name'] == 'Adaptive Immune System':
                                    damage = damage + 2
                                    player2_health -= damage
                                else:
                                    damage = damage - 1
                                    player2_health -= damage
                            if total_turns >= 11:
                                if player_1_assigned['Name'] == 'Adaptive Immune System':
                                    damage = damage +3
                                    player2_health -= damage
                                else:
                                    damage = damage - 2
                                    player2_health -= damage
                            message = f"{player_1_assigned['Name']} dealt {damage} damage!"
                        else:
                            player1_health -= damage
                            message = f"{player_1_assigned['Name']} healed {abs(damage)} HP!"
                        message_timer = pygame.time.get_ticks()
                        isturnover = True
                    elif event.key == pygame.K_d:
                        damage = int(player_1_assigned['Damage'][2])
                        if damage >= 1:
                            if total_turns < 5:
                                player2_health -= damage
                            if 5 <= total_turns < 11:
                                if player_1_assigned['Name'] == 'Adaptive Immune System':
                                    damage = damage + 2
                                    player2_health -= damage
                                else:
                                    damage = damage - 1
                                    player2_health -= damage
                            if total_turns >= 11:
                                if player_1_assigned['Name'] == 'Adaptive Immune System':
                                    damage = damage +3
                                    player2_health -= damage
                                else:
                                    damage = damage - 2
                                    player2_health -= damage
                            message = f"{player_1_assigned['Name']} dealt {damage} damage!"
                        else:
                            player1_health -= damage
                            message = f"{player_1_assigned['Name']} healed {abs(damage)} HP!"
                        message_timer = pygame.time.get_ticks()
                        isturnover = True
                elif current_turn == 2:
                    if event.key == pygame.K_UP:
                        damage = int(player_2_assigned['Damage'][0])
                        if damage >= 1:
                            if total_turns < 5:
                                player1_health -= damage
                            if 5 <= total_turns < 11:
                                if player_2_assigned['Name'] == 'Adaptive Immune System':
                                    damage = damage + 2
                                    player1_health -= damage
                                else:
                                    damage = damage - 1
                                    player1_health -= damage
                            if total_turns >= 11:
                                if player_2_assigned['Name'] == 'Adaptive Immune System':
                                    damage = damage +3
                                    player1_health -= damage
                                else:
                                    damage = damage - 2
                                    player1_health -= damage
                            message = f"{player_2_assigned['Name']} dealt {damage} damage!"
                        else:
                            player2_health -= damage
                            message = f"{player_2_assigned['Name']} healed {abs(damage)} HP!"
                        message_timer = pygame.time.get_ticks()
                        isturnover = True
                    elif event.key == pygame.K_DOWN:
                        damage = int(player_2_assigned['Damage'][1])
                        if damage >= 1:
                            if total_turns < 5:
                                player1_health -= damage
                            if 5 <= total_turns < 11:
                                if player_2_assigned['Name'] == 'Adaptive Immune System':
                                    damage = damage + 2
                                    player1_health -= damage
                                else:
                                    damage = damage - 1
                                    player1_health -= damage
                            if total_turns >= 11:
                                if player_2_assigned['Name'] == 'Adaptive Immune System':
                                    damage = damage +3
                                    player1_health -= damage
                                else:
                                    damage = damage - 2
                                    player1_health -= damage
                            message = f"{player_2_assigned['Name']} dealt {damage} damage!"
                        else:
                            player2_health -= damage
                            message = f"{player_2_assigned['Name']} healed {abs(damage)} HP!"
                        message_timer = pygame.time.get_ticks()
                        isturnover = True
                    elif event.key == pygame.K_LEFT:
                        damage = int(player_2_assigned['Damage'][2])
                        if damage >= 1:
                            if total_turns < 5:
                                player1_health -= damage
                            if 5 <= total_turns < 11:
                                if player_2_assigned['Name'] == 'Adaptive Immune System':
                                    damage = damage + 2
                                    player1_health -= damage
                                else:
                                    damage = damage - 1
                                    player1_health -= damage
                            if total_turns >= 11:
                                if player_2_assigned['Name'] == 'Adaptive Immune System':
                                    damage = damage +3
                                    player1_health -= damage
                                else:
                                    damage = damage - 2
                                    player1_health -= damage
                            message = f"{player_2_assigned['Name']} dealt {damage} damage!"
                        else:
                            player2_health -= damage
                            message = f"{player_2_assigned['Name']} healed {abs(damage)} HP!"
                        message_timer = pygame.time.get_ticks()
                        isturnover = True
            if current_turn == 1:
                render_text_button(f"{player_1_assigned['Name']}'s Turn", font_large, (255, 255, 255), 20, 40)
            else:
                render_text_button(f"{player_2_assigned['Name']}'s Turn", font_large, (255, 255, 255), 20, 40)

            if pygame.time.get_ticks() - message_timer < MESSAGE_DURATION:
                render_text_button(message, font_medium, (255,255,0), None ,250)
            pygame.display.update()
            clock.tick(30)


def player_fight():
    global current_turn , player1_health, player2_health, total_turns, current_state

    while True:
        if current_turn == 1: 
            total_turns += 1
            render_text_button(f"{player_1_assigned['Name']}'s Turn", font_large, (255, 255, 255), 20 , 50)
            handle_player_turn(1,2)
            if player2_health <= 0:
                if player_1_assigned['Name'] in ('Virus', 'Bacteria', 'Parasite'):
                    current_state = pathogen_win
                else:
                    current_state = immune_sys_win
                break
            current_turn = 2
        if current_turn == 2:
            total_turns += 1
            render_text_button(f"{player_2_assigned['Name']}'s Turn", font_large, (255, 255, 255), 20 , 50)
            handle_player_turn(2,1)
            if player1_health <= 0:
                if player_2_assigned['Name'] in ('Virus', 'Bacteria', 'Parasite'):
                    current_state = pathogen_win
                else:
                    current_state = immune_sys_win
                break
            current_turn = 1
        


# Made a class to create an enter button
class Button:
    # Initializes the button with its properties
    def __init__(self, text, x, y, width, height, color, hover_color, font, font_color):
        self.text = text  # The text displayed on the button
        self.x = x  
        self.y = y  
        self.width = width  
        self.height = height 
        self.color = color  
        self.hover_color = hover_color  
        self.font = font  
        self.font_color = font_color  
        self.rect = pygame.Rect(x, y, width, height) 

    # Draws the button on the screen
    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()  # Get the current position of the mouse. the mouse position on the screen
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(surface, self.hover_color, self.rect)  #The hover color 
        else:
            pygame.draw.rect(surface, self.color, self.rect)  # the button without the hover colore

        # the buttons text 
        text_surface = self.font.render(self.text, True, self.font_color)
        # this centers the button on the game sureface 
        text_rect = text_surface.get_rect(center=self.rect.center)
        # puts the text on the button
        surface.blit(text_surface, text_rect)

    def mouse(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True  
        return False  

# Helper function to draw multi-line text
def draw_multiline_text(surface, text, font, color, pos, line_spacing=5):
    lines = text.splitlines()  # Split the text into lines
    y = pos[1]  # Start at the given y position

    # Render each line and get its rect for centering
    rendered_lines = [font.render(line, True, color) for line in lines]
    
    # Compute total height of the text block
    total_height = sum(line.get_height() for line in rendered_lines) + (line_spacing * (len(lines) - 1))

    # Starting y position to center the block vertically
    y = (height - total_height) // 2 #alter the hight of the text on the surface screen. 

    # Now center each line horizontally by adjusting its rect
    for line in rendered_lines:
        text_rect = line.get_rect(center=(width // 2, y))  # Center horizontally
        surface.blit(line, text_rect)
        y += line.get_height() + line_spacing  # Update y for next line

#creating a background class for the end screens
class Background():
      def __init__(self, end_image_path):
            self.bgimage = pygame.image.load(end_image_path)
            self.rectBGimg = self.bgimage.get_rect()
 
            self.bgY1 = 0
            self.bgX1 = 0
 
            self.bgY2 = -self.rectBGimg.height
            self.bgX2 = 0
 
            self.movingDownSpeed = 2.5
         
      def update(self):
        self.bgY1 += self.movingDownSpeed
        self.bgY2 += self.movingDownSpeed
        if self.bgY1 >= self.rectBGimg.height:
            self.bgY1 = -self.rectBGimg.height
        if self.bgY2 >= self.rectBGimg.height:
            self.bgY2 = -self.rectBGimg.height
             
      def render(self, surface):
         surface.blit(self.bgimage, (self.bgX1, self.bgY1))
         surface.blit(self.bgimage, (self.bgX2, self.bgY2))

#create background objects to use in the end screens, calling on the background class
background_object_path = Background('data/PathogenImage.jpeg')
background_object_imm = Background('data/2624574.jpg')

# Creates the "Enter" button with its properties the hight variable positions the button on the screen
enter_button = Button("Enter", width // 2 - 100, height - 450, 200, 50, (0, 128, 0), (255, 0, 0), button_font, (255, 255, 255))

#choices and turns set
current_choice = ''
current_turn = 1
total_turns = 0

#game states
start_screen = 0
character_screen = 1
pathogen_screen = 2
immune_screen = 3
fight_screen = 4
immune_sys_win = 5
pathogen_win = 6

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
        screen.blit(background_image, (0, 0))
        # this is the helper function allowing to write mulitple lines. 
        draw_multiline_text(screen, text, font, (0, 0, 0), (0, 0))
        #Places the enter button created above into the game loop
        enter_button.draw(screen)
        # Event handling
        for event in events:
            # Check if the enter button is clicked
            if enter_button.mouse(event):
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
                        timer = pygame.time.get_ticks()
                    if immune_system.rect.collidepoint(event.pos):
                        current_choice = 'immune'
                        timer = pygame.time.get_ticks()
    if current_state == pathogen_screen:
        draw_pathogen_screen()
        virus = ClickableSprite(virus_image, 80, 300)
        bacteria = ClickableSprite(bacteria_image, 450, 300)
        parasite = ClickableSprite(parasite_image, 800,300)
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
        player_1_rect = (100,300)
        player_2_rect = (800,300)
        player1_health = int(player_1_assigned['Health'])
        player2_health = int(player_2_assigned['Health'])
        player_fight()
    if current_state == immune_sys_win:
        #play sound
        sound.stop()
        Success_sound.play(-1, 0)
        #load in background
        background_object_imm.update()
        background_object_imm.render(screen)
        #Draw multi-line text at the center of the screen
        draw_multiline_text(screen, imm_text, font, (0, 0, 0), (0, 0))
    if current_state == pathogen_win:
        #play sound
        sound.stop()
        doomsound.play(-1, 0)
        #load in background
        background_object_path.update()
        background_object_path.render(screen)
        #Draw multi-line text at the center of the screen
        draw_multiline_text(screen, path_text, font, (255, 255, 255), (0, 0))
    
    pygame.display.flip()
    fpsClock.tick(fps)