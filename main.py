# ========================== | Imports | ==============================
import pygame
import random
from settings import *
from sprites import *
# ========================== | Display | ==============================
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Donkey Kong Arcade")

# ========================== | Game loop | ==========================
running = True
clock = pygame.time.Clock()
spawn_timer = 0
spawn_interval = 90
min_barrel_count = 2
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_over:
                reset_game()
            elif event.key == pygame.K_SPACE:
                CHARACTER.jump()
    screen.fill((0, 0, 0))
# ================================== | CREATE | ======================
    for platform in PLATFORMS:
        platform.draw(screen)
    for stair in STAIRS:
        stair.draw(screen)
# ================================= | Update Barrel | ================
    if not game_over:
        for barrel in BARRELS:
            barrel.update()
            barrel.draw(screen)

        for barrel in BARRELS:
            if CHARACTER.rect.colliderect(barrel.rect):
                game_over = True
                break
        spawn_timer += clock.get_rawtime()
        if spawn_timer >= spawn_interval:
            for platform in PLATFORMS:
                x = random.randint(830, 1060)
                y = platform.rect.top - barrel_radius
                barrel = Barrel(x, y, barrel_radius, RED, barrel_speed)
                BARRELS.append(barrel)
            spawn_timer = 0
# ================================= | END Update Barrel | =============
        CHARACTER.update()
        CHARACTER.draw(screen)
    else:
        game_over_message()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


