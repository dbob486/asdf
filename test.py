# Sprite classes for platform game
import pygame as pg
from settings import *
vec = pg.math.Vector2

class Cube(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
                
    def update(self):
       clone()
       spawn()
       asdf()

    def cube(self, COLOR):
        self.image = pg.Surface((CUBE_WIDTH, CUBE_HEIGHT))
        self.image.fill(COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)

    def difficulty(self):
        pass

    def clone(self):
        pass

    def spawn(self):
        pass

    def asdf(self):
        pass
