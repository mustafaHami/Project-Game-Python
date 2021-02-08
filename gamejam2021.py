import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30
FramePerSec = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

DISPLAYSURF = pygame.display.set_mode((1024,768))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

pygame.draw.line(DISPLAYSURF, BLACK, (150,130), (130,170))
pygame.draw.line(DISPLAYSURF, BLACK, (150,130), (170,170))

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    FramePerSec.tick(FPS)
