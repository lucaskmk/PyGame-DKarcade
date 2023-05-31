# ========================== | Imports | ==============================
import pygame
from pygame.locals import *
import random
import operator
import time
from settings import *
# ========================== | PreSets | ==============================
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# ========================== | SPRITES | ==============================
DKSTARTGAME = pygame.image.load('imagens\Donkey_Kong_flier.jpg').convert_alpha()
DKSTARTGAME = pygame.transform.scale(DKSTARTGAME, (WIDTH, HEIGHT))
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
CHARACTER_HAMMER_LEFT = pygame.image.load('imagens\sprite_martelo_esquerdo.png')
CHARACTER_HAMMER_LEFT = pygame.transform.scale(CHARACTER_HAMMER_LEFT, (CHARACTER_WIDTH+30,CHARACTER_HEIGHT)).convert_alpha()
CHARACTER_HAMMER_RIGHT = pygame.image.load('imagens\sprite_martelo_direito.png').convert_alpha()
CHARACTER_HAMMER_RIGHT = pygame.transform.scale(CHARACTER_HAMMER_RIGHT, (CHARACTER_WIDTH+30,CHARACTER_HEIGHT))
CHARACTER_HAMMER_UP_LEFT = pygame.image.load('imagens\sprite_martelo_cima_direita.png').convert_alpha()
CHARACTER_HAMMER_UP_LEFT = pygame.transform.scale(CHARACTER_HAMMER_UP_LEFT, (CHARACTER_WIDTH+30,CHARACTER_HEIGHT)).convert_alpha()
CHARACTER_HAMMER_UP_RIGHT = pygame.image.load('imagens\sprite_Mmartelo_cima_direita.png').convert_alpha()
CHARACTER_HAMMER_UP_RIGHT = pygame.transform.scale(CHARACTER_HAMMER_UP_RIGHT, (CHARACTER_WIDTH+30,CHARACTER_HEIGHT)).convert_alpha()

BARRIL_IMG=pygame.image.load('imagens/sprite_barril.png').convert_alpha()
BARRIL_IMG=pygame.transform.scale(BARRIL_IMG, (BARREL_WIDTH,BARREL_HEIGHT))
BARRIL_EXPLODE=pygame.image.load('imagens\explosion.png').convert_alpha()
BARRIL_EXPLODE=pygame.transform.scale(BARRIL_EXPLODE, (BARREL_WIDTH,BARREL_HEIGHT))
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