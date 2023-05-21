# ========================== | Imports | ==============================
import pygame
import random
from sprites import *
# ========================== | Tamanhos | ==============================
WIDTH = 800  
HEIGHT = 1000
RED = (255, 0, 0)
WHITE = (255, 255, 255)
## ========================= | Objects | ============================== 
# (Posicao X, posicao Y, tamanho em X, grosura em Y , (Cor))
platform1 = Platform(0, 950, 800, 20, RED)
platform2 = Platform(0, 950-150, 800, 20, RED)
platform3 = Platform(0, 950-300, 800, 20, RED)
platform4 = Platform(0, 950-450, 800, 20, RED)
platform5 = Platform(0, 950-600, 800, 20, RED)
platform6 = Platform(0, 950-750, 800, 20, RED)

stair1 = Stair(720, 950-150, 50, 150, WHITE)
stair2 = Stair(30, 950-300, 50, 150, WHITE)
stair3 = Stair(720, 950-450, 50, 150, WHITE)
stair4 = Stair(30, 950-600, 50, 150, WHITE)
stair5 = Stair(720, 950-750, 50, 150, WHITE)