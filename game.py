import pygame # importation des bonnes bibliothèques
import pyscroll
import globals
import time
from pytmx.util_pygame import load_pygame
from jeu1 import Jeu1
from jeu2 import Jeu2
from jeu3 import Jeu3
from key import Cle

pygame.init()
clock = pygame.time.Clock()


class Game():

    def __init__(self):  # fonction qui se s'occupe du chargement du jeu
        # création d'une fenêtre
        #self.screen = pygame.display.set_mode((400, 400))

       
        self.screen = pygame.display.set_mode((1024, 650))
        globals.chrono_init() # initialisation du chrono 
        pygame.display.set_caption("Escape - Adventure          CHRONO ==> "+ globals.chrono()) # association du nom de la fenetre et affichage du chrono

        # charger la carte
        tmx_data = load_pygame("assets/map.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(
            map_data, self.screen.get_size())
        map_layer.zoom = 3

        self.walls = tmx_data.get_layer_by_name("buissons").data
        self.locks = tmx_data.get_layer_by_name("cadenas").data
        
        # initialisation du joueur
        player_position = tmx_data.get_object_by_name("player")
        self.player = globals.player
        self.player.init(player_position.x, player_position.y)
        

        self.cles =[Cle(40,39,'JEU1'),Cle(30,7,'JEU3'),Cle(40,22,'JEU2')]

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(
            map_layer=map_layer, default_layer=3) #position du personnage par rapport aux calques(ex: mettre a 3 au lieu de 2 pour pas que le personnage soit en dessous des buissons)
        self.group.add(self.player)
        self.group.add(self.cles)

        # pygame.time.Clock().tick(100)
        globals.background_music()

    # déplacement du personnage


    def handle_input(self):
      
      pressed = pygame.key.get_pressed()
      if pressed[pygame.K_UP]: #déplacement vers le haut
        self.player.move_up()
        # print(self.player.position)
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

  
  
    def checkMaison(self):

      position = self.player.position;
      x = int(round(position[0] / 32, 0))
      y = int(round(position[1] / 32, 0))
      if (x < 0) or (y < 0) or (x > 49) or (y > 49):
        return
      if self.locks[y][x] != 0:
          if self.player.jeux == 0 and self.player.hasKey('JEU1'):
            self.player.place = 'JEU1'
            Jeu1.init()
            self.player.jeux += 1
          elif self.player.jeux == 1 and self.player.hasKey('JEU2'):
              self.player.place = 'JEU2'
              Jeu2.init()   
              self.player.jeux += 1
          elif self.player.jeux == 2 and self.player.hasKey('JEU3'):
                self.player.place = 'JEU3'
                Jeu3()
          else:
            file= "assets/alertsound.mp3"
            pygame.mixer.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            runningson = True
            while runningson:
              runningson = pygame.mixer.music.get_busy()
            globals.background_music()


    def checkKeys(self):
      for cle in self.cles:
        if cle.check_colission():
          self.cles.remove(cle)
          self.group.remove(cle)
          globals.background_music()

    def run(self):
        #Affichage des règles
        screen = pygame.display.get_surface()
        intmaison= pygame.image.load("assets/intmaisonregles.png").convert_alpha()
        intmaison=pygame.transform.scale(intmaison,(1024,650))
        regle = pygame.image.load("assets/regles.png").convert_alpha()
        screen.blit(intmaison, (0,0))
        screen.blit(regle, (92,45))

       
        
        debutjeu = True
        pygame.display.flip()
    
        while debutjeu:
        
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    debutjeu = False

        globals.chrono_init() # initialisation du chrono 
        pygame.display.set_caption("Escape - Adventure          CHRONO ==> "+ globals.chrono()) # association du nom de la fenetre et affichage du chrono




      
        # boucle infini qui fait tourner le jeu
        fin = False
        running = True
        affchrono = 0
        while running:
          affchrono += 1
          if self.player.place == 'MAZE':
            self.handle_input()
            self.group.update() #actualisation du groupe
            self.group.center(self.player.rect.center)                     #dessiner les entites du groupe
            # pour dessiner directement les calques sur l'ecran
            self.group.draw(self.screen)
            if affchrono >= 50 : 
              affchrono = 0
              pygame.display.set_caption("Escape - Adventure          CHRONO ==> "+ globals.chrono()) # association du nom de la fenetre et affichage du chrono
            pygame.display.flip()

            
            self.checkMaison() # on regarde si on est sur une maison

            self.checkKeys()

            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

            if self.player.position[1] <= 1 :
              #on a terminé le jeu
              fin = True
              running = False
        if fin == False:
          pygame.quit()
        else: 
          # on afficher FIN 
          imgfin = pygame.image.load("assets/theend.jpg").convert_alpha()
          screen.blit(imgfin, (374,233))
          pygame.display.flip()
          time.sleep(20)
          pygame.quit()