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
    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[K_DOWN]:
            self.sentido = 0
            self.rect.y += self.velocidad
        if teclas[K_UP]:
            self.sentido = 1
            self.rect.y -= self.velocidad
        if teclas[K_RIGHT]:
            self.sentido = 2
            self.rect.x += self.velocidad
        if teclas[K_LEFT]:
            self.sentido = 3
            self.rect.x -= self.velocidad
        if teclas[K_DOWN] or teclas[K_LEFT] or teclas[K_RIGHT] or teclas[K_UP]:
            self.cont += 1
            self.cont %= 3
            self.image = self.imagenes[self.sentido][self.cont]


class Villano(Personaje):
    pass