import pygame
from pygame import *
from pygame.sprite import Sprite

class Personaje(Sprite):

    def __init__(self, sprites, pos):
        Sprite.__init__(self)
        self.imagenes = sprites
        self.sentido = 0
        self.cont = 0
        self.velocidad = 10
        self.image = self.imagenes[self.sentido][self.cont]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]       

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Heroe(Personaje):
    pass

class Villano(Personaje):
    pass