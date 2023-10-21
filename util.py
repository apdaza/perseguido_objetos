import pygame

class Util:

    def cargar_imagen(self, nombre, optimizar = False):
        imagen = pygame.image.load(nombre)

        if optimizar:
            imagen = imagen.convert()
        else:
            imagen = imagen.convert_alpha()
        return imagen  

    def cargar_imagenes_heroe(self):
        return [
            [self.cargar_imagen('imagenes/F1.png'),self.cargar_imagen('imagenes/F2.png'),self.cargar_imagen('imagenes/F3.png')],
            [self.cargar_imagen('imagenes/B1.png'),self.cargar_imagen('imagenes/B2.png'),self.cargar_imagen('imagenes/B3.png')],
            [self.cargar_imagen('imagenes/D1.png'),self.cargar_imagen('imagenes/D2.png'),self.cargar_imagen('imagenes/D3.png')],
            [self.cargar_imagen('imagenes/I1.png'),self.cargar_imagen('imagenes/I2.png'),self.cargar_imagen('imagenes/I3.png')]
        ]  

    def cargar_imagenes_villano(self):
        return [
            [self.cargar_imagen('imagenes/SF1.png'),self.cargar_imagen('imagenes/SF2.png'),self.cargar_imagen('imagenes/SF3.png')],
            [self.cargar_imagen('imagenes/SB1.png'),self.cargar_imagen('imagenes/SB2.png'),self.cargar_imagen('imagenes/SB3.png')],
            [self.cargar_imagen('imagenes/SD1.png'),self.cargar_imagen('imagenes/SD2.png'),self.cargar_imagen('imagenes/SD3.png')],
            [self.cargar_imagen('imagenes/SI1.png'),self.cargar_imagen('imagenes/SI2.png'),self.cargar_imagen('imagenes/SI3.png')]
        ]      