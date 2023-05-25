import pygame
import random
import time
from sprites import *
from settings import *
from settings import screen
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


