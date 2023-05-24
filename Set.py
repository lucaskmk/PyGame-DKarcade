import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Define colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)

#Define measures

WIDTH = 1000
HEIGHT = 780

CHARACTER_X=100
CHARACTER_Y=HEIGHT-50-20
CHARACTER_WIDTH=40
CHARACTER_HEIGHT=50


PLATFORM_WIDTH=WIDTH-60
PLATFORM_HEIGHT=30

STAIR_WIDTH=30
STAIR_HEIGHT=145

DK_WIDTH=120
DK_HEIGHT=120

barrels = []
BARREL_WIDTH = 30
BARREL_HEIGHT = 30


# Set up display and initialize Pygame

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Donkey Kong Arcade")

# Create barrels


#images

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

BARRIL_IMG=pygame.image.load('imagens/sprite_barril.png').convert_alpha()
BARRIL_IMG=pygame.transform.scale(BARRIL_IMG, (BARREL_WIDTH,BARREL_HEIGHT))

STAIR_IMG=pygame.image.load('imagens/sprite_escadas.png').convert_alpha()
STAIR_IMG=pygame.transform.scale(STAIR_IMG, (STAIR_WIDTH, STAIR_HEIGHT))

PLATFORM_IMG=pygame.image.load('imagens/sprite_chao.png').convert_alpha()
PLATFORM_IMG=pygame.transform.scale(PLATFORM_IMG, (PLATFORM_WIDTH, PLATFORM_HEIGHT))

PLATFORM_IMG_i=pygame.image.load('imagens/sprite_chao.png').convert_alpha()
PLATFORM_IMG_i=pygame.transform.scale(PLATFORM_IMG, (PLATFORM_WIDTH+70, PLATFORM_HEIGHT+15))

DK_IMG=pygame.image.load('imagens/sprite_DK_barril.png').convert_alpha()
DK_IMG=pygame.transform.scale(DK_IMG, (DK_WIDTH, DK_HEIGHT))

def game_over_message():
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over - Press any key to restart", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)

# Reset the game state
def reset_game():
    global game_over
    game_over = False
    #=================================== | Posicoes do jogador apos respawn | =====================
    character.rect.x = 100
    character.rect.y = (HEIGHT - 50 - 20)
    character.velocity = 0
    character.on_ground = False
    character.on_stair = False
    spawn_interval = 100
    barrels.clear()
# ========================== | Class | =================================================================================================================================================
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, img):
        self.image=img
        self.rect = pygame.Rect(x, y, width, height)


class Stair(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, img):
        self.image=img
        self.rect = pygame.Rect(x, y, width, height)


# Class for the character ============================================================================
class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height,img):
        self.image=img
        self.rect = pygame.Rect(x, y, width, height)
        self.velocity = 0
        self.jump_power = 8
        self.last_jump = pygame.time.get_ticks()
        self.jump_ticks = 700
        self.is_jumping = False
        self.last_key = 'right' 

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
                on_stair=True
                self.velocity=0
                self.rect.y+=self.velocity
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    self.rect.y-=2
                elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    self.rect.y+=2
            else:
                on_stair = False
        if on_stair==False:
            self.velocity += gravity
            self.rect.y += self.velocity
            

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
        elif not (keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_RIGHT] or keys[pygame.K_d]):
            if self.last_key == 'right':
                self.image = CHARACTER_STAND_IMG_RIGHT
            elif self.last_key == 'left':
                self.image = CHARACTER_STAND_IMG_LEFT


            

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

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, img):
        self.image=img
        self.rect = pygame.Rect(x, y, width, height)


# Class for barrels

class Barrel(pygame.sprite.Sprite):
    def __init__(self, x, y,width, height, img):
        self.image=img
        self.rect = pygame.Rect(x, y, width, height)
        self.speed =-4
        self.y_velocity = 0

    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.y_velocity

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
        



# ========================= | Objects | ================================================================================================================================================== 
# (Posicao X, posicao Y, tamanho em X, grosura em Y , (Cor))
# Create platforms
plataforma_inicial=Platform(0,HEIGHT-50, WIDTH, 50, PLATFORM_IMG_i)
PLATFORMS=[plataforma_inicial]
STAIRS=[]

for i in range(1,5):
    if (-1)**i < 0:
        EIXO_X_PLATAFORMA = 0
        EIXO_X_ESCADA=WIDTH-100
    else:
        EIXO_X_PLATAFORMA=70
        EIXO_X_ESCADA=80


    PLATFORMS.append(Platform(EIXO_X_PLATAFORMA, (HEIGHT-50)-150*i,  PLATFORM_WIDTH, PLATFORM_HEIGHT, PLATFORM_IMG))
    STAIRS.append(Stair(EIXO_X_ESCADA, (HEIGHT-30)-150*i, STAIR_WIDTH ,STAIR_HEIGHT , STAIR_IMG))
#stair6 = Stair(320, 950-870, 50, 120, WHITE)

# Create character   (0,HEIGHT-50, WIDTH, 50, RED)
character = Character(CHARACTER_X,CHARACTER_Y,CHARACTER_WIDTH,CHARACTER_HEIGHT,CHARACTER_IMG)
DK= Enemy( WIDTH-(DK_WIDTH+20) , 20 ,DK_WIDTH, DK_HEIGHT, DK_IMG)


gravity = 0.4

running = True
clock = pygame.time.Clock()
spawn_interval = 100
game_over = False


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_over:
                reset_game()
            elif event.key == pygame.K_SPACE:
                CHARACTER_IMG= pygame.image.load('imagens/sprite_mario_pulando.png').convert_alpha()
                CHARACTER_IMG=pygame.transform.scale(CHARACTER_IMG, (CHARACTER_WIDTH, CHARACTER_HEIGHT)) 
                character.jump()
                
 

    screen.fill((0, 0, 0))

    for stair in STAIRS:
        screen.blit(stair.image, stair.rect)

    for platform in PLATFORMS:
        screen.blit(platform.image, platform.rect)



    if not game_over:
        for barrel in barrels:
            barrel.update()
            screen.blit(barrel.image, barrel.rect)


        for barrel in barrels:
            if character.rect.colliderect(barrel.rect):
                game_over = True
                break

        tempo=pygame.time.get_ticks()
        intervalo= tempo - spawn_interval
        if intervalo >= spawn_interval :
            spawn_interval=tempo
            x = WIDTH-50
            y = 150
            barrel = Barrel(x, y, BARREL_WIDTH, BARREL_HEIGHT, BARRIL_IMG)
            barrels.append(barrel)

            


        character.update()
        screen.blit(character.image, character.rect)
        DK.update()
        screen.blit(DK.image, DK.rect)

    else:
        game_over_message()

    pygame.display.flip()
    clock.tick(50)

pygame.quit()


