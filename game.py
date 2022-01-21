import pygame
import pyscroll
import pytmx
from player import Player
from pytmx.util_pygame import load_pygame
pygame.init()


class Game():
    def __init__(self):  # fonction qui se charge du chargement du jeu
        # window creation
        self.screen = pygame.display.set_mode((1024, 768))
        pygame.display.set_caption("Escape - Adventure")

        # load the map
        tmx_data = load_pygame("assets/map.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(
            map_data, self.screen.get_size())
        map_layer.zoom = 3

        # player generation
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)

        # draw the layers group
        self.group = pyscroll.PyscrollGroup(
            map_layer=map_layer, default_layer=3)
        self.group.add(self.player)

    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation("up")
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation("down")
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation("left")
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation("right")

    def run(self):

        # loop of the game
        running = True

        while running:
            self.handle_input()
            self.group.update()
            self.group.center(self.player.rect.center)
            # pour dessiner directement les calques sur l'ecran
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


pygame.quit()
