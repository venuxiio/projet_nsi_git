#Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *

x = 0
y = 0
xb = 0
yb = 0
xpas= 5
ecrant=320
#Initialisation de la bibliothèque Pygame
pygame.init()

#Création de la fenêtre
fenetre = pygame.display.set_mode((ecrant, ecrant))
pygame.display.set_caption("Escape - Adventure")
fond = pygame.image.load("labyrinthe3.png").convert()
banana = pygame.image.load("banane.png").convert_alpha()
#fond = pygame.transform.scale(fond,(1640, 1480))
fenetre.blit(fond, (0, 0))
fenetre.blit(banana, (0, 0))
pygame.display.update()
continuer_jeu = 1
while continuer_jeu:
    fenetre.blit(fond, (x, y))
    fenetre.blit(banana, (xb, yb))
    pygame.display.flip()
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer_jeu = 0
            continuer = 0
    if event.type == KEYDOWN:
        if event.key == K_RIGHT:
            xb += xpas
            if xb>=ecrant:
              x=x-ecrant
              xb=0
        if event.key == K_LEFT:
            xb -= xpas
            if xb<0:
              x=x+ecrant
              xb=ecrant
        if event.key == K_UP:
            yb -= xpas
            if yb<0:
              y+=ecrant
              yb=ecrant
        if event.key == K_DOWN:
            yb += xpas
            if 0<=y<=1280:
              if yb>=ecrant:
                y-=ecrant
                yb=0
