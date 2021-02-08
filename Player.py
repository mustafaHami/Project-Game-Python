import pygame, sys
from pygame.locals import *

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.jump = 5
        self.image = pygame.image.load('images/tree_player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 550

    def move_right(self):
        self.rect.x += self.velocity

    def jump(self):    
        x,y=10,300
        movex,movey=0,0
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                movex = -0.2
            elif event.key==K_RIGHT:
                movex=+0.2
            elif event.key==K_DOWN:
                movey=+0.2
            elif event.key==K_SPACE:
                movey=-0.4
                movey=+0.4
        if event.type==KEYUP:
                if event.key==K_LEFT:
                    movex = 0
                elif event.key==K_RIGHT:
                    movex=0
                elif event.key==K_DOWN:
                    movey=0
                elif event.key==K_SPACE:
                    movey=0
        x+=movex
        y+=movey
        screen.blit(player,(x,y)) 