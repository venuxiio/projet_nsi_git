import pygame # importation des bonnes bibliothèques
import globals

class Cle(pygame.sprite.Sprite):
    def __init__(self,tiledX,tiledY, jeu):
      super().__init__()
      self.tiledX = tiledX
      self.tiledY = tiledY
      self.jeu = jeu
      self.sprite_sheet = pygame.image.load('assets/keys.png') # récupération de l'image
      self.image = self.get_image(0, 0)
      self.image.set_colorkey([0, 0, 0])
      # position
      self.rect = self.image.get_rect()
      self.position = [tiledX*32, tiledY*32]
   
    def update(self):  # mettre a jour le sprite de la cle
        self.rect.topleft = self.position
    
    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image

    def check_colission(self):
      position = globals.player.position;
      tiledX = int(round(position[0] / 32, 0))
      tiledY = int(round(position[1] / 32, 0))
      if tiledX ==self.tiledX and tiledY==self.tiledY:
        globals.player.keys.append(self)
        print ('winKey', self.jeu)
        self.play_keysound()
        return True
      return False
    
    def play_keysound(self):
      file= "assets/keysound.mp3"
      pygame.mixer.init()
      pygame.mixer.music.load(file)
      pygame.mixer.music.play()
      runningson = True
      while runningson:
        runningson = pygame.mixer.music.get_busy()
    
