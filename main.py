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
