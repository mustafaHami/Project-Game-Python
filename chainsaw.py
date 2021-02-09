import pygame

class ChainSaw(pygame.sprite.Sprite):

    def __init__(self):
        self.damage = 10
        self.rect = self.image.load('images/chainsaw.png')
        self.rect.x = 1030
        self.rect = 550

    def move(self):
