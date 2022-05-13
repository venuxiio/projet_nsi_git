import pygame  # importation des bonnes bibliothèques
import pyscroll
import pytmx
from pygame.locals import *
from game import Game

if __name__ == "__main__":  #utilisé pour exécuter du code uniquement si le fichier a été exécuté directement et non importé.
    pygame.init()
    game = Game()
    game.run()
