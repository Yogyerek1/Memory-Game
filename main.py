import pygame
from config import *

pygame.init()

# variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memory game")
GAME_FONT = pygame.font.Font("resources/fonts/ChailceNogginRegular-2OXoW.ttf", 60)
TEXT_SURFACE = GAME_FONT.render("Memory Game", True, "black")
TEXT_RECT = TEXT_SURFACE.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 155))
SCENE_STATE = 1 # 1 - Main Menu, 2 - Game scene
FPS = 60
CLOCK = pygame.time.Clock()
BACKGROUND_COLOR = "cyan"
SOUND_STATE = True


# load menu resources
play_button = pygame.image.load("resources/MainMenu/playbutton1.png")
play_button_rect = play_button.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
soundof_button = pygame.image.load("resources/MainMenu/soundoff.png")
soundof_button_pos = (SCREEN_WIDTH - soundof_button.get_width() - 10, SCREEN_HEIGHT - soundof_button.get_height() - 10)
soundon_button = pygame.image.load("resources/MainMenu/soundon.png")
soundon_button_pos = (SCREEN_WIDTH - soundon_button.get_width() - soundof_button.get_width() - 25, SCREEN_HEIGHT - soundon_button.get_height() - 10)
soundoff_button_rect = soundof_button.get_rect(topleft=soundof_button_pos)
soundon_button_rect = soundon_button.get_rect(topleft=soundon_button_pos)
def MainMenuRender():
    # Play gomb középre igazítása
        
        screen.blit(play_button, play_button_rect)
        
        # Hang gomb jobb alsó sarokba helyezése (a képernyő szélétől 10 pixellel beljebb)
        
        screen.blit(soundof_button, soundof_button_pos)

        
        screen.blit(soundon_button, soundon_button_pos)

        screen.blit(TEXT_SURFACE, TEXT_RECT)


# load game resources
card_back = pygame.image.load("resources/Game/card_back_1.png")
card_back_rect = card_back.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

card_1 = pygame.image.load("resources/Game/card1.png")
card_1_rect = card_1.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

def game_render():
     screen.blit(card_back, card_back_rect)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if SCENE_STATE == 1:
                  if event.button == 1:
                        if play_button_rect.collidepoint(event.pos):
                            print("A play gombra kattintottál!")
                            SCENE_STATE = 2
                        elif soundoff_button_rect.collidepoint(event.pos):
                            print("Hang kikapcsolva!")
                            SOUND_STATE = False
                        elif soundon_button_rect.collidepoint(event.pos):
                            print("Hang bekapcsolva!")
                            SOUND_STATE = True
                                      
    screen.fill(BACKGROUND_COLOR)
    if SCENE_STATE == 1:
        MainMenuRender()
    elif SCENE_STATE == 2:
        game_render()
    CLOCK.tick(FPS)
    pygame.display.update()

pygame.quit()