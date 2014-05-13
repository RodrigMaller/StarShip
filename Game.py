import sys, os
import pygame
from Spaceship import Spaceship
from pygame.locals import *

class Game:
    def __init__(self):
        pygame.init()
        self._running = True
        self._size = self._weight, self._height = 800, 600
        self._clock = pygame.time.Clock()
        self._clock.tick(60)
        self._allSprites = pygame.sprite.Group()
    
    def execute(self):
        self.createScreen()
        self.createPlayer()
        
        while(self._running):
            for event in pygame.event.get():
                if not hasattr(event, 'key'): continue
                self.processEvent(event)
        
            self.render()
            pygame.display.flip()
    
    def render(self):
        self._allSprites.clear(self._screen, self._bg)
        self._allSprites.update()
        self._allSprites.draw(self._screen)
    
    def processEvent(self, event):
        down = (event.type == KEYDOWN)
        if event.key == K_LEFT: self._player.k_left = down * -self._player.speed
        if event.key == K_RIGHT: self._player.k_right = down * self._player.speed
        if event.type == KEYDOWN and event.key == K_SPACE:
            nShot = self._player.shoot(self.load_image("shot.png"))
            self._allSprites.add(nShot)
        if event.key == K_ESCAPE: sys.exit()
    
    def createScreen(self):
        self._screen = pygame.display.set_mode(self._size)
        self._bg, self._bgRect = self.load_image("bg.png")
        self._screen.blit(self._bg, (0, 0))
    
    def createPlayer(self):
        x, y = self._bgRect.center
        initPos = (x, self._height-50)
        self._player = Spaceship(initPos, self.load_image("Spaceship.png"))
        self._allSprites.add(self._player)
    
    def load_image(self, name, colorkey=None):
        try:
            image = pygame.image.load(name)
        except pygame.error, message:
            print 'Cannot load image:', name
            raise SystemExit, message
        image.convert()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image, image.get_rect()
    
if __name__ == "__main__" :
    Game = Game()
    Game.execute()
