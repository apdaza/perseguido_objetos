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

    def asociar(self, personaje):
        self.asociado = personaje

    def update(self):
        pass

    def draw(self, screen):
        self.rect.x %= screen.get_width()
        self.rect.y %= screen.get_height()
        self.image = self.imagenes[self.sentido][self.cont]
        screen.blit(self.image, self.rect)

class Heroe(Personaje):

    def __init__(self, sprites, pos):
        super().__init__(sprites, pos)
        self.vida = 100
        self.puntos = 0


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

    def draw(self, screen):
        fuente = pygame.font.Font(None, 20)
        super().draw(screen)
        texto_vida = fuente.render("vida = " + str(self.vida), 1, (200, 0, 0))
        screen.blit(texto_vida, [self.rect.x - 20, self.rect.y - 20])
        texto_puntos = fuente.render("puntos = " + str(self.puntos), 1, (200, 0, 0))
        screen.blit(texto_puntos, [self.rect.x - 20, self.rect.y + 35])
            


class Villano(Personaje):
    def update(self):
        if self.asociado.rect.x < self.rect.x:
            self.rect.x -= self.velocidad
            self.sentido = 3
        if self.asociado.rect.x > self.rect.x:
            self.rect.x += self.velocidad
            self.sentido = 2
        if self.asociado.rect.y < self.rect.y:
            self.rect.y -= self.velocidad
            self.sentido = 1
        if self.asociado.rect.y > self.rect.y:
            self.rect.y += self.velocidad
            self.sentido = 0