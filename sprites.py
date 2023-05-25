# ========================== | Imports | ==============================
import pygame
import random
from settings import *
# ========================== | PreSets | ==============================
#Sounds
pygame.mixer.music.load('sound/background.mp3')
pygame.mixer.music.set_volume(0.2)
pulo=pygame.mixer.Sound('sound/pulo.ogg')
# ========================== | SPRITES | ==============================
CHARACTER_IMG=pygame.image.load('imagens/sprite_mario_direita.png').convert_alpha()
CHARACTER_IMG=pygame.transform.scale(CHARACTER_IMG, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
CHARACTER_STAND_IMG_RIGHT = pygame.image.load('imagens\sprite_mario_direita.png').convert_alpha()
CHARACTER_STAND_IMG_RIGHT = pygame.transform.scale(CHARACTER_STAND_IMG_RIGHT, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
CHARACTER_STAND_IMG_LEFT = pygame.image.load('imagens\sprite_mario_esquerda.png').convert_alpha()
CHARACTER_STAND_IMG_LEFT = pygame.transform.scale(CHARACTER_STAND_IMG_LEFT, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
CHARACTER_JUMPING_IMG_RIGHT = pygame.image.load('imagens\sprite_mario_pulando.png').convert_alpha()
CHARACTER_JUMPING_IMG_RIGHT = pygame.transform.scale(CHARACTER_JUMPING_IMG_RIGHT, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
CHARACTER_JUMPING_IMG_LEFT = pygame.image.load('imagens\sprite_mario_pulando_ESQUERDA.png').convert_alpha()
CHARACTER_JUMPING_IMG_LEFT = pygame.transform.scale(CHARACTER_JUMPING_IMG_LEFT, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
CHARACTER_IMG_UP = pygame.image.load('imagens\sprite_mario_subindo.png').convert_alpha()
CHARACTER_IMG_UP =  pygame.transform.scale(CHARACTER_IMG_UP, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
CHARACTER_IMG_DOWN = pygame.image.load('imagens\sprite_mario_descendo.png').convert_alpha()
CHARACTER_IMG_DOWN =  pygame.transform.scale(CHARACTER_IMG_DOWN, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
CHARACTER_HAMMER_LEFT = pygame.image.load('imagens\sprite_martelo_esquerdo.png').convert_alpha()
CHARACTER_HAMMER_LEFT = pygame.transform.scale(CHARACTER_HAMMER_LEFT, (BARREL_WIDTH,BARREL_HEIGHT))
CHARACTER_HAMMER_RIGHT = pygame.image.load('imagens\sprite_martelo_direito.png').convert_alpha()
CHARACTER_HAMMER_RIGHT = pygame.transform.scale(CHARACTER_HAMMER_RIGHT, (BARREL_WIDTH,BARREL_HEIGHT))
BARRIL_IMG=pygame.image.load('imagens/sprite_barril.png').convert_alpha()
BARRIL_IMG=pygame.transform.scale(BARRIL_IMG, (BARREL_WIDTH,BARREL_HEIGHT))
BARRIL_explode=pygame.image.load('imagens\explosion-pixel-art.png').convert_alpha()
BARRIL_explode=pygame.transform.scale(BARRIL_explode, (BARREL_WIDTH,BARREL_HEIGHT))
BARRIL_IMG_D_BAIXO=pygame.image.load('imagens/sprite_barril_direita_baixo.png').convert_alpha()
BARRIL_IMG_D_BAIXO=pygame.transform.scale(BARRIL_IMG_D_BAIXO, (BARREL_WIDTH,BARREL_HEIGHT))
BARRIL_IMG_D_CIMA=pygame.image.load('imagens/sprite_barril_direita_cima.png').convert_alpha()
BARRIL_IMG_D_CIMA=pygame.transform.scale(BARRIL_IMG_D_CIMA, (BARREL_WIDTH,BARREL_HEIGHT))
BARRIL_IMG_E_BAIXO=pygame.image.load('imagens/sprite_barril_esquerda_baixo.png').convert_alpha()
BARRIL_IMG_E_BAIXO=pygame.transform.scale(BARRIL_IMG_E_BAIXO, (BARREL_WIDTH,BARREL_HEIGHT))
STAIR_IMG=pygame.image.load('imagens/sprite_escadas.png').convert_alpha()
STAIR_IMG=pygame.transform.scale(STAIR_IMG, (STAIR_WIDTH, STAIR_HEIGHT))
PLATFORM_IMG=pygame.image.load('imagens/sprite_chao.png').convert_alpha()
PLATFORM_IMG=pygame.transform.scale(PLATFORM_IMG, (PLATFORM_WIDTH, PLATFORM_HEIGHT))
PLATFORM_IMG_i=pygame.image.load('imagens/sprite_chao.png').convert_alpha()
PLATFORM_IMG_i=pygame.transform.scale(PLATFORM_IMG, (PLATFORM_WIDTH+70, PLATFORM_HEIGHT+15))
FOGO_IMG = pygame.image.load('imagens/sprite_fire.png').convert_alpha()
FOGO_IMG = pygame.transform.scale(FOGO_IMG, ( FOGO_WIDTH, FOGO_HEIGHT))
FOGO_IMG2 = pygame.image.load('imagens/sprite_fogo2.png').convert_alpha()
FOGO_IMG2 = pygame.transform.scale(FOGO_IMG2, ( FOGO_WIDTH, FOGO_HEIGHT))
FOGO_IMG3 = pygame.image.load('imagens/sprite_fogo3.png').convert_alpha()
FOGO_IMG3 = pygame.transform.scale(FOGO_IMG3, ( FOGO_WIDTH, FOGO_HEIGHT))
DK_IMG=pygame.image.load('imagens/sprite_dk_jogando.png').convert_alpha()
DK_IMG=pygame.transform.scale(DK_IMG, (DK_WIDTH-10, DK_HEIGHT-10))
DK_IMG_DIREITA=pygame.image.load('imagens/sprite_dk_bravo_direita.png').convert_alpha()
DK_IMG_DIREITA=pygame.transform.scale(DK_IMG_DIREITA, (DK_WIDTH, DK_HEIGHT))
DK_IMG_ESQUERDA=pygame.image.load('imagens/sprite_dk_bravo_esquerda.png').convert_alpha()
DK_IMG_ESQUERDA=pygame.transform.scale(DK_IMG_ESQUERDA, (DK_WIDTH, DK_HEIGHT))
MARTELO_IMG=pygame.image.load('imagens/sprite_martelo.png').convert_alpha()
MARTELO_IMG=pygame.transform.scale(MARTELO_IMG, (MARTELO_WIDTH, MARTELO_HEIGHT))
# ========================== | Class | =================================================================================================================================================
barrels = []
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, img):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.rect = pygame.Rect(x, y, width, height)


class Stair(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, img):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.rect = pygame.Rect(x, y, width, height)

# Class for the character ============================================================================
# Class for DK
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, img):
        pygame.sprite.Sprite.__init__(self)       
        self.image=img
        self.rect = pygame.Rect(x, y, width, height)
        self.image_list = [DK_IMG,DK_IMG_DIREITA,DK_IMG_ESQUERDA]
        self.i=0
        self.ultima_i=0
    def update(self):
        agora=pygame.time.get_ticks()
        if agora-self.ultima_i>=700:
            self.i+=1
            self.image=self.image_list[self.i % 3]
            self.ultima_i=agora


#============================================================================================
#Class for fire
class fogo(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, img):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.rect = pygame.Rect(x, y, width, height)
        self.image_list = [FOGO_IMG3, FOGO_IMG, FOGO_IMG2]
        self.i=0
        self.ultima_i=0
    def update(self):
        agora=pygame.time.get_ticks()
        if agora-self.ultima_i>=500:
            self.i+=1
            self.image=self.image_list[self.i % 3]
            self.ultima_i=agora

# Class for barrels

class Barrel(pygame.sprite.Sprite):
    def __init__(self, x, y,width, height, img):

        pygame.sprite.Sprite.__init__(self)

        self.image=img
        self.rect = pygame.Rect(x, y, width, height)
        self.speed =-4
        self.y_velocity = 0


        self.i=0
        self.ultima_i=0

    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.y_velocity
        agora=pygame.time.get_ticks()
        if agora-self.ultima_i>=250:
            if self.speed<0:
                self.image_list = [BARRIL_IMG,  BARRIL_IMG_E_BAIXO, BARRIL_IMG_D_BAIXO, BARRIL_IMG_D_CIMA]
            if self.speed>0:
                self.image_list = [BARRIL_IMG, BARRIL_IMG_D_CIMA, BARRIL_IMG_D_BAIXO, BARRIL_IMG_E_BAIXO]

            self.i+=1
            self.image=self.image_list[self.i % 4]
            self.ultima_i=agora


        for platform in PLATFORMS:
            if self.rect.colliderect(platform.rect):
                self.rect.bottom = platform.rect.top
                self.y_velocity = 0
                break
        else:
            self.y_velocity += gravity

        

        # Deixa ele so dentro da tela

        if self.rect.x < 0:
            self.rect.x = 0
            self.speed= 4

        if self.rect.x > WIDTH-20:
            self.rect.x = WIDTH-20
            self.speed = -4

        if self.rect.colliderect(fogo.rect):
            self.image= BARRIL_explode
        if (self.rect.x <= 2) and (self.rect.y >= CHARACTER_Y-70 ):
            self.velocity=0
            self.rect.x = -10
            self.rect.y = 10000000
            self.y_velocity = 0
            self.speed = 0

class Martelo(pygame.sprite.Sprite):
    def __init__(self, x, y,width, height, img):

        pygame.sprite.Sprite.__init__(self)      
        self.image=img
        self.rect = pygame.Rect(x, y, width, height)
