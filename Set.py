import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
WIDTH = 1000
HEIGHT = 780

def game_over_message():
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over - Press any key to restart", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)

# Reset the game state
def reset_game():
    global game_over
    game_over = False
    character.rect.x = 100
    character.rect.y = 930
    character.velocity = 0
    character.on_ground = False
    character.on_stair = False
    barrels.clear()
# Class for platforms
class Platform:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

# Class for stairs
class Stair:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

# Class for the character
class Character:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.velocity = 0
        self.jump_power = 12
        self.on_ground = False
        self.on_stair = False

    def update(self):
        self.velocity += gravity
        self.rect.y += self.velocity

        for platform in PLATFORMS:
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

        for stair in STAIRS:
            if self.rect.colliderect(stair.rect):
                self.rect.bottom = stair.rect.top
                self.velocity = 0
                self.on_ground = True
                self.on_stair = True
                break
        else:
            self.on_stair = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= 3
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += 3

        if self.on_stair:
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.rect.y -= 2
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.rect.y += 2

        if self.rect.bottom > 950:
            self.rect.bottom = 950
            self.velocity = 0
            self.on_ground = True

        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity = 0
        # Deixar ele so dentro da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTHdd

    def jump(self):
        if self.on_ground or self.on_stair:
            self.velocity = -self.jump_power
            self.on_ground = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

# Class for barrels
class Barrel:
    def __init__(self, x, y, radius, color, speed):
        self.rect = pygame.Rect(x, y - radius, radius * 2, radius * 2)
        self.color = color
        self.speed = speed
        self.y_velocity = 0

    def update(self):
        self.rect.x -= self.speed
        self.rect.y += self.y_velocity

        for platform in PLATFORMS:
            if self.rect.colliderect(platform.rect):
                self.rect.bottom = platform.rect.top
                self.y_velocity = 0
                break
        else:
            self.y_velocity += gravity

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

# Set up display and initialize Pygame

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Donkey Kong Arcade")

# ========================= | Objects | ================================================================================================================================================== 
# (Posicao X, posicao Y, tamanho em X, grosura em Y , (Cor))
# Create platforms
plataforma_inicial=Platform(0,HEIGHT-50, WIDTH, 50, RED)
PLATFORMS=[plataforma_inicial]
STAIRS=[]

for i in range(1,5):
    if (-1)**i < 0:
        EIXO_X_PLATAFORMA = 0
        EIXO_X_ESCADA=WIDTH-70
    else:
        EIXO_X_PLATAFORMA=50
        EIXO_X_ESCADA=70
    PLATFORMS.append(Platform(EIXO_X_PLATAFORMA, (HEIGHT-50)-150*i, WIDTH-40, 20, RED))
    STAIRS.append(Stair(EIXO_X_ESCADA, (HEIGHT-50)-150*i, 20, 150, WHITE))
#stair6 = Stair(320, 950-870, 50, 120, WHITE)

# Create character   (0,HEIGHT-50, WIDTH, 50, RED)
character = Character(100, (HEIGHT-50-20), 20, 50, WHITE)
# Create barrels
barrels = []
barrel_radius = 10
barrel_speed = 4
for platform in PLATFORMS:
    x = random.randint(830, 1060)
    y = platform.rect.top - barrel_radius
    barrel = Barrel(x, y, barrel_radius, RED, barrel_speed)
    barrels.append(barrel)
# Check for collision between character and barrels
for barrel in barrels:
    if character.rect.colliderect(barrel.rect):
        running = False  # Set running to False to end the game
        break



# Set gravity value
gravity = 0.6
# Game loop

# Game loop
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
                character.jump()

    screen.fill((0, 0, 0))

    for platform in PLATFORMS:
        platform.draw(screen)

    for stair in STAIRS:
        stair.draw(screen)

    if not game_over:
        for barrel in barrels:
            barrel.update()
            barrel.draw(screen)

        for barrel in barrels:
            if character.rect.colliderect(barrel.rect):
                game_over = True
                break
        spawn_timer += clock.get_rawtime()
        if spawn_timer >= spawn_interval:
            for platform in PLATFORMS:
                x = random.randint(830, 1060)
                y = platform.rect.top - barrel_radius
                barrel = Barrel(x, y, barrel_radius, RED, barrel_speed)
                barrels.append(barrel)
            spawn_timer = 0

        character.update()
        character.draw(screen)
    else:
        game_over_message()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


