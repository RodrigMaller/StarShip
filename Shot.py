import sys, os
import pygame
from pygame.locals import *

class Shot(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = image
        self.speed = 1
        self.pos = pos
        
    def update(self):
        x, y = self.pos
        if y > 0:
            y += -self.speed
            self.pos = (x, y)
        else:
            self.kill()
        self.rect.center = self.pos
