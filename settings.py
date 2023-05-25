# ========================== | Imports | ================================================================================================================================================ 
import pygame
import random
from sprites import Character, Platform, Enemy, fogo, Barrel, Martelo, barrels
from sprites import *
# ========================== | PreSets | ================================================================================================================================================ 
WIDTH = 1000
HEIGHT = 780
CHARACTER_X=100
CHARACTER_Y=HEIGHT-50-20
CHARACTER_WIDTH=40
CHARACTER_HEIGHT=50
PLATFORM_WIDTH=WIDTH-60
PLATFORM_HEIGHT=30
STAIR_WIDTH=30
STAIR_HEIGHT=145
DK_WIDTH=120
DK_HEIGHT=120
FOGO_HEIGHT = 90
FOGO_WIDTH = 50
BARREL_WIDTH = 33
BARREL_HEIGHT = 33
MARTELO_WIDTH= 30
MARTELO_HEIGHT=30
RED = (255, 0, 0)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Donkey Kong Arcade")
character = Character(CHARACTER_X,CHARACTER_Y,CHARACTER_WIDTH,CHARACTER_HEIGHT,CHARACTER_IMG)
DK= Enemy( WIDTH-(DK_WIDTH+20) , 20 ,DK_WIDTH, DK_HEIGHT, DK_IMG)
fogo = fogo (CHARACTER_X-60, CHARACTER_Y-70 ,FOGO_WIDTH, FOGO_HEIGHT, FOGO_IMG)
martelo = Martelo(820, 470, MARTELO_WIDTH, MARTELO_HEIGHT, MARTELO_IMG)
listamartelo=pygame.sprite.Group()
listamartelo.add(martelo)
gravity = 0.4
running = True
clock = pygame.time.Clock()
ultimo_barril= 0
game_over = False
#  ========================== | Reset | ================================================================================================================================================ 
def game_over_message():
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over - Press any key to restart", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)

# Reset the game state
def reset_game():
    global game_over
    game_over = False
    #=================================== | Posicoes do jogador apos respawn | =======================================
    character.rect.x = 100
    character.rect.y = (HEIGHT - 50 - 20)
    character.velocity = 0
    character.on_ground = True
    character.on_stair = False
    character.equiped= False
    spawn_interval = 100
    martelo.rect.x = 820
    barrels.clear()
# ========================= | Objects | ============================================================================    
plataforma_inicial=Platform(0,HEIGHT-50, WIDTH, 50, PLATFORM_IMG_i)
PLATFORMS=[plataforma_inicial]
STAIRS=[]
for i in range(1,6):
    if (-1)**i < 0:
        EIXO_X_PLATAFORMA = 0
        EIXO_X_ESCADA=WIDTH-100
    else:
        EIXO_X_PLATAFORMA=70
        EIXO_X_ESCADA=80
    PLATFORMS.append(Platform(EIXO_X_PLATAFORMA, (HEIGHT-50)-150*i,  PLATFORM_WIDTH, PLATFORM_HEIGHT, PLATFORM_IMG))
    if i == 5 :
        STAIRS.append(Stair(EIXO_X_ESCADA-80, (HEIGHT-30)-150*i, STAIR_WIDTH ,STAIR_HEIGHT , STAIR_IMG))
    else:
        STAIRS.append(Stair(EIXO_X_ESCADA, (HEIGHT-30)-150*i, STAIR_WIDTH ,STAIR_HEIGHT , STAIR_IMG))