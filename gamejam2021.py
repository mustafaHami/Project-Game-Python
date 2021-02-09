import pygame, sys
from pygame.locals import *
from Game import Game
import time
# Initializing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SPEED = 5
SCORE = 0

# Setting up fonts that will be used
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

<<<<<<< HEAD
# Create a white DISPLAYSURF


=======
# Create a white screen
>>>>>>> 293d8569f15e4a46cca40bc40b5c6be6b7ed0f6a
DISPLAYSURF = pygame.display.set_mode((1024, 768))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Forescape")



class Background():
    def __init__(self):
        self.bgimage = pygame.image.load('images/background.jpg')
        self.bgimage = pygame.transform.scale(self.bgimage, (1024, 768))
        self.rectBGimg = self.bgimage.get_rect()

        self.bgY1 = 0
        self.bgX1 = 0

        self.bgY2 = 0
        self.bgX2 = self.rectBGimg.width

        self.moving_speed = 5           

    def update(self):
        self.bgX1 -= self.moving_speed
        self.bgX2 -= self.moving_speed
        if self.bgX1 <= -self.rectBGimg.width:
            self.bgX1 = self.rectBGimg.width
        if self.bgX2 <= -self.rectBGimg.width:
            self.bgX2 = self.rectBGimg.width

    def render(self):
        DISPLAYSURF.blit(self.bgimage, (self.bgX1, self.bgY1))
        DISPLAYSURF.blit(self.bgimage, (self.bgX2, self.bgY2))


# Setting up Sprites
game = Game()
P1 = game.player
back_ground = Background()

<<<<<<< HEAD

# HEALTH BAR


=======
>>>>>>> 293d8569f15e4a46cca40bc40b5c6be6b7ed0f6a


# Creating Sprites Groups
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
saut = 20
jump = False

# Game Loop
while True:

<<<<<<< HEAD

    # Cycles through all occurring events

=======
>>>>>>> 293d8569f15e4a46cca40bc40b5c6be6b7ed0f6a
    # Every game events
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP and saut == 20:
                jump = True
                print("t'as appuyer")

    if jump == True and saut >= -20:
        saut -= 1
        P1.jumpy(saut)

    if saut == -19:
        saut = 20
        jump = False


    back_ground.update()
    back_ground.render()

    # DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
<<<<<<< HEAD
    DISPLAYSURF.blit(scores, (10, 10))

    # Moves and Re-draws all Sprites

=======
>>>>>>> 293d8569f15e4a46cca40bc40b5c6be6b7ed0f6a
    DISPLAYSURF.blit(scores, (10, 10))
    # Add fruits
    game.all_fruits.draw(DISPLAYSURF)
    # Moves and Re-draws
<<<<<<< HEAD

=======
>>>>>>> 293d8569f15e4a46cca40bc40b5c6be6b7ed0f6a
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

<<<<<<< HEAD

    game.player.update_health_bar(DISPLAYSURF)

    for fruits in game.all_fruits:
        fruits.forward()

=======
    for fruits in game.all_fruits:
        fruits.forward()
>>>>>>> 293d8569f15e4a46cca40bc40b5c6be6b7ed0f6a

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.8)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(1.5)
        pygame.quit()
        sys.exit()


    pygame.display.update()
    FramePerSec.tick(FPS)
