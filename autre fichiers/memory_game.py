import pygame
import random
import time
from pygame.locals import *
lecran = 600
hecran = 600



def quadrillage():
    color = (255,0,0)
    # dessin du cadre

    for i in range (7):
        for j in range(4):
            pygame.draw.rect(fenetre, color, pygame.Rect((i*11)+11 + (i*74), (j*4)+4 + (j*115), 74, 115),  2)
    return