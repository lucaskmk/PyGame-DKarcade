# ========================== | Imports | ==============================
# import pygame
import json
from pygame.locals import *
import random
import operator
import time
from settings import *
from sprites import *

with open('saves.json', 'r') as arq:
    savedscore=arq.read()
savedscore=json.loads(savedscore)
# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Define score
font = pygame.font.Font(None, 36)
score = 0
np = 1
nplayer = 'Player'

barrels = []

# Set up display and initialize Pygame

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Donkey Kong Arcade")

#Sounds

pygame.mixer.music.load('sound/background.mp3')
pygame.mixer.music.set_volume(0.1)
pulo=pygame.mixer.Sound('sound/pulo.mp3')
pulo.set_volume(0.05)
martelosom=pygame.mixer.Sound('sound/martelo.mp3')
martelosom.set_volume(0.05)

def game_over_message():
    font = pygame.font.Font(None, 36)
    if score > int(savedscore["Top 2"]) and score > int(savedscore["Top 3"]):
        savedscore["Top 1"] = score
    elif score > int(savedscore["Top 3"]):
        savedscore["Top 2"] = score
    elif score > int(savedscore["Top 3"]):
        savedscore["Top 3"] = score
    top1 = font.render("Score: " + str(savedscore[0]) + '  :      ' + str(savedscore["Top 1"]), True, (255, 255, 255))
    top2 = font.render("Score: " + str(savedscore[1]) + '  :      ' +  str(savedscore["Top 2"]), True, (255, 255, 255))
    top3 = font.render("Score: " + str(savedscore[2]) + '  :      ' +  str(savedscore["Top 3"]), True, (255, 255, 255))
    screen.blit(top1, (LEADERBOARD_X, LEADERBOARD_Y))
    screen.blit(top2, (LEADERBOARD_X, LEADERBOARD_Y+40))
    screen.blit(top3, (LEADERBOARD_X, LEADERBOARD_Y+80))
        
        
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
    character.on_ground = True
    character.on_stair = False
    character.equiped= False
    spawn_interval = 100
    martelo.rect.x = 820
    hitbarrell = False
    TIME = 0
    barrels.clear()
# ========================== | Class | =================================================================================================================================================
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, img):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.rect = pygame.Rect(x, y, width, height)


class Stair(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, img):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.rect = pygame.Rect(x, y, width, height)


# Class for the character ============================================================================
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
            pulo.play()

    



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
            if self.last_key == 'left':
                self.image=CHARACTER_HAMMER_UP_LEFT
            elif self.last_key == 'right':
                self.image=CHARACTER_HAMMER_UP_RIGHT
            if keys[pygame.K_p]:
                self.hit = True
                if self.last_key == 'left':
                    self.image=CHARACTER_HAMMER_LEFT
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

        if self.equiped==True:
            if keys[pygame.K_p]:
                self.hit = True
                if self.last_key == 'left':
                    self.image=CHARACTER_HAMMER_LEFT  
            
                elif self.last_key == 'right':
                    self.image = CHARACTER_HAMMER_RIGHT    

        

            

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

        
        
        
#=============================================================================================
# Class for DK

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, img):
        pygame.sprite.Sprite.__init__(self)       
        self.image=img
        self.rect = pygame.Rect(x, y, width, height)
        self.image_list = [DK_IMG,DK_IMG_DIREITA,DK_IMG_ESQUERDA]
        self.i=0
        self.ultima_i=0
    def update(self):
        agora=pygame.time.get_ticks()
        if agora-self.ultima_i>=500:
            self.i+=1
            self.image=self.image_list[self.i % 3]
            self.ultima_i=agora


#============================================================================================
#Class for fire
class fogo(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, img):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.rect = pygame.Rect(x, y, width, height)
        self.image_list = [FOGO_IMG3, FOGO_IMG, FOGO_IMG2]
        self.i=0
        self.ultima_i=0
    def update(self):
        agora=pygame.time.get_ticks()
        if agora-self.ultima_i>=500:
            self.i+=1
            self.image=self.image_list[self.i % 3]
            self.ultima_i=agora

# Class for barrels

class Barrel(pygame.sprite.Sprite):
    def __init__(self, x, y,width, height, img):

        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.rect = pygame.Rect(x, y, width, height)
        self.speed =-4
        self.y_velocity = 0
        self.i=0
        self.ultima_i=0

    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.y_velocity
        agora=pygame.time.get_ticks()
        if agora-self.ultima_i>=250:
            if self.speed<0:
                self.image_list = [BARRIL_IMG,  BARRIL_IMG_E_BAIXO, BARRIL_IMG_D_BAIXO, BARRIL_IMG_D_CIMA]
            if self.speed>0:
                self.image_list = [BARRIL_IMG, BARRIL_IMG_D_CIMA, BARRIL_IMG_D_BAIXO, BARRIL_IMG_E_BAIXO]

            self.i+=1
            self.image=self.image_list[self.i % 4]
            self.ultima_i=agora

        if character.rect.colliderect(self.rect) or self.rect.colliderect(character.rect):
                self.image = BARRIL_EXPLODE
                

                    
                    
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


class Martelo(pygame.sprite.Sprite):
    def __init__(self, x, y,width, height, img):

        pygame.sprite.Sprite.__init__(self)      
        self.image=img
        self.rect = pygame.Rect(x, y, width, height)
    

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y,width, height,img):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.rect = pygame.Rect(x, y, width, height)
        self.image_list= [BARRIL_EXPLODE,BARRIL_EXPLODE,BARRIL_EXPLODE]
        self.i=0
        self.ultima_i=0

        def update(self):

            agora=pygame.time.get_ticks()
            if agora-self.ultima_i>=500:
                self.i+=1
                self.image=self.image_list[self.i]
                self.ultima_i=agora
                    

            if self.i==len(self.image_list):
                self.kill()

                    # Se ainda não chegou ao fim da explosão, troca de imagem.


# ========================= | Objects | ================================================================================================================================================== 
# (Posicao X, posicao Y, tamanho em X, grosura em Y , (Cor))
# Create platforms
plataforma_inicial=Platform(0,HEIGHT-50, WIDTH, 50, PLATFORM_IMG_i)
PLATFORMS=[plataforma_inicial]
STAIRS=[]

for i in range(1,6):
    if (-1)**i < 0:
        EIXO_X_PLATAFORMA = 0
        EIXO_X_ESCADA=WIDTH-100
    else:
        EIXO_X_PLATAFORMA=70
        EIXO_X_ESCADA=80


    PLATFORMS.append(Platform(EIXO_X_PLATAFORMA, (HEIGHT-50)-150*i,  PLATFORM_WIDTH, PLATFORM_HEIGHT, PLATFORM_IMG))
    if i == 5 :
        STAIRS.append(Stair(EIXO_X_ESCADA-80, (HEIGHT-30)-150*i, STAIR_WIDTH ,STAIR_HEIGHT , STAIR_IMG))
    else:
        STAIRS.append(Stair(EIXO_X_ESCADA, (HEIGHT-30)-150*i, STAIR_WIDTH ,STAIR_HEIGHT , STAIR_IMG))
#stair6 = Stair(320, 950-870, 50, 120, WHITE)

# Create character   (0,HEIGHT-50, WIDTH, 50, RED)
character = Character(CHARACTER_X,CHARACTER_Y,CHARACTER_WIDTH,CHARACTER_HEIGHT,CHARACTER_IMG)
DK= Enemy( WIDTH-(DK_WIDTH+20) , 20 ,DK_WIDTH, DK_HEIGHT, DK_IMG)
fogo = fogo (CHARACTER_X-60, CHARACTER_Y-70 ,FOGO_WIDTH, FOGO_HEIGHT, FOGO_IMG)
martelo = Martelo(820, 470, MARTELO_WIDTH, MARTELO_HEIGHT, MARTELO_IMG)
#x_barrilquebrado = barrel.rect.x
#x_barrilquebrado = barrel.rect.y
#barrelhit = barrelhit(x_barrilquebrado, y_barrilquebrado, BARREL_WIDTH, BARREL_HEIGHT, BARRIL_IMG)
listamartelo=pygame.sprite.Group()
listamartelo.add(martelo)
gravity = 0.4

running = True
clock = pygame.time.Clock()

ultimo_barril= 0
game_over = False
hitbarrel = False


pygame.mixer.music.play(loops=-1)
TIME = 0
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
        #ganhouu        for stair in STAIRS:
        if character.rect.colliderect(stair.rect):     
            if character.rect.y <= 50:
                game_over = True
    for platform in PLATFORMS:
        screen.blit(platform.image, platform.rect)


    if character.equiped:
        TIME += 1
        timewithammer = font.render("Tempo com Martelo :  " + str(600-TIME), True, (255, 255, 255))
        screen.blit(timewithammer, (200, 10))
    if TIME == 600:
        character.equiped = False
        TIME = 0
    if not game_over:
        for barrel in barrels:
            barrel.update()
            screen.blit(barrel.image, barrel.rect)
            

# ==============================================colisao baril e mario ===================================
        for barrel in barrels:

            if character.rect.colliderect(barrel.rect):
                if not character.hit:
                    savedscore[nplayer+str(np)] = score*100
                    np += 1
                    score = 0
                    print(savedscore)
                    game_over = True
                else:
                    barrel.velocity=0
                    barrel.y_velocity = 0
                    martelosom.play()
                    barrel.update()
                    screen.blit(barrel.image, barrel.rect)
                    hitbarrel = True
                    score += 1
                    time.sleep(0.2)
                    barrel.rect.y = 10000000
                    break
            else:        
                if (barrel.rect.y+6 > character.rect.y) and (barrel.rect.y-6 < character.rect.y) :
                        score+=0.5
            if barrel.rect.colliderect(fogo.rect) :
                Explosao=Explosion(barrel.rect.x, barrel.rect.y, BARREL_WIDTH, BARREL_HEIGHT,BARRIL_EXPLODE)
                Explosao.update()
                screen.blit(Explosao.image, Explosao.rect)
                score+=1
                barrel.velocity=0
                barrel.rect.x = -10
                barrel.rect.y = 10000000
                barrel.y_velocity = 0
                barrel.speed = 0

        spawn_interval = random.randint(1500, 2000)
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
        
        score_text = font.render("Score: " + str(score*100), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        pygame.display.update()

    else:
        game_over_message()

    pygame.display.flip()
    clock.tick(50)




pygame.quit()

