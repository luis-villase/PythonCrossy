import pygame
from gameObject import GameObject


class Enemy(GameObject):
    def __init__(self, x, y, width, height, image_path, speed):
        super().__init__(x, y, width, height, image_path)
        self.speed = speed

    def move(self, max_width):
        if self.x <= 0 or self.x >= max_width - self.width:
            self.speed = (-1) * self.speed
        self.x += self.speed
