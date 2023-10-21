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
        self.villanos = []
        for i in range(10):
            self.villanos.append(Villano(util.cargar_imagenes_villano(),(0, 0)))
        for v in self.villanos:    
            v.asociar(self.heroe)

    def jugar(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
            self.screen.blit(self.background, (0, 0))
            if self.heroe.vida > 0:
                self.heroe.draw(self.screen)
                self.heroe.update()
                for v in self.villanos:
                    v.draw(self.screen)
                    v.update()
                    if v.rect.colliderect(v.asociado.rect):
                        v.asociado.vida -= 1
                        v.asociado.puntos -= 1
            else:
                fuente = pygame.font.Font(None, 100)
                texto = fuente.render("Game Over", 1, (200, 0, 0))
                self.screen.blit(texto, (self.SCREEN_WIDTH/2 - texto.get_width()/2,
                                         self.SCREEN_HEIGHT/2 - texto.get_height()/2))
                
            display.update()
            time.delay(50)
                    


    

