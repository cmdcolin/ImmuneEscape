import pygame 
import sys 

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Text-Based Battle')

font_large=pygame.font.SysFont(None, 60)
font_medium = pygame.font.SysFont(None,40)
font_small = pygame.font.SysFont(None, 30)

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (0,255,0)
BLUE = (0,0,255)

font = pygame.font.Font(None,36)

# class Player:
#     def __init__(self,name,max_health,pos_y,actions):
#         self.name = name
#         self.health = max_health
#         self.pos_y = pos_y
#         self.actions = actions 
#         self.input_text = ''

# p1_actions = {}

player1_health = 100
player2_health = 100
current_turn = 1


def render_text_button(text,font,color,x,y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(topleft=(x,y))
    screen.blit(text_surface,(x,y))
    return text_rect

def handle_player_turn(player,opponent):
    global player1_health, player2_health

    screen.fill((0, 0, 0)) # Black background
    render_text_button(f"{player}'s Turn", font_large, (255, 255, 255), 20, 50)
    render_text_button(f"Pathogen Health: {player1_health}", font_small, (255, 255, 255), 20, 120)
    render_text_button(f"Immune System Health: {player2_health}", font_small, (255, 255, 255), 500, 120)
    render_text_button("Choose your action:", font_medium, (255, 255, 255), 300, 400)
    attack_rect = render_text_button("[Attack]", font_medium, (255, 0, 0), 100, 450) # Red
    mutate_rect = render_text_button("[Mutate]", font_medium, (0, 255, 0), 100, 500) # Green
    evade_rect = render_text_button("[Evade]", font_medium,(0,200,255), 600, 500)
    screen.blit(player1_img, (50,screen_height//2 -75))
    screen.blit(player2_img, (screen_width - 200, screen_height//2 - 75))
    pygame.display.flip()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if attack_rect.collidepoint(event.pos):
                    damage = 20
                    if player == 1:
                        player2_health -= damage
                    else:
                        player1_health -= damage
                    return 
                if mutate_rect.collidepoint(event.pos):
                    return 
        pygame.time.Clock().tick(30)

player2_img = pygame.image.load('data/TCell0001.png').convert_alpha()
player1_img = pygame.image.load('data/SARSCoV20002.png').convert_alpha()

player1_img = pygame.transform.scale(player1_img, (150,150))
player2_img = pygame.transform.scale(player2_img, (150,150))



def main():
    global current_turn , player1_health, player2_health

    while True:
        if player1_health<= 0 or player2_health <=0:
            winner = 'Immune System' if player2_health <= 0 else 'Pathogen'
            screen.fill((0,0,0))
            winner_text = font_large.render(f"{winner} wins !", True, (0,255,0))
            winner_text_rect = winner_text.get_rect(center=(screen_width//2, screen_height//2))
            screen.blit(winner_text, winner_text_rect)
            pygame.display.flip()
            pygame.time.wait(3000)
            break 
        if current_turn == 1: 
            handle_player_turn('Immune System', 'Pathogen')
            current_turn = 2
        else:
            handle_player_turn('Pathogen','Immune System')
            current_turn = 1
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
            


           