# ========================== | Imports | ==============================
import pygame
from settings import *
from sprites import *
# ========================== | Display | ==============================
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Donkey Kong Arcade")

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                CHARACTER.jump()
    screen.fill((0, 0, 0))
#========================== | CREATE | ====================
    PLATFORM1.draw(screen)
    PLATFORM2.draw(screen)
    PLATFORM3.draw(screen)
    PLATFORM4.draw(screen)
    PLATFORM5.draw(screen)
    PLATFORM6.draw(screen)
    PLATFORM7.draw(screen)
    STAIR1.draw(screen)
    STAIR2.draw(screen)
    STAIR3.draw(screen)
    STAIR4.draw(screen)
    STAIR5.draw(screen)
    STAIR6.draw(screen)
    
    CHARACTER.update()
    CHARACTER.draw(screen)
    pygame.display.flip() # Update no jogo
    clock.tick(60)
pygame.quit()
