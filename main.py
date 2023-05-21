# ========================== | Imports | ==============================
import pygame
import random
from settings import *
from sprites import *
# ========================== | Display | ==============================
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Donkey Kong Arcade")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#========================== | CREATE | ====================
    platform1.draw(screen)
    platform2.draw(screen)
    platform3.draw(screen)
    platform4.draw(screen)
    platform5.draw(screen)
    platform6.draw(screen)
    stair1.draw(screen)
    stair2.draw(screen)
    stair3.draw(screen)
    stair4.draw(screen)
    stair5.draw(screen)
    pygame.display.flip() # Update no jogo
