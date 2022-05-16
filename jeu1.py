import pygame # importation des bonnes bibliothèques
import random
import time
import globals


###############################################################################
#####                         JEU MEMORY                                  #####
###############################################################################

# Variable du jeu de memo
lCarte = 74 # largeur d'une carte
hCarte = 115 # hauteur d'une carte
lEspace = 11 # espacement en largeur entre deux cartes
hEspace = 11 # espacement en hauteur entre deux cartes
lNbCarte = 6 # nombre de colone de cartes
hNbCarte = 3 # nombre de ligne de cartes
color = (255, 0, 0) # couleur du quadrillage sous les cartes en rouge
nbcartes = lNbCarte * hNbCarte # nombre total de cartes
tmemo = [[99 for i in range(lNbCarte)] for j in range(hNbCarte)] # tableau des numéro des cartes
tmemocart = [[0 for i in range(lNbCarte)] for j in range(hNbCarte)] # tableau des cartes retournées
posxcarte = 99  # position en x (colone) de la carte selectionnée
posycarte = 99 # position en y (ligne) de la carte sélectionnée
# le numéro de la carte sélectionnée sera : tmemo[posycarte][posxcarte]
tempscartesvisible = 1 # temps où les cartes sont visibles
tempsgagne = 10 # temps où le message gagné est affiché
decal_larg=262 # décalage du bord de l'écran en largeur 
decal_haut=136 # décalage du bord de l'écran en hauteur



continuer_jeu = 1
termine=False

class Jeu1():

  def quadrillage(screen): 
    """ screen est l'écran du jeu pour l'affichage. Fonction qui affiche le quadrillage rouge derrière les cartes. Cette fonction ne revoie rien (fonction d'affichage)."""

    for i in range(lNbCarte):
            for j in range(hNbCarte):
                pygame.draw.rect(
                    screen, color,
                    pygame.Rect(decal_larg+(i * lEspace) + lEspace + (i * lCarte),
                                decal_haut+(j * hEspace) + hEspace+ (j * hCarte), lCarte, hCarte), 2)
    



  def cartedos(screen): 
    """ screen est l'écran du jeu pour l'affichage. Fonction qui affiche l'image du dos descartes du mémory. Cette fonction ne revoie rien (fonction d'affichage)."""
    
    image= pygame.image.load("cartes/dos.png").convert_alpha()
    for i in range (lNbCarte):
        for j in range(hNbCarte):
            screen.blit(image, (decal_larg+(i*lEspace)+lEspace + (i*lCarte), decal_haut+(j*hEspace)+hEspace + (j*hCarte)))


  def initmemo(): 
    """ Aucun paramètre d'entrée. Fonction qui rempli la liste tmemo représentant le tableau de memory avec les numéros des cartes correspondant au nom des fichiers sans le png. Cette fonction ne revoie rien."""
    for i in range(1,int (((nbcartes/2)+1))):
        x = random.randrange(0, nbcartes)
        bsortie = False
        j=0
        while bsortie == False:
            if tmemo [int (x/lNbCarte)][x%lNbCarte]  ==99 :
                tmemo [int (x/lNbCarte)][x%lNbCarte] = i
                j=j+1
            if j==2:
                bsortie =True
            x = random.randrange(0, nbcartes)


  def selectcarte (posx,posy,screen):
    """ posx est un entier: postion en x de la souris lors du clic, posy est un entier : position en y de la souris lors du clic, screen est l'écran du jeu pour l'affichage. Fonction qui affiche la carte en fonction de la position cliquée. Cette fonction revoie le numéro de la carte retournée ou une chaine vide si l'on a cliqué à coté d'une carte ou sur une carte retournée."""
    
    cartx = 99
    carty = 99
    global posxcarte
    global posycarte
    retcarte = ""
    for i in range (lNbCarte):
      if posx >=decal_larg+(i*lEspace)+lEspace + (i*lCarte) and posx <=decal_larg+(i*lEspace)+lEspace + (i*lCarte)+lCarte :
        cartx = i

    for j in range(hNbCarte):
      if posy >= decal_haut+(j*hEspace)+hEspace + (j*hCarte) and posy <=decal_haut+(j*hEspace)+hEspace + (j*hCarte) +hCarte:
        carty = j


    if cartx != 99 and carty!= 99:
      if tmemocart[carty][cartx] == 0 :
        tmemocart[carty][cartx] =1
        posxcarte = cartx
        posycarte = carty
        retcarte = str(tmemo[carty][cartx])
        imagefic = str(tmemo[carty][cartx])+".png"
        image= pygame.image.load("cartes/"+imagefic).convert_alpha()
        screen.blit(image, (decal_larg+(cartx*lEspace)+lEspace + (cartx*lCarte) ,decal_haut+(carty*hEspace)+hEspace + (carty*hCarte)))
        pygame.display.flip()




    return retcarte



  def verifmemo (carte1 , carte2 , posxcarte1 , posycarte1 ,posxcarte2 ,posycarte2, screen):
    """ carte1 est une chaine: le numéro de la premiere carte retournée, carte2 estune chaine: le numéro de la dexieme carte retournée, posxcarte1 est un entier: la postion en x de la carte 1 dans les listes tmemocart et tmemo , posycarte1 est un entier: la postion en y de la carte 1 dans les listes tmemocart et tmemo, posxcarte2 est un entier: la postion en x de la carte 2 dans les listes tmemocart et tmemo, posycarte2 est un entier: la postion en y de la carte 2 dans les listes tmemocart et tmemo, screen est l'écran du jeu pour l'affichage. Cette procedure vérifie si les 2 artes retournée sont identiques et renseigne la liste tmemocart des cartes retournées.Cette fonction ne revoie rien."""

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



  def affichejeu (screen): 
    """ screen est l'écran du jeu pour l'affichage. Fonction affiche le cartes ou les dos des cartes en fonction de leurs état dans tmemocart. Cette fonction ne revoie rien (fonction d'affichage)."""

    for i in range (lNbCarte):
      for j in range(hNbCarte):
        if tmemocart [j][i]==0:
          Jeu1.affichedos(decal_larg+(i*lEspace)+lEspace + (i*lCarte), decal_haut+(j*hEspace)+hEspace + (j*hCarte),screen)
        else:
          Jeu1.affichecarte (decal_larg+(i*lEspace)+lEspace + (i*lCarte), decal_haut+(j*hEspace)+hEspace + (j*hCarte),tmemo[j][i],screen)

    pygame.display.flip()


  def affichedos (dox,doy,screen): 
    """ dox est un entier: la position en x du dos de la carte, doy est un entier:la position en y du dos de la carte, screen est l'écran du jeu pour l'affichage. Fonction affiche le dos d'une carte à la position dox,doy. Cette fonction ne revoie rien (fonction d'affichage)."""
    
    image= pygame.image.load("cartes/dos.png").convert_alpha()
    screen.blit(image, (dox, doy))
    pygame.display.flip()

  def affichecarte (cax,cay,ca,screen): 
    """ cax est un entier: la position en x de la carte, cay est un entier:la position en y de la carte, ca est un entier: le numéro du fichier de la carte, screen est l'écran du jeu pour l'affichage. Fonction affiche la carte à la position cax,cay. Cette fonction ne revoie rien (fonction d'affichage)."""
    
    imagefic = str(ca)+".png"
    image= pygame.image.load("cartes/"+imagefic).convert_alpha()
    screen.blit(image, (cax,cay))
    pygame.display.flip()


  def validmemo (): 
    """ aucun paramètres. Fonction qui vérifie si le mémory est terminé. Cette fonction revoie true si le mémory est terminé sinon false."""
    ret= True
    for i in range (lNbCarte):
      for j in range(hNbCarte):
        if tmemocart[j][i] == 0:
          ret=False
    return ret

  def Finjeu1(screen): 
    """screen est l'écran du jeu pour l'affichage. Fonction affiche GAGNE . Cette fonction ne revoie rien (fonction d'affichage)."""

    police = pygame.font.SysFont('arial', 120,True)
    imagetxt = police.render("GAGNE",1,(255,0,0))
    screen.blit(imagetxt,(decal_larg+100,decal_haut + 100))
    pygame.display.flip()
    time.sleep(tempsgagne)

    globals.player.position[1] += -150
    globals.player.place = 'MAZE' 
    globals.background_music()

  def init():
    """Aucun paramètres en entrée. Fonction d'initialisation et de lancement du jeu de mémory. Cette fonction ne revoie rien."""
   
    screen = pygame.display.get_surface()
    intmaison= pygame.image.load("assets/intmaison1.png").convert_alpha()
    intmaison=pygame.transform.scale(intmaison,(1024,650))
    screen.blit(intmaison, (0,0))
    #screen.fill(pygame.Color("black")) # on met un écran noir sur la totalité de l'écran
    pygame.display.flip()
    pygame.display.set_caption("Escape - Adventure (memory)         CHRONO ==> "+ globals.chrono()) # association du nom de la fenetre et affichage du chrono

    file= "assets/Memory1.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    runningson = True
    while runningson:
      #pygame.display.set_caption("Escape - Adventure (memory)         CHRONO ==> "+ globals.chrono()) # association du nom de la fenetre et affichage du chrono
      runningson = pygame.mixer.music.get_busy()
      
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

    affchrono = 0
    while continuer_jeu:
      affchrono +=1 
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
            else:
              # hack to win quickly
              if clickx<10 and  clicky<10:
                termine = True
      if affchrono >= 1000:
        affchrono = 0
        pygame.display.set_caption("Escape - Adventure (memory)         CHRONO ==> "+ globals.chrono()) # association du nom de la fenetre et affichage du chrono
      if termine ==True:
        file= "assets/Memory1.mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        Jeu1.Finjeu1(screen)
        continuer_jeu = 0

