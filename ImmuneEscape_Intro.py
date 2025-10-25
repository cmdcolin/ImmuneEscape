#!/usr/bin/env python3

import pygame
import sys

pygame.init()
pygame.mixer.init() # for adding sound. 

fps = 60
fpsClock = pygame.time.Clock()

# Sets up the pygame surface aka the screen we see. 
width, height = 1200, 800
screen = pygame.display.set_mode((width, height))
background_image = pygame.image.load('data/Immune battle.jpg').convert()
background_image = pygame.transform.scale(background_image, (width, height))

# We can add sound to play in
# sound = pygame.mixer.Sound('')

# Text specifications
font = pygame.font.SysFont(None, 75)
button_font = pygame.font.SysFont(None, 50)

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

# Multi-line text to display
text = "\nWelcome to ImmuneEscape!\n\n\n\n\n\n\n\n\n\n\n\nWhere the outcomes is literally life or death\n PLAY AT YOUR OWN RISK"

# Creates the "Enter" button with its properties
enter_button = Button("Enter", width // 2 - 100, height - 450, 200, 50, (0, 128, 0), (255, 0, 0), button_font, (255, 255, 255))

# Game end screen loop
end_screen = True
while end_screen:
    screen.blit(background_image, (0, 0))

    # this is the helper function allowing to write mulitple lines. 
    draw_multiline_text(screen, text, font, (0, 0, 0), (0, 0))

    #Places the enter button created above into the game loop
    enter_button.draw(screen)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check if the enter button is clicked
        if enter_button.mouse(event):
            end_screen = False
    

    pygame.display.flip()
    fpsClock.tick(fps)  