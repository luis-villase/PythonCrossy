import pygame
from gameObject import GameObject
from player import Player
from enemy import Enemy


class Game:
    def __init__(self):
        self.width = 800
        self.height = 800
        self.tile_size = 50
        self.white = (255, 255, 255)
        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.bg_image = GameObject(0, 0, self.width, self.height, 'assets/base/background.png')
        self.chest = GameObject(375, 50, self.tile_size, self.tile_size, 'assets/base/treasure.png')
        file = 'assets/full tilemap.png'

        self.level = 1.0
        self.restart()

    def restart(self):
        self.player = Player(375, 725, self.tile_size, self.tile_size, 'assets/base/player.png', 5)
        speed = 2 + (self.level * 5)
        enemy_img = 'assets/base/enemy.png'
        if self.level >= 4:
            self.enemies = [
                Enemy(1, 600, self.tile_size, self.tile_size, enemy_img, speed),
                Enemy(700, 400, self.tile_size, self.tile_size, enemy_img, speed - 2),
                Enemy(250, 200, self.tile_size, self.tile_size, enemy_img, speed + 2)
            ]
        elif self.level >= 2:
            self.enemies = [
                Enemy(1, 600, self.tile_size, self.tile_size, enemy_img, speed),
                Enemy(700, 400, self.tile_size, self.tile_size, enemy_img, speed - 2)
            ]
        else:
            self.enemies = [
                Enemy(1, 600, self.tile_size, self.tile_size, enemy_img, speed),
            ]

    def refresh(self):
        self.window.fill(self.white)
        self.window.blit(self.bg_image.image, (self.bg_image.x, self.bg_image.y))
        self.window.blit(self.chest.image, (self.chest.x, self.chest.y))
        self.window.blit(self.player.image, (self.player.x, self.player.y))
        for enemy in self.enemies:
            self.window.blit(enemy.image, (enemy.x, enemy.y))
        pygame.display.update()

    def move_objects(self, direction_x, direction_y):
        self.player.move(direction_x, direction_y, self.width, self.height)
        for enemy in self.enemies:
            enemy.move(self.width)

    def is_dead(self):
        for enemy in self.enemies:
            if self.collision_detection(self.player, enemy):
                self.level = 1.0
                return True
        return False

    def got_chest(self):
        if self.collision_detection(self.player, self.chest):
            self.level += 0.5
            return True
        return False

    @staticmethod
    def collision_detection(object_1, object_2):
        if object_1.y > (object_2.y + object_2.height):
            return False
        elif object_2.y > (object_1.y + object_1.height):
            return False
        if object_1.x > (object_2.x + object_2.width):
            return False
        elif object_2.x > (object_1.x + object_1.width):
            return False
        return True

    def game_loop(self):
        direction_y = 0
        direction_x = 0
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction_y = -1
                    elif event.key == pygame.K_DOWN:
                        direction_y = 1
                    elif event.key == pygame.K_LEFT:
                        direction_x = -1
                    elif event.key == pygame.K_RIGHT:
                        direction_x = 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction_y = 0
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        direction_x = 0

            self.move_objects(direction_x, direction_y)
            self.refresh()

            if self.is_dead() or self.got_chest():
                self.restart()

            self.clock.tick(60)
