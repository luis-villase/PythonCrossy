import pygame
from gameObject import GameObject


class Player(GameObject):
    def __init__(self, x, y, width, height, image_path, speed):
        super().__init__(x, y, width, height, image_path)
        self.speed = speed

    def move(self, direction_x, direction_y, max_width, max_height):
        if (self.y <= max_height - self.height and direction_y == 1) or (self.y >= 0 and direction_y == -1):
            self.y += (direction_y * self.speed)
        if (self.x <= max_width - self.width and direction_x == 1) or (self.x >= 0 and direction_x == -1):
            self.x += (direction_x * self.speed)
