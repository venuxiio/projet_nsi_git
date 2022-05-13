import pygame # importation des bonnes bibliothèques
import pyscroll
import pytmx
from player import Joueur
from pytmx.util_pygame import load_pygame

import math
import random
import time


pygame.init()
efface = False # variable globale qui indique si l'on se trouve dans une maison qui permet de ne plus afficher le labyrinthe et les déplacements du personnage
finjeu1=False # variable globale qui indique que l'on a gagné le jeu et qui réactive la'affichage du labyrinthe et le déplacement du personnage.

# Variable du jeu de memo
lCarte = 74 # largeur d'une carte
hCarte = 115 # hauteur d'une carte
lEspace = 11 # espacement en largeur entre deux cartes
hEspace = 11 # espacement en hauteur entre deux cartes
lNbCarte = 7 # nombre de colone de cartes
hNbCarte = 4 # nombre de ligne de cartes
color = (255, 0, 0) # couleur du quadrillage sous les cartes en rouge
nbcartes = lNbCarte * hNbCarte # nombre total de cartes
tmemo = [[99 for i in range(lNbCarte)] for j in range(hNbCarte)] # tableau des numéro des cartes
tmemocart = [[0 for i in range(lNbCarte)] for j in range(hNbCarte)] # tableau des cartes retournées
posxcarte = 99  # position en x (colone) de la carte selectionnée
posycarte = 99 # position en y (ligne) de la carte sélectionnée
# le numéro de la carte sélectionnée sera : tmemo[posycarte][posxcarte]
tempscartesvisible = 1 # temps où les cartes sont visibles
tempsgagne = 10 # temps où le message gagné est affiché


continuer_jeu = 1
termine=False


class Game():

    def __init__(self):  # fonction qui se s'occupe du chargement du jeu
        # création d'une fenêtre
        #self.screen = pygame.display.set_mode((400, 400))
        self.screen = pygame.display.set_mode((1024, 650))
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
      global efface
      if efface == False:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: #déplacement vers le haut
          self.player.move_up()
          print(self.player.position)
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

        self.checkMaison(self.player.position) # on regarde si on est sur une maison



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

    def checkMaison(self, position):
      global efface

      # Maison1
      if position [0] >496 and position [0] <528 and position [1] >1023 and position [1] <1086 and efface == False:
        print ("Efface")
        efface = True
        Jeu1.jmemo(self)

        return True

      else:
        return False


    def run(self):
        global efface
        global finjeu1
        # boucle infini qui fait tourner le jeu
        running = True

        while running:
            self.handle_input()
            self.group.update() #actualisation du groupe
            self.group.center(self.player.rect.center) #dessiner les entites du groupe
            # pour dessiner directement les calques sur l'ecran
            self.group.draw(self.screen)
            if efface == False:
              pygame.display.flip()
            if finjeu1==True:
              self.player.position[0]=500
              self.player.position[1]=1020
              efface = False
              finjeu1 = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


        pygame.quit()


###############################################################################
#####                         JEU MEMORY                                  #####
###############################################################################

class Jeu1():

  def quadrillage(screen): # fonction qui affiche le quadrillage derrière les cartes (rectangles rouges)
    for i in range(lNbCarte):
            for j in range(hNbCarte):
                pygame.draw.rect(
                    screen, color,
                    pygame.Rect((i * lEspace) + lEspace + (i * lCarte),
                                (j * hEspace) + hEspace+ (j * hCarte), lCarte, hCarte), 2)
    return



  def cartedos(screen): # fonction qui affiche l'image du dos des cartes du mémory
      image= pygame.image.load("cartes/dos.png").convert_alpha()
      for i in range (lNbCarte):
          for j in range(hNbCarte):
              screen.blit(image, ((i*lEspace)+lEspace + (i*lCarte), (j*hEspace)+hEspace + (j*hCarte)))


  def initmemo(): # fonction qui remplit le tableau tmemo avec les valeurs des cartes
      for i in range(1,int (((nbcartes/2)+1))):
          x = random.randrange(0, nbcartes)
          bsortie = False
          j=0
          while bsortie == False:
              if tmemo [int (x/lNbCarte)][x%lNbCarte]  ==99 :
                  tmemo [int (x/lNbCarte)][x%lNbCarte] = i
                  j=j+1
                  print(tmemo)
              if j==2:
                  bsortie =True
              x = random.randrange(0, nbcartes)
      print(tmemo)

  def selectcarte (posx,posy,screen):
    cartx = 99
    carty = 99
    global posxcarte
    global posycarte
    retcarte = ""
    for i in range (lNbCarte):
      if posx >=(i*lEspace)+lEspace + (i*lCarte) and posx <= (i*lEspace)+lEspace + (i*lCarte)+lCarte :
        cartx = i

    for j in range(hNbCarte):
      if posy >= (j*hEspace)+hEspace + (j*hCarte) and posy <=(j*hEspace)+hEspace + (j*hCarte) +hCarte:
        carty = j


    if cartx != 99 and carty!= 99:
      if tmemocart[carty][cartx] == 0 :
        tmemocart[carty][cartx] =1
        posxcarte = cartx
        posycarte = carty
        retcarte = str(tmemo[carty][cartx])
        imagefic = str(tmemo[carty][cartx])+".png"
        image= pygame.image.load("cartes/"+imagefic).convert_alpha()
        screen.blit(image, ((cartx*lEspace)+lEspace + (cartx*lCarte) ,(carty*hEspace)+hEspace + (carty*hCarte)))
        pygame.display.flip()
        print(tmemo)


    print(retcarte)
    return retcarte



  def verifmemo (carte1 , carte2 , posxcarte1 , posycarte1 ,posxcarte2 ,posycarte2, screen):

    if carte1 != carte2:
        tmemocart [posycarte1][posxcarte1] =0
        tmemocart [posycarte2][posxcarte2] =0


    carte1 =""
    carte2 =""
    posxcarte1 =99
    posxcarte2 =99
    posycarte1 =99
    posycarte2 =99

    Jeu1.affichejeu(screen)



  def affichejeu (screen): # affiche les dos et les cartes en fonction des 0 (dos des cartes) et des 1 (on retourne les cartes) de tmemocarte
    for i in range (lNbCarte):
      for j in range(hNbCarte):
        if tmemocart [j][i]==0:
          Jeu1.affichedos((i*lEspace)+lEspace + (i*lCarte), (j*hEspace)+hEspace + (j*hCarte),screen)
        else:
          Jeu1.affichecarte ((i*lEspace)+lEspace + (i*lCarte), (j*hEspace)+hEspace + (j*hCarte),tmemo[j][i],screen)

    pygame.display.flip()


  def affichedos (dox,doy,screen): # affiche le dos de la carte à l'emplacement passé en paramètre
    image= pygame.image.load("cartes/dos.png").convert_alpha()
    screen.blit(image, (dox, doy))
    pygame.display.flip()

  def affichecarte (cax,cay,ca,screen): # affiche la carte à l'emplacement passé en paramètre
    imagefic = str(ca)+".png"
    image= pygame.image.load("cartes/"+imagefic).convert_alpha()
    screen.blit(image, (cax,cay))
    pygame.display.flip()


  def validmemo (): #vérifier si on a fini le memo
    ret= True
    for i in range (lNbCarte):
      for j in range(hNbCarte):
        if tmemocart[j][i] == 0:
          ret=False
    return ret

  def Finjeu1(screen): # dit gagné si on a gagné
    global finjeu1
    police = pygame.font.SysFont('arial', 120,True)
    imagetxt = police.render("GAGNE",1,(255,0,0))
    screen.blit(imagetxt,(100,24+4*115))
    pygame.display.flip()
    time.sleep(tempsgagne)
    finjeu1 = True #renvoie l'affichage du labyrinthe et du personnage derrière la maison


  def jmemo(self):



    screen = pygame.display.get_surface()
    screen.fill(pygame.Color("black")) # erases the entire screen surface
    pygame.display.flip()
    Jeu1.quadrillage(screen)
    Jeu1.cartedos(screen)
    pygame.display.flip()


    Jeu1.initmemo()

    global posxcarte
    global posycarte
    carte = ""
    carte1 = ""
    carte2 = ""
    posxcarte1 = 99
    posxcarte2 = 99
    posycarte1 = 99
    posycarte2 = 99
    posxcarte = 99
    posycarte = 99
    termine=False
    continuer_jeu = 1
    carteretourne = 0


    while continuer_jeu:

      for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
          if pygame.mouse.get_pressed()[0] == True:
            clickx = pygame.mouse.get_pos()[0]
            clicky = pygame.mouse.get_pos()[1]
            
            carte = Jeu1.selectcarte(clickx,clicky,screen)
            if carte != "":
              carteretourne = carteretourne +1
              if carteretourne == 1:
                carte1 = carte
                posxcarte1 = posxcarte
                posycarte1 = posycarte
              if carteretourne == 2 :
                carte2 = carte
                posxcarte2 = posxcarte
                posycarte2 = posycarte
                if carte1 != carte2:
                  time.sleep(tempscartesvisible)
                Jeu1.verifmemo(carte1, carte2, posxcarte1 ,posycarte1 ,posxcarte2, posycarte2, screen)
                carteretourne = 0
                carte = ""
                termine = Jeu1.validmemo()


      if termine ==True:
          Jeu1.Finjeu1(screen)
          continuer_jeu = 0

