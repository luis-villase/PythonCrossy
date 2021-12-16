import pygame
from game import Game

pygame.init()

game = Game()
game.game_loop()

pygame.quit()
quit()

# TODO: Do the tileset in order to randomly load a scene
