#!/usr/bin/env python3

import pygame
import sys

pygame.init()
pygame.mixer.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 1200, 800
screen = pygame.display.set_mode((width, height))

# Text specifications
font = pygame.font.Font(None, 75)

#make the viriable for sound.
Success_sound = pygame.mixer.Sound('data/Success.mp3')

############################ Font for button ###########################
Immune_restart_button_font = pygame.font.SysFont(None, 50)

class Background():
      def __init__(self):
            self.bgimage = pygame.image.load('data/2624574.jpg')
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

class ImmuneRestartButton:
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
    y = (height - total_height) // 2

    # Now center each line horizontally by adjusting its rect
    for line in rendered_lines:
        text_rect = line.get_rect(center=(width // 2, y))  # Center horizontally
        surface.blit(line, text_rect)
        y += line.get_height() + line_spacing  # Update y for next line

# Multi-line text to display
text = "Immune System Wins!\n\nCongratulations you've\nsurvived ImmuneEscape!\nThank you for playing\n\nThis was as an Anastasia, Emma,\nWalter, & Colin Production"

background_object = Background()

Success_sound.play(-1, 0) #plays the music

# Creates the "Enter" button with its properties the hight variable positions the button on the screen
IM_Restart_button = ImmuneRestartButton("Restart", width // 2 - 100, height - 150, 200, 50, (0, 0, 0), (255, 0, 0), Immune_restart_button_font, (255, 255, 255))

# Game end screen loop
end_screen = True
while end_screen:
    screen.fill((0, 0, 0))  # Fill the screen with black

    background_object.update()
    background_object.render(screen)

    # Draw multi-line text at the center of the screen
    draw_multiline_text(screen, text, font, (0, 0, 0), (0, 0))
    #Places the enter button created above into the game loop
    IM_Restart_button.draw(screen)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            end_screen = False
    
    pygame.display.flip()  # Update the display
    fpsClock.tick(fps)  # Control the frame rate

# Main game loop (empty for now)
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.flip()
    fpsClock.tick(fps)