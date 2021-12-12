import pygame
pygame.init()

# creation de la fenetre
pygame.display.set_mode((800, 600))
pygame.display.set_caption("Find Eve")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
