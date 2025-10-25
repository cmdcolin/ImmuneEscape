#!/usr/bin/env python3

import pygame
import sys

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))

# Text specifications
font = pygame.font.Font(None, 45)

# Helper function to draw multi-line text
def draw_multiline_text(surface, text, font, color, pos, line_spacing=5):
    lines = text.splitlines()  # Split the text into lines
    y = pos[1]  # Start at the given y position

    # Render each line and get its rect for centering
    rendered_lines = [font.render(line, True, color) for line in lines]
    
    # Compute total height of the text block
    total_height = sum(line.get_height() for line in rendered_lines) + (line_spacing * (len(lines) - 1))

    # Starting y position to center the block vertically
    y = (height - total_height) // 10

    # Now center each line horizontally by adjusting its rect
    for line in rendered_lines:
        text_rect = line.get_rect(center=(width // 2, y))  # Center horizontally
        surface.blit(line, text_rect)
        y += line.get_height() + line_spacing  # Update y for next line

# Multi-line text to display
text = "Congratulations you've\nsurvived ImmuneEscape!\nThank you for playing\n\nThis was as an Anastasia, Emma\nWalter, & Colin Production"

# Game start screen loop
start_screen = True
while start_screen:
    screen.fill((0, 0, 0))  # Fill the screen with black

    # Draw multi-line text at the center of the screen
    draw_multiline_text(screen, text, font, (123, 252, 3), (0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            start_screen = False

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