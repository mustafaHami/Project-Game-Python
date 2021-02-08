import pygame, sys
from pygame.locals import *
from Game import Game
pygame.init()

FPS = 30
FramePerSec = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

DISPLAYSURF = pygame.display.set_mode((1024,768))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("ForestCape")

background = pygame.image.load('images/day_forest.png')

game = Game()

while True:

    #background applying
    DISPLAYSURF.blit(background, (0,0))
    #player applying
    DISPLAYSURF.blit(game.player.image, game.player.rect)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    FramePerSec.tick(FPS)
