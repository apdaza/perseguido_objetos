from personaje import *
from util import Util
from sys import exit


class Juego:
    def __init__(self):
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.ICON_SIZE = 32

        init()
        util = Util()

        self.screen = display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        display.set_caption("El perseguido")
        self.background = util.cargar_imagen("imagenes/fondo.jpg")
        self.heroe = Heroe(util.cargar_imagenes_heroe(), (self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT/2))

    def jugar(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
            self.screen.blit(self.background, (0, 0))
            self.heroe.draw(self.screen)
            self.heroe.update()
            display.update()
            time.delay(50)
                    


    

