import pygame
import random
import time
from ClassCharecter import *
from sprites import Character, Platform, Enemy, fogo, Barrel, Martelo, barrels
from sprites import *
from settings import *
from settings import screen,  MARTELO_WIDTH
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
#=================================== | Initialize Pygame | =====================
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
#=================================== | Initialize Pygame | =====================
pygame.init()
pygame.mixer.init()
pygame.mixer.music.play(loops=-1)
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            character.hit = False
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_over:
                reset_game()
            elif event.key == pygame.K_SPACE:  
                    character.jump()
    screen.fill((0, 0, 0))
    for stair in STAIRS:
        STAIR_IMG = pygame.Surface.set_colorkey(stair.image, (0,0,0))
        screen.blit(stair.image, stair.rect)
    for platform in PLATFORMS:
        screen.blit(platform.image, platform.rect)
    if not game_over:
        for barrel in barrels:
            barrel.update()
            screen.blit(barrel.image, barrel.rect)
        for barrel in barrels:
            if character.rect.colliderect(barrel.rect):
                if not character.hit:
                    game_over = True
                    break
            if fogo.rect.colliderect(barrel.rect):
                barrel.kill()
        spawn_interval = random.randint(2000, 3500)
        tempo=pygame.time.get_ticks()
        intervalo= tempo - ultimo_barril
        if intervalo >= spawn_interval:
            DK.i=0
            ultimo_barril=tempo
            x = WIDTH-160
            y = 150
            barrel = Barrel(x, y, BARREL_WIDTH, BARREL_HEIGHT, BARRIL_IMG)
            barrels.append(barrel)
        if character.rect.colliderect(martelo.rect):
            martelo.rect.x = 1200
            character.equiped= True
        character.update()
        screen.blit(character.image, character.rect)
        DK.update()
        screen.blit(DK.image, DK.rect)
        fogo.update()
        screen.blit(fogo.image, fogo.rect)
        martelo.update()
        listamartelo.draw(screen)
    else:
        game_over_message()
    pygame.display.flip()
    clock.tick(50)
pygame.quit()


