import math
import pygame
import globals
import time

#Class pour gérer la classe balle
class Balle(pygame.sprite.Sprite):
    #constructeur de la Class
    def __init__(self,x,y,v,paddle):
      super().__init__()
      self.r = 5
      self.sticky = False
      self.paddle = paddle
      self.x =x
      self.v = v
      self.new_ball()
      self.image = pygame.Surface([self.r*2,self.r*2]).convert_alpha()
      # self.image.fill(globals.colorbleu)
      pygame.draw.circle(self.image, globals.colorjaune, (self.r, self.r), self.r)
      self.rect = self.image.get_rect()

    def update(self):
      if not self.launch:
        self.x = self.paddle.x  
    
      self.rect.center = (globals.decal_larg + self.x, globals.decal_haut+ self.y)
      
    #méthode qui permet de déplacer la balle a la vitesse "dx" "dy" et revient True si la balle est perdu et sors par le bas et gère les bounces
    def move(self): 

        if self.x + self.dx > globals.larg_game - self.r:
           self.dx = -self.dx

        if self.x + self.dx < self.r:
           self.dx = -self.dx
        
        if self.y + self.dy > globals.haut_game - self.r:
            return True

        if self.y + self.dy < self.r:
           self.dy = -self.dy
          

        if (self.launch):
            self.x +=self.dx
            self.y +=self.dy
        
        return False

    #remettre une balle au debut 
    def new_ball(self):
        self.sticky = False
        self.launch = False
        self.dx = self.v
        self.dy = -self.v
        self.y = globals.haut_game - 34
        
#Class qui permet de gérer la planche en bas de l'écran
class Paddle(pygame.sprite.Sprite):
    #constructeur de la Class Paddle
    def __init__(self,x):
      super().__init__()
      self.larg = 50
      self.haut = 4
      self.x =x
      self.y = globals.haut_game-30
      self.image = pygame.Surface([self.larg,self.haut])
      self.image.fill(globals.colorrouge)
      self.rect = self.image.get_rect()

    #sprite méthode toujours appelé a chaque loop, 
    #elle prend la position x de la souris et l'applique au sprite dans la limite des bords
    def update(self):
      x = pygame.mouse.get_pos()[0] -globals.decal_larg
      if x<self.larg/2:
          self.x= self.larg/2
      elif x> globals.larg_game-self.larg/2:
          self.x = globals.larg_game-self.larg/2
      else:
          self.x = x

      self.rect.center = (globals.decal_larg + self.x, globals.decal_haut+ self.y)

    #méthode qui permet de savoir si la balle rebondie sur la planche
    def touch(self, ball):
        if ball.y<self.y:
            return False
        
        if ball.y>self.y+4:
            return False
        
        if abs(ball.x-self.x)<self.larg/2:
            return True
        else:
            return False
    #méthode permet de faire rebondir la balle sur la planche, si la balle n'est pas en contact avec la planche alors il y aura une nouvelle balle
    def rebounce(self,ball:Balle):
        #print (ball.sticky)
        if not ball.sticky:
            ball.dy = -ball.dy
        else:
            ball.new_ball()
          
#Class qui gère les bricks
class Brick(pygame.sprite.Sprite):
    def __init__(self,x,y):
      super().__init__()
      self.x =x
      self.y = y
      self.r = 15
      self.image = pygame.Surface([self.r*2,self.r*2]).convert_alpha()
      # self.image.fill(globals.colorbleu)
      pygame.draw.circle(self.image, globals.colorvert, (self.r, self.r), self.r)
      self.rect = self.image.get_rect()
      self.rect.center = (globals.decal_larg + self.x, globals.decal_haut+ self.y)

    #méthode qui permet grâce a la loi de Pythagore de calculer la distances entre la balle et la brique
    def get_distance(self, ball):
        d = math.sqrt(math.pow(ball.x + ball.dx - self.x, 2) + math.pow(ball.y + ball.dy - self.y, 2));
        return d

    #méthode permet de faire rebondir la balle sur la brique si la distance entre les deux objets sont plus petit que le rayon de la brique
    def rebounce(self,ball,distance):
        nx = -(ball.x + ball.dx - self.x) / distance
        ny = -(ball.y + ball.dy - self.y) / distance
        dot = ball.dx * nx + ball.dy * ny
        ball.dx = ball.dx - 2 * dot * nx
        ball.dy = ball.dy - 2 * dot * ny
      
#Class qui gère le jeu 3
class Jeu3():
    #statut du jeu qui peut être running, gameover, abandonner et win
    status = 'running'

    ballRadius = 10
    paddleWidth = 250
  
    #vitesse de la balle
    speed = 2
    
    #nombre de vie
    lives = 3

    bricks=[]
        
    #affiche les vies en cours  
    def display_lives(self,fenetre):
        policetitre = pygame.font.SysFont('impact', 20,False)
        imagetxt = policetitre.render('lives:' + str(self.lives),True,globals.colorrouge)
        fenetre.blit(imagetxt,(0,0))
      
    #affiche le message "game over" et retourne au MAZE après 3 secondes
    def display_game_over(self,fenetre):
        policetitre = pygame.font.SysFont('impact', 40,False)
        imagetxt = policetitre.render('Game OVER',True,globals.colorrouge)
        fenetre.blit(imagetxt,(20,100))
        pygame.display.flip()
        time.sleep(3)
        globals.pass_game() 

    #affiche le message "Win!!" et place le joueur devant la maison
    def display_win(self,fenetre):
        policetitre = pygame.font.SysFont('impact', 40,False)
        imagetxt = policetitre.render('Win !!',True,globals.colorvert)
        fenetre.blit(imagetxt,(20,100))
        pygame.display.flip()
        time.sleep(3)
        globals.abandon_game() 
      
    #constructeur de la Class Jeu3
    def __init__(self):
        pygame.display.set_caption("Escape - Adventure (BALL GAME)         CHRONO ==> "+ globals.chrono()) # association du nom de la fenetre et affichage du chrono
        self.fenetre = pygame.display.get_surface()
        globals.background_house(self.fenetre)
        globals.texte_titre("BALL GAME",globals.colorjaune, self.fenetre)

        #mettre la music en place lors du commencement du jeu
        file= "assets/Memory1.mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

        #permet de contenir et de gérer plusieurs objets Sprite.
        self.sprites = pygame.sprite.Group()

        #mettre les briques allignés et espacés
        for c in range(0,9): 
            for d in range(0,3):
               brick = Brick(c * 50 + 50 ,50 + d * 50)
               self.bricks.append(brick)
               self.sprites.add(brick)

        self.paddle = Paddle(globals.larg_game / 2)
        self.sprites.add(self.paddle)
        self.ball = Balle(globals.larg_game / 2, globals.haut_game - self.paddleWidth / 2, self.speed,self.paddle)
        self.sprites.add(self.ball)
        affchrono = 0
        #pendant que le statut "running" est en place 
        while self.status=='running':
            affchrono += 1
            for event in pygame.event.get():
                self.handle_event(event)
            pygame.display.flip()
            globals.background_house(self.fenetre)

            #affichage de la fenetre qui affiche les vies du joueur
            self.display_lives(self.fenetre)
            
            #si le nombre de briques est égal a 0, le statut est mis a "win" et le joueur passe derrière la porte
            if len(self.bricks)==0:
                self.status = 'win'
            #dans une boucle qui prend en compte chaque brique dans les briques, la variable distance "d" va prendre la distance entre la brique et la balle
            for brick in self.bricks:
                d = brick.get_distance(self.ball)

                #si la distance est inferieur au rayon de la brique alors la balle rebondie et la brique disparait du jeu
                if (d<brick.r):
                    brick.rebounce(self.ball,d)
                    self.bricks.remove(brick)
                    self.sprites.remove(brick)
            #si la balle touche la planche la balle rebondie 
            if self.paddle.touch(self.ball):
                self.paddle.rebounce(self.ball)

            lose = self.ball.move()
            #si tu perds, alors le nombre de vies diminue et si ton nombre de vies et égal à 0 alors le joueur est replacé en face de la maison et doit alors recommencer le jeu
            if lose:
                self.lives-=1
                if self.lives>0:
                    self.ball.new_ball()
                else:
                    self.status = 'game_over'

            #permet d'updater toutes les sprites
            self.sprites.draw(self.fenetre)
            self.sprites.update()

            if affchrono >= 10:
              affchrono = 0
              pygame.display.set_caption("Escape - Adventure (BALL GAME)         CHRONO ==> "+ globals.chrono()) # association du nom de la fenetre et affichage du chrono

        #si le statut est a "abandon" alors le joueur est replacé dans le maze devant la maison, sinon si la statut est "gameover" alors le message game over apparait et sinon si le statut est win alors le joueur a gagné et le joueur peut passer de l'autre coté 
        if self.status=='abandon':
            globals.abandon_game()
        elif self.status=='game_over':
            self.display_game_over(self.fenetre)
        else:
            self.display_win(self.fenetre)
            globals.pass_game()

    
    def handle_event(self,event):
        #juste un hack pour passer directement de l'autre coté de la maison
        if globals.hack_win(event):
            self.status = 'win'

        #si on quitte alors le joueur est replacé dans le labyrinthe devant la maison
        if event.type== pygame.QUIT:
            self.status = 'abandon'
          
        #le joueur peut prendre la balle et la laisser sur la planche en bas en appuyant sur la roulette de la souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (self.ball.launch):
                 self.ball.sticky = True
            else:
                self.ball.launch = True
           

 