import pygame
pygame.init()

# creation de la fenetre
pygame.display.set_mode((800, 600))
pygame.display.set_caption("Find Eve")
print()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
