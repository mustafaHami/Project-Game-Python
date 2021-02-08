import pygame, sys
from pygame.locals import *
from Game import Game
pygame.init()

FramePerSec = pygame.time.Clock()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

DISPLAYSURF = pygame.display.set_mode((1024,768))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("ForestCape")

background = pygame.image.load('images/day_forest.png')
background_size = background.get_size()
background_rect = background.get_rect()

w,h = background_size
x = 0
y = 0

x1 = 0
y1 = -h

running = True

game = Game()

while True:

    #background spawing and moving
    while running:
        DISPLAYSURF.blit(background, background_rect)
        pygame.display.update()
        for event in pygame.event.get(): 
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()
        y1 += 5
        y += 5
        DISPLAYSURF.blit(background,(-y,-x))
        DISPLAYSURF.blit(background,(-y1,-x1))
        #player spawning
        DISPLAYSURF.blit(game.player.image, game.player.rect)
        if y > h:
            y = -h
        if y1 > h:
            y1 = -h
        pygame.display.flip()
        pygame.display.update()
        FramePerSec.tick(15)
                
    #pygame.display.update()

    for event in pygame.event.get(): 
        if event.type == QUIT:
            running = false
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
                #which button is used ? 
            if event.key == pygame.K_SPACE:
                break

                
