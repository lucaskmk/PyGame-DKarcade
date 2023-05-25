import pygame
import random
from settings import *
from sprites import Character, Platform, Enemy, fogo, Barrel, Martelo, barrels
from sprites import *


class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height,img):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.equiped= False
        self.rect = pygame.Rect(x, y, width, height)
        self.velocity = 0
        self.jump_power = 8
        self.last_jump = pygame.time.get_ticks()
        self.jump_ticks = 700
        self.is_jumping = False
        self.last_key = 'right' 
        self.lastupdown_key = 'still'
        self.on_ground = True
        self.on_stair=False
    def jump(self):
        now = pygame.time.get_ticks()
        ticks_decorridos = now - self.last_jump
        if ticks_decorridos > self.jump_ticks:
            self.velocity = -self.jump_power
            self.last_jump=now
            self.is_jumping = True  
    def update(self):

        keys = pygame.key.get_pressed()
        for stair in STAIRS:
            if self.rect.colliderect(stair.rect):
                self.on_stair=True
                self.image = CHARACTER_IMG_UP
                self.velocity=0
                self.rect.y+=self.velocity
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    self.rect.y-=2
                    self.lastupdown_key = 'up'
                    self.on_ground = False
                elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    self.rect.y+=2
                    self.lastupdown_key = 'down'
                    self.on_ground = False
                self.image = CHARACTER_IMG_DOWN
            else:
                
                on_stair = False

        if self.on_stair: # se na escada so desenho da escada
            # Imagem escada
            if self.lastupdown_key == 'up' :
                self.image = CHARACTER_IMG_UP
            elif self.lastupdown_key == 'down':
                self.image = CHARACTER_IMG_DOWN
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.rect.x -= 3
                self.last_key = 'left'
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.rect.x += 3
                self.last_key = 'right'
        else: # se n faz td
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.rect.x -= 3
                self.image = pygame.image.load('imagens/sprite_mario_andando_esquerda.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
                self.last_key = 'left'
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.rect.x += 3
                self.image = pygame.image.load('imagens/sprite_mario_andando_direita.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
                self.last_key = 'right'
            # IMAGEM SALTANDO
            if self.is_jumping: 
                if self.last_key == 'right':
                    self.image = CHARACTER_JUMPING_IMG_RIGHT
                elif self.last_key == 'left':
                    self.image = CHARACTER_JUMPING_IMG_LEFT 
            # IMAGEM PARADO
            if not (keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_RIGHT] or keys[pygame.K_d]):
                if not self.on_ground:
                    # IMAGEM SALTANDO enquatoparado
                    if not self.on_stair:
                        if self.last_key == 'right':
                            self.image = CHARACTER_JUMPING_IMG_RIGHT
                        elif self.last_key == 'left':
                            self.image = CHARACTER_JUMPING_IMG_LEFT
                    # Imagem escada
                    if self.lastupdown_key == 'up' :
                        self.image = CHARACTER_IMG_UP
                    elif self.lastupdown_key == 'down':
                        self.image = CHARACTER_IMG_DOWN
                elif self.on_ground:
                    if self.last_key == 'right':
                        self.image = CHARACTER_STAND_IMG_RIGHT
                    elif self.last_key == 'left':
                        self.image = CHARACTER_STAND_IMG_LEFT
                    if self.is_jumping: # IMAGEM SALTANDO se tambem parado
                        if self.last_key == 'right':
                            self.image = CHARACTER_JUMPING_IMG_RIGHT
                        elif self.last_key == 'left':
                            self.image = CHARACTER_JUMPING_IMG_LEFT 
            
        if on_stair==False:
            self.velocity += gravity
            self.rect.y += self.velocity
            self.lastupdown_key = 'still'
            self.on_ground = True
            self.on_stair =  False
            
            
        #for event in pygame.event.get():
        # ----- Verifica consequências
        #if event.type == pygame.KEYUP:
        #====================================== COM MARTELO ============================================================================
        if self.equiped==True:
            if keys[pygame.K_p]:
                self.hit = True
                if self.last_key == 'left':
                    self.image = CHARACTER_HAMMER_LEFT
                elif self.last_key == 'right':
                    self.image = CHARACTER_HAMMER_RIGHT
                    
                    
        for platform in PLATFORMS:
            if self.rect.colliderect(platform.rect):
                if self.velocity > 0:
                    self.rect.bottom = platform.rect.top
                    self.velocity = 0
                else:
                    self.rect.top = platform.rect.bottom
                    self.velocity = 0
                self.is_jumping = False
                break        
        
        if self.rect.bottom > 950:
            self.rect.bottom = 950
            self.velocity = 0
            self.on_ground = True

        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity = 0

        # Deixa ele so dentro da tela

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
     