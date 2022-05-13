import pygame # importation des bonnes bibliothèques


class Joueur(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('assets/player.png') # récupération de l'image
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

        
        self.speed = 1 # nombre de pixel par déplacement 
        pygame.time.Clock().tick(150)
        
    def change_animation(self,name): 
      
      self.image = self.image = self.images[name]

      self.image.set_colorkey((0,0,0)) # transpârance derière le personnage 

    # déplacement du personnage
    def move_right(self): self.position[0] += self.speed # déplacement a droite 

    def move_left(self): self.position[0] -= self.speed # déplacement a gauche

    def move_up(self): self.position[1] -= self.speed # déplacement en haut 

    def move_down(self): self.position[1] += self.speed # deplacement en bas


    def update(self):  # mettre a jour le sprite du joueur
        self.rect.topleft = self.position

    # taille du personnage
    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image
