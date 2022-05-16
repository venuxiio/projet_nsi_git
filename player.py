import pygame # importation des bonnes bibliothèques

class Joueur(pygame.sprite.Sprite):
    #constructeur de la Class Joueur
    def __init__(self):
      super().__init__()
    def init(self, x, y):
      self.keys=[] 
      self.jeux = 0 
      # variable  qui indique si l'on se trouve dans le maze qui permet de ne plus afficher le labyrinthe et les déplacements du personnage
      self.place = 'MAZE' 
      # récupération de l'image
      self.sprite_sheet = pygame.image.load('assets/player.png') 
      self.image = self.get_image(0, 0)
      self.image.set_colorkey([0, 0, 0])
      # position
      self.rect = self.image.get_rect()
      self.position = [x, y]
      # association de l'image du personnage à haut bas droite gauche
      self.images = {
        # association de la bonne image en fonction de la direction
        "down": self.get_image(0,0),  
        "left": self.get_image(0,32),
        "right":self.get_image(0,64),
        "up":self.get_image(0,96)
      }

      # nombre de pixel par déplacement 
      self.speed = 2 

      
    #méthode qui vérifie si le joueur a la clé d'un mini jeu  
    def hasKey(self,jeu):
      for key in self.keys:
        if key.jeu == jeu:
          return True
      return False
      
    #changer l'image du joueur selon sa direction
    def change_animation(self,name): 
      self.image = self.images[name]
      self.image.set_colorkey((0,0,0)) # transparence derière le personnage 

    # déplacement du personnage

    # déplacement a droite 
    def move_right(self): self.position[0] += self.speed 
    # déplacement a gauche
    def move_left(self): self.position[0] -= self.speed 
    # déplacement en haut 
    def move_up(self): self.position[1] -= self.speed 
    # deplacement en bas
    def move_down(self): self.position[1] += self.speed 
    # mettre a jour le sprite du joueur
    def update(self):  
        self.rect.topleft = self.position

    # retrouver la bonne image dans la grosse image
    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image
