import pygame # importation des bonnes bibliothèques
import pyscroll
import pytmx
from player import Joueur
from pytmx.util_pygame import load_pygame
import math
pygame.init()


class Jeu():
    def __init__(self):  # fonction qui se s'occupe du chargement du jeu
        # création d'une fenêtre
        self.screen = pygame.display.set_mode((1024, 768))
        pygame.display.set_caption("Escape - Adventure") # association du nom de la fenetre

        # charger la carte
        tmx_data = load_pygame("assets/map.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(
            map_data, self.screen.get_size())
        map_layer.zoom = 3

        self.walls = tmx_data.get_layer_by_name("buissons").data 

        # initialisation du joueur
        player_position = tmx_data.get_object_by_name("player")
        self.player = Joueur(player_position.x, player_position.y)

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(
            map_layer=map_layer, default_layer=3) #postion du personnage par rapport aux calques(ex: mettre a 3 au lieu de 2 pour pas que le personnage soit en dessous des buissons)
        self.group.add(self.player)
    # déplacement du personnage


    def handle_input(self):
      pressed = pygame.key.get_pressed()
      if pressed[pygame.K_UP]: #déplacement vers le haut
        self.player.move_up()
        self.player.change_animation("up")
        if (self.checkColission(self.player.position)): # regarde si il y a un buisson avant de tourner
          self.player.move_down()
      elif pressed[pygame.K_DOWN]: # déplacement vers le bas 
        self.player.move_down()
        self.player.change_animation("down")
        if (self.checkColission(self.player.position)): # regarde si il y a un buisson avant de tourner
          self.player.move_up()
      elif pressed[pygame.K_LEFT]: # déplacement vers la gauche 
        self.player.move_left()
        self.player.change_animation("left")
        if (self.checkColission(self.player.position)): # regarde si il y a un buisson avant de tourner 
          self.player.move_right()
      elif pressed[pygame.K_RIGHT]: # déplacement vers la droite
        self.player.move_right()
        self.player.change_animation("right")
        if (self.checkColission(self.player.position)): # regarde si il y a un buisson avant de tourner
          self.player.move_left()

          
    #pour pas que le personnage depasse pas les buissons
    def checkColission(self, position):
      x = int(round(position[0] / 32, 0))
      y = int(round(position[1] / 32, 0))
      if (x < 0) or (y < 0) or (x > 49) or (y > 49):
        return True
      if self.walls[y][x] != 0:
        return True
      else:
        return False

    def run(self):

        # boucle infini qui fait tourner le jeu
        running = True

        while running:
            self.handle_input() 
            self.group.update() #actualisation du groupe
            self.group.center(self.player.rect.center) #dessiner les entites du groupe
            # pour dessiner directement les calques sur l'ecran
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


pygame.quit()
