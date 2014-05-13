import sys, os
import pygame
from Shot import Shot
from pygame.locals import *

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = image
        self.speed = 0.5
        self.pos = pos
        self.k_left = self.k_right = 0
    
    def update(self):
        x, y = self.pos
        self.movement = (self.k_left + self.k_right)
        if (self.movement >= 0 and x < 800-25) or (self.movement < 0 and x > 0+25):
            x += self.movement
            self.pos = (x, y)
        self.rect.center = self.pos
        
    def shoot(self, image):
        x, y = self.pos
        y -= 20
        initPos = (x, y)
        shot = Shot(initPos, image)
        return shot
