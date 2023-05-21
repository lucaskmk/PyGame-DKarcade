# ========================== | Imports | ==============================
import pygame
import random
from settings import *
# ========================== | PreSets | ==============================
WIDTH = 800  
HEIGHT = 1000
GRAVITY = 0.6
RED = (255, 0, 0)
WHITE = (255, 255, 255)
# ========================== | Class | ==============================
class Platform:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class Stair:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class Character:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.velocity = 0
        self.jump_power = 12
        self.on_ground = False
        self.on_stair = False  # indicar se ta na escada
    def update(self):
        # botar gravidade na velocidade
        self.velocity += GRAVITY
        # Update posicao do jogador
        self.rect.y += self.velocity
        for platform in PLATFORMS: # =============================== COLISAO PLATFORMA
            if self.rect.colliderect(platform.rect):
                if self.velocity > 0:
                    self.rect.bottom = platform.rect.top
                    self.velocity = 0
                    self.on_ground = True
                else:
                    self.rect.top = platform.rect.bottom
                    self.velocity = 0
                break
        else:
            self.on_ground = False
        for stair in STAIRS: # ====================================== COLISAO NA ESCADA
            if self.rect.colliderect(stair.rect):
                self.rect.bottom = stair.rect.top
                self.velocity = 0
                self.on_ground = True
                self.on_stair = True 
                break
        else:
            self.on_stair = False
        keys = pygame.key.get_pressed() # =========================== MOV HORIZONTAL
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= 3
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += 3

        # Deixar ele so dentro da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        if self.on_stair: # ========================================= MOV VERTICAL NAS ESCADAS
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.rect.y -= 2
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.rect.y += 2
    def jump(self):
        if self.on_ground:
            self.velocity = -self.jump_power
            self.on_ground = False
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
## ========================= | Objects | ============================== 
# (Posicao X, posicao Y, tamanho em X, grosura em Y , (Cor))
PLATFORM1 = Platform(0, 950, 800, 20, RED)
PLATFORM2 = Platform(0, 950-150, 800, 20, RED)
PLATFORM3 = Platform(0, 950-300, 800, 20, RED)
PLATFORM4 = Platform(0, 950-450, 800, 20, RED)
PLATFORM5 = Platform(0, 950-600, 800, 20, RED)
PLATFORM6 = Platform(0, 950-750, 800, 20, RED)
PLATFORM7 = Platform(200, 950-870, 200, 20, RED)
STAIR1 = Stair(720, 950-150, 50, 150, WHITE)
STAIR2 = Stair(30, 950-300, 50, 150, WHITE)
STAIR3 = Stair(720, 950-450, 50, 150, WHITE)
STAIR4 = Stair(30, 950-600, 50, 150, WHITE)
STAIR5 = Stair(720, 950-750, 50, 150, WHITE)
STAIR6 = Stair(320, 950-870, 50, 120, WHITE)

CHARACTER = Character(100, 930, 50, 50, WHITE)
# detectar colisoes nessa lista
PLATFORMS = [PLATFORM1, PLATFORM2, PLATFORM3, PLATFORM4, PLATFORM5, PLATFORM6, PLATFORM7]
STAIRS = [STAIR1, STAIR2, STAIR3, STAIR4, STAIR5, STAIR6]