import pygame # importation des bonnes bibliothèques
import random
import time
import csv
import globals

###############################################################################
#####                         JEU QUIZZ                                   #####
###############################################################################

# Variable du quizz
lecran = 1024 #dimension de l'ecran
hecran = 650
decal_larg=262 # décallage par rapport au bord de l'écran
decal_haut=80
larg_quizz= lecran-(decal_larg*2) #dimensions de la zone de quizz
haut_quizz= hecran-(decal_haut*2)
# position des ligne pour les réponses
ligneM = decal_haut+int ((haut_quizz/3)*2) # position de la ligne qui sépare la partie question de la partie réponse
ligneB = decal_haut+int (((haut_quizz-decal_haut-ligneM)/2)+ligneM)#position de la ligne qui sépare les deux réponses du haut au deux réponses du bas
ligneV = decal_larg+int (larg_quizz/2)# position de la ligne au milieu qui sépare les questions de droite et les questions de gauche

# position x de l'écriture des questions et des réponses
xquestion = decal_larg+10
xrep1 =decal_larg+10
xrep3 =decal_larg+10
xrep2 = ligneV+10
xrep4 = ligneV+10

# position y de l'écriture des questions et des réponses
yquestion = int((ligneM-decal_haut)/4+decal_haut)
yrep1 = ligneM + 5
yrep2 = ligneM + 5
yrep3 = ligneB + 5
yrep4 = ligneB + 5

carquestion =  int (larg_quizz/8.4)
lignequestion =int ((haut_quizz-20)/20)

carrep = int ((larg_quizz/2)/8.4)
lignerep = int (((ligneB-ligneM)-20)/9)

colornoir = (0,0,0)
colorrouge = (255,0,0)
colorvert = (0,255,0)
colorjaune = (255,255,0)
colorbleu = (0,0,255)

reponsecorrecte= ""
question = ""
rep1 = ""
rep2 = ""
rep3 = ""
rep4 = ""

score = 0
scoremax= 5
pygame.font.init()
police = pygame.font.SysFont('arial', 15,True)
policetitre = pygame.font.SysFont('arial', 40,True)


class Jeu2():

    def textetitre(titre,color,fenetre):
      """ titre est une chaine: le titre du quizz, color est une couleur: la couleur d'affichage du titre, fenetre est l'écran du jeu pour l'affichage. Fonction affiche le titre du quizz. Cette fonction ne revoie rien (fonction d'affichage)."""
      imagetxt = policetitre.render("QUIZZ",1,color)# création du mot quizz
      fenetre.blit(imagetxt,(decal_larg+int((larg_quizz/2)-(len(titre)/2*25)   ),decal_haut+5))# affichage du mot quizz


    def affichescore1(fenetre):
      """fenetre est l'écran du jeu pour l'affichage. Fonction affiche le score du quizz. Cette fonction ne revoie rien (fonction d'affichage)."""
      pygame.draw.rect(fenetre,colornoir,pygame.Rect(int(decal_larg+larg_quizz-150),decal_haut,150,25))
      imagetxt = police.render("Score:",1,colorbleu)
      fenetre.blit(imagetxt,(int(decal_larg+larg_quizz-150   ),decal_haut+5))
      pygame.draw.rect(fenetre,colorbleu,pygame.Rect(int(decal_larg+larg_quizz-100),decal_haut+5,20,20),1)
      pygame.draw.rect(fenetre,colorbleu,pygame.Rect(int(decal_larg+larg_quizz-80),decal_haut+5,20,20),1)
      pygame.draw.rect(fenetre,colorbleu,pygame.Rect(int(decal_larg+larg_quizz-60),decal_haut+5,20,20),1)
      pygame.draw.rect(fenetre,colorbleu,pygame.Rect(int(decal_larg+larg_quizz-40),decal_haut+5,20,20),1)
      pygame.draw.rect(fenetre,colorbleu,pygame.Rect(int(decal_larg+larg_quizz-20),decal_haut+5,20,20),1)

      if score >=1:
          pygame.draw.rect(fenetre,colorbleu,pygame.Rect(int(decal_larg+larg_quizz-100),decal_haut+5,20,20))
      if score >=2:
          pygame.draw.rect(fenetre,colorbleu,pygame.Rect(int(decal_larg+larg_quizz-80),decal_haut+5,20,20))
      if score >=3:
          pygame.draw.rect(fenetre,colorbleu,pygame.Rect(int(decal_larg+larg_quizz-60),decal_haut+5,20,20))
      if score >=4:
          pygame.draw.rect(fenetre,colorbleu,pygame.Rect(int(decal_larg+larg_quizz-40),decal_haut+5,20,20))
      if score >=5:
          pygame.draw.rect(fenetre,colorbleu,pygame.Rect(int(decal_larg+larg_quizz-20),decal_haut+5,20,20))


    def posequestion(x,fenetre,qcm):
      """x est un entier: l'indice de la question, fenetre est l'écran du jeu pour l'affichage, qcm est une liste : la liste des questions du qcm. Fonction pose la question du qcm et affiche les 4 choix. Cette fonction ne revoie rien (fonction d'affichage)."""
      global reponsecorrecte
      global question
      global rep1
      global rep2
      global rep3
      global rep4

      question = qcm[x][0]
      rep1 = qcm[x][1]
      rep2 = qcm[x][2]
      rep3 = qcm[x][3]
      rep4 = qcm[x][4]

      Jeu2.textequestion(question,colorrouge,fenetre)

      Jeu2.reponse1(rep1,1,fenetre)
      Jeu2.reponse2(rep2,1,fenetre)
      Jeu2.reponse3(rep3,1,fenetre)
      Jeu2.reponse4(rep4,1,fenetre)

      reponsecorrecte = int (qcm[x][5])


      pygame.display.flip()

    def textequestion(question,color,fenetre):
      """question est une chaine: la question du QCM,color est une couleur: la couleur de la question, fenetre est l'écran du jeu pour l'affichage. Fonction affiche la question du qcm . Cette fonction ne revoie rien (fonction d'affichage)."""
      pygame.draw.rect(fenetre,colornoir,pygame.Rect(xquestion,yquestion,larg_quizz-10,ligneM-yquestion))

      chainequestionaff = []
      chainequestionaff = Jeu2.decoupechaine(question,carquestion)
      poslignequestion =  0
      for lignequestion in chainequestionaff:
        imagetxt = police.render(lignequestion,1,color)
        fenetre.blit(imagetxt,(xquestion,yquestion + poslignequestion*20))
        poslignequestion +=1
    
       

    def reponse1 (rep1,afftype,fenetre):
      """rep1 est une chaine: le choix 1 du QCM,afftype est un entier: =1 ==> choix texte rouge sur fond noir (choix sélectionnable) =2 ==> choix texte noir sur fond vert (réponse juste) =3 ==> choix texte noir sur fond rouge (réponse fausse), fenetre est l'écran du jeu pour l'affichage. Fonction affiche le choix 1 du qcm . Cette fonction ne revoie rien (fonction d'affichage)."""

      if afftype == 1 :
          color = colorrouge
          colorf = colornoir
      else:
          if afftype == 2 :
              color = colornoir
              colorf = colorvert
          else:
              color = colornoir
              colorf = colorrouge

      pygame.draw.rect(fenetre,colorf,pygame.Rect(decal_larg,ligneM,ligneV-decal_larg,ligneB-ligneM))
      pygame.draw.rect(fenetre,colorrouge,pygame.Rect(decal_larg,ligneM,ligneV-decal_larg,ligneB-ligneM),4)

      chainereponseaff = []
      chainereponseaff = Jeu2.decoupechaine(rep1,carrep)
      poslignereponse =  0
      for lignereponse in chainereponseaff:
        imagetxt = police.render(lignereponse,1,color)
        fenetre.blit(imagetxt,(xrep1,yrep1 + poslignereponse*20))
        poslignereponse +=1

    


    def reponse2 (rep2,afftype,fenetre):
      """rep2 est une chaine: le choix 2 du QCM,afftype est un entier: =1 ==> choix texte rouge sur fond noir (choix sélectionnable) =2 ==> choix texte noir sur fond vert (réponse juste) =3 ==> choix texte noir sur fond rouge (réponse fausse), fenetre est l'écran du jeu pour l'affichage. Fonction affiche le choix 2 du qcm . Cette fonction ne revoie rien (fonction d'affichage)."""

      if afftype == 1 :
          color = colorrouge
          colorf = colornoir
      else:
          if afftype == 2 :
              color = colornoir
              colorf = colorvert
          else:
              color = colornoir
              colorf = colorrouge

      pygame.draw.rect(fenetre,colorf,pygame.Rect(ligneV,ligneM,ligneV-decal_larg,ligneB-ligneM))
      pygame.draw.rect(fenetre,colorrouge,pygame.Rect(ligneV,ligneM,ligneV-decal_larg,ligneB-ligneM),4)


      chainereponseaff = []
      chainereponseaff = Jeu2.decoupechaine(rep2,carrep)
      poslignereponse =  0
      for lignereponse in chainereponseaff:
        imagetxt = police.render(lignereponse,1,color)
        fenetre.blit(imagetxt,(xrep2,yrep2 + poslignereponse*20))
        poslignereponse +=1


    def reponse3 (rep3,afftype,fenetre):
      """rep3 est une chaine: le choix 3 du QCM,afftype est un entier: =1 ==> choix texte rouge sur fond noir (choix sélectionnable) =2 ==> choix texte noir sur fond vert (réponse juste) =3 ==> choix texte noir sur fond rouge (réponse fausse), fenetre est l'écran du jeu pour l'affichage. Fonction affiche le choix 3 du qcm . Cette fonction ne revoie rien (fonction d'affichage)."""
      if afftype == 1 :
          color = colorrouge
          colorf = colornoir
      else:
          if afftype == 2 :
              color = colornoir
              colorf = colorvert
          else:
              color = colornoir
              colorf = colorrouge

      pygame.draw.rect(fenetre,colorf,pygame.Rect(decal_larg,ligneB,ligneV-decal_larg,ligneB-ligneM))
      pygame.draw.rect(fenetre,colorrouge,pygame.Rect(decal_larg,ligneB,ligneV-decal_larg,ligneB-ligneM),4)

      chainereponseaff = []
      chainereponseaff = Jeu2.decoupechaine(rep3,carrep)
      poslignereponse =  0
      for lignereponse in chainereponseaff:
        imagetxt = police.render(lignereponse,1,color)
        fenetre.blit(imagetxt,(xrep3,yrep3 + poslignereponse*20))
        poslignereponse +=1
    
     
    def reponse4 (rep4,afftype,fenetre):
      """rep4 est une chaine: le choix 4 du QCM,afftype est un entier: =1 ==> choix texte rouge sur fond noir (choix sélectionnable) =2 ==> choix texte noir sur fond vert (réponse juste) =3 ==> choix texte noir sur fond rouge (réponse fausse), fenetre est l'écran du jeu pour l'affichage. Fonction affiche le choix 4 du qcm . Cette fonction ne revoie rien (fonction d'affichage)."""
      if afftype == 1 :
          color = colorrouge
          colorf = colornoir
      else:
          if afftype == 2 :
              color = colornoir
              colorf = colorvert
          else:
              color = colornoir
              colorf = colorrouge

      pygame.draw.rect(fenetre,colorf,pygame.Rect(ligneV,ligneB,ligneV-decal_larg,ligneB-ligneM))
      pygame.draw.rect(fenetre,colorrouge,pygame.Rect(ligneV,ligneB,ligneV-decal_larg,ligneB-ligneM),4)

      chainereponseaff = []
      chainereponseaff = Jeu2.decoupechaine(rep4,carrep)
      poslignereponse =  0
      for lignereponse in chainereponseaff:
        imagetxt = police.render(lignereponse,1,color)
        fenetre.blit(imagetxt,(xrep4,yrep4 + poslignereponse*20))
        poslignereponse +=1
      
       

    def selectreponse(x,y):
      """x ext un entier: position x du clic de la souris, y est un entier: position y du clic de la souris. Fonction indique la réponse sélectionnée en fonctionduclicde la souris. Cette fonction revoie la case réponse cliquée."""
      selectedreponse=0
      if y >= ligneM:
          # on séléctionner une réponse
          if x>=decal_larg and x< ligneV:
              if y<ligneB:
                  #on a sélectionner la réponse 1
                  selectedreponse = 1
              else :
                  if y<decal_haut+haut_quizz:
                      #on a sélectionner la réponse 3
                      selectedreponse = 3

          else :
              if x<= decal_larg+larg_quizz:
                  if y<ligneB:
                      #on a sélectionner la réponse 2
                      selectedreponse = 2
                  else :
                      if y<decal_haut+haut_quizz:
                          #on a sélectionner la réponse 4
                          selectedreponse = 4


      return selectedreponse

    def verifreponse (repselect,repjuste,fenetre):
      """repselect est un entier: la réponse sélectionnée, repjuste est un entier: la réponse juste fenetre est l'écran du jeu pour l'affichage. Fonction verifie si la réponse est correcte et affiche le résultat en conséquence.  Cette fonction ne revoie rien (fonction d'affichage)."""
      global score

      if repselect == repjuste:
          reptype = 2
          score = score +1
      else:
          reptype = 3
          score = 0

      if repselect == 1 :
          Jeu2.reponse1(rep1,reptype,fenetre)

      if repselect == 2 :
          Jeu2.reponse2(rep2,reptype,fenetre)

      if repselect == 3 :
          Jeu2.reponse3(rep3,reptype,fenetre)

      if repselect == 4 :
          Jeu2.reponse4(rep4,reptype,fenetre)
      Jeu2.affichescore1(fenetre)
      pygame.display.flip()

    def decoupechaine (chaine, nbcarac):
      """chaine est une chaine: la chaine à découper, nbcarac est un entier:nombre de craractères par ligne. Fonction qui découpe la chaine de caractère passée en paramètres en liste de chaine de mois de nbcaract se terminant par un point, une virgule ou un epace, pour découper un chaine de manière plus lisible. Cette fonction revoie un liste de chaines."""
      chainedecoup=[]
      while len (chaine) > 0 :
          # parcour de la chaine de nb carac à 0 pour la decoupe aux espaces virgules et points   
          if len(chaine)<nbcarac :
              chainedecoup.append (chaine)
              chaine = ""
          else :
              for i in range (nbcarac,0,-1):
  
                  if chaine [i] in (" ",",","."):
  
                      chainedecoup.append (chaine[0:i+1])
                      chaine = chaine [i+1:]
                      break    
      return chainedecoup


    def init():
      """Aucun paramètres en entrée. Fonction d'initialisation et de lancement du jeu de quizz. Cette fonction ne revoie rien."""
      global player

      fenetre = pygame.display.get_surface()
      intmaison= pygame.image.load("assets/intmaison1.png").convert_alpha()
      intmaison=pygame.transform.scale(intmaison,(1024,650))
      fenetre.blit(intmaison, (0,0))
      pygame.display.flip()


      file= "assets/quizz1.mp3"
      pygame.mixer.init()
      pygame.mixer.music.load(file)
      pygame.mixer.music.play() 
      runningson = True
      while runningson:
          runningson = pygame.mixer.music.get_busy()


      pygame.draw.rect(fenetre,colornoir,pygame.Rect(decal_larg,decal_haut,larg_quizz,haut_quizz))

      #textequestion("1+1 = ?")
      Jeu2.textetitre("QUIZZ",colorjaune, fenetre)

      pygame.display.flip()

      qcm = []

      with open('assets/qcm1.csv', newline='') as csvfile:
          spamreader = csv.reader(csvfile, delimiter=';')
          for row in spamreader:
              qcm.append(row)






      x = random.randrange(1, len(qcm))

      continuer = True

      Jeu2.affichescore1(fenetre)
      pygame.display.flip()

      Jeu2.posequestion(x, fenetre,qcm)

      affchrono = 0
      while continuer:
        affchrono +=1
        for event in pygame.event.get():

          if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] == True:
                clickx = event.pos[0]
                clicky = event.pos[1]
                reponseselect = Jeu2.selectreponse(clickx,clicky)
                if reponseselect != 0:
                    Jeu2.verifreponse (reponseselect,reponsecorrecte,fenetre)
                    time.sleep(5)
                    if score>=scoremax:
                        continuer=False
                    else :
                        x = random.randrange(1, len(qcm))
                        Jeu2.posequestion(x,fenetre,qcm)
                        
          if affchrono >= 1000:
                  affchrono = 0
                  pygame.display.set_caption("Escape - Adventure (Quizz)         CHRONO ==> "+ globals.chrono()) # association du nom de la fenetre et affichage du chrono

      runningson = True
      pygame.mixer.music.play()
      while runningson:
          runningson = pygame.mixer.music.get_busy()

      global player


      globals.player.position[1] += -150
      globals.player.place = 'MAZE' 
      globals.background_music()

