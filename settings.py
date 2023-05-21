# ========================== | Imports | ==============================
import pygame
import random
from sprites import *
# ========================== | Tamanhos | ==============================
WIDTH = 800  
HEIGHT = 1000

## ========================= | Objects | ============================== 
# (Posicao X, posicao Y, tamanho em X, grosura em Y , (Cor))
platform1 = Platform(0, 950, 800, 20, (255, 0, 0))
platform2 = Platform(0, 950-150, 800, 20, (255, 0, 0))
platform3 = Platform(0, 950-300, 800, 20, (255, 0, 0))
platform4 = Platform(0, 950-450, 800, 20, (255, 0, 0))
platform5 = Platform(0, 950-600, 800, 20, (255, 0, 0))
platform6 = Platform(0, 950-750, 800, 20, (255, 0, 0))