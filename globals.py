from player import Joueur
import pygame
import time

player = Joueur()
chronodebut = 0
lecran = 1024 #dimension de l'ecran
hecran = 650
decal_larg=262 # décallage par rapport au bord de l'écran
decal_haut=111
larg_game= lecran-(decal_larg*2) #dimensions de la zone de quizz
haut_game= hecran-(decal_haut*2)

colornoir = (0,0,0)
colorrouge = (255,0,0)
colorvert = (0,255,0)
colorjaune = (255,255,0)
colorbleu = (0,0,255)

def background_music():
    file= "assets/backgroundmusic.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)

def chrono_init ():
  global chronodebut
  chronodebut = int (time.time())  # récupération du temps en secondes dpuis le 1er janvier 1970

def chrono ():
  global chronodebut
  diftime = int(time.time()) - chronodebut  # calcul du temps en secondes écoulé depuis le debut du jeu 
  #conversion de ce temps en heures minutes secondes
  heures = int (diftime /3600)
  minutes = int ((diftime-heures*3600)/60)
  secondes = diftime-heures*3600-minutes*60
  return (str(heures)+ " h " + str(minutes) + " m " + str(secondes) + " s")
def texte_titre(titre,color,fenetre):
    policetitre = pygame.font.SysFont('arial', 40,True)
    imagetxt = policetitre.render(titre,1,color)# création du mot quizz
    fenetre.blit(imagetxt,(decal_larg+int((larg_game/2)-(len(titre)/2*25)   ),decal_haut+5))# affichage du mot quizz

def background_house(fenetre):
    intmaison= pygame.image.load("assets/intmaison1.png").convert_alpha()
    intmaison=pygame.transform.scale(intmaison,(1024,650))
    fenetre.blit(intmaison, (0,0))
    
    pygame.draw.rect(fenetre,colornoir,pygame.Rect(decal_larg,decal_haut,larg_game,haut_game))


def play_sound(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play() # If the loops is -1 then the music will repeat indefinitely.
    runningson = True
    while runningson:
        runningson = pygame.mixer.music.get_busy()

def pass_game():
    player.position[1] += -150
    player.place = 'MAZE' 
    background_music()

def abandon_game():
    player.position[1] += 10
    player.place = 'MAZE' 
    background_music()

def hack_win(event):
    if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
        clickx = pygame.mouse.get_pos()[0]
        clicky = pygame.mouse.get_pos()[1]
        if clickx<10 and  clicky<10:
            return True
    return False
  
  