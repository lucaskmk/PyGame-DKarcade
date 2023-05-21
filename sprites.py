# ========================== | Imports | ==============================
import pygame
import random
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