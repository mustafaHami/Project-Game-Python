import pygame, sys
from pygame.locals import *
from Game import Game
import time
import random

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
SPEED = 5

# Setting up fonts that will be used
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
font_fin = pygame.font.SysFont("Verdana", 35)
game_over = font.render("Game Over", True, BLACK)

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((1024, 768))
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

class Background2():
    def __init__(self):
        self.bgimage = pygame.image.load('images/night_forest.png')
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
back_ground2 = Background2()
'''def rungame():
    if len(name_entry.get()) != 0:
        window.destroy()
        game.is_playing = True'''

'''def tutorial():
    tuto_window = Tk()
    window.geometry("1024x768")
    window.config(background ="#97CE68")import matplotlib


    label_title = Label(frame,text="Your mission is to escape this forest",font=("Courrier",40), bg = "#97CE68",fg="black")


#/////////////////////////////MENU WINDOW//////////////////////////////////////////////////////////
window = Tk()

#Menu 
window.title("Forescape")
window.geometry("1024x768")
window.config(background ="#97CE68")

#creating Frame 
frame = Frame(window,bg='#97CE68')

#creating image 
width = 500
height = 100 
image = PhotoImage(file="images/logo_size.png")
canvas = Canvas(window, width=width, height=height)
canvas.create_image(width/2,height/2,image=image)
canvas.pack()
#add text
label_title = Label(frame,text="Enter your name",font=("Courrier",40), bg = "#97CE68",fg="black")
label_title.grid(row=1,column=0,sticky=W)
name_entry = Entry(frame,font=("Courrier",40), bg = "#97CE68",fg="black")
name_entry.grid(row=1,column=1,sticky=W)
global name 
name = name_entry.get()
frame.pack(expand=YES)
#addign a button 
play_button = Button(window,text="Tutorial",font=("Courrier",40), bg = "white",fg="green",command=tutorial)
play_button.pack(fill=X)
play_button = Button(window,text="Play",font=("Courrier",40), bg = "white",fg="green",command=rungame)
play_button.pack(fill=X)

window.mainloop()
#/////////////////////////////MENU WINDOW//////////////////////////////////////////////////////////
'''


# Creating Sprites Groups
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
saut = 20
jump = False
random = random.randint(0,100)
enVie = "second"
#music = pygame.mixer.music.load("son/Wordl2.mp3")
# Game Loop

while True:

    if enVie == "first":
        # Every game events
        for event in pygame.event.get():
            if event.type == INC_SPEED:
                SPEED += 0.5
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_z and saut == 20:
                    jump = True
        if jump == True and saut >= -20:
            saut -= 1
            P1.jumpy(saut)

        if saut == -19:
            saut = 20
            jump = False

        back_ground.update()
        back_ground.render()

        # Add fruits
        game.all_fruits.draw(DISPLAYSURF)
        # Moves and Re-draws

        for entity in all_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()

        #Health Bar
        game.player.update_health_bar(DISPLAYSURF)

        #Animation
        game.player.update_animation()

        for fruits in game.all_fruits:
            fruits.forward()
            game.update(DISPLAYSURF)
            pygame.display.update()

        # To be run if collision occurs between Player and Enemy
        if pygame.sprite.spritecollideany(P1, enemies):
            time.sleep(0.8)

            DISPLAYSURF.fill(RED)
            DISPLAYSURF.blit(game_over, (30, 250))

            pygame.display.update()
            '''for entity in all_sprites:
                entity.kill()
            time.sleep(1.5) 
            pygame.quit()
            sys.exit()'''
        if P1.health == 0:
            DISPLAYSURF.fill(BLACK)
            DISPLAYSURF.blit(font_fin.render("CLICK DEUX FOIS POUR ALLER DANS L'AUTRE MONDE",True, WHITE), (30,350))
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.time.wait(3000)
                pygame.mixer.music.play(-1)
                enVie = "second"
                P1.health = P1.max_health
        pygame.display.update()

    elif enVie == "second":


        back_ground2.render()
        game.player.update_animation()

        # Every game events
        for event in pygame.event.get():
            if event.type == INC_SPEED:
                 SPEED += 0.5
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_z and saut == 20:
                    jump = True
                elif event.key == pygame.K_SPACE:
                    P1.projectile()
        if jump == True and saut >= -20:
            saut -= 1
            P1.jumpy(saut)

        if saut == -19:
            saut = 20
            jump = False

        # actualisé la barre d'evenement
        game.update_comet(DISPLAYSURF)
        # recupere les projectils
        for projectile in P1.all_projectile:
            projectile.move()
        # appliquer les porjectile
        game.player.all_projectile.draw(DISPLAYSURF)

        # recupere les monstres
        for monster in game.all_monsters:
            monster.forward()
            monster.update_health_bar(DISPLAYSURF)
            monster.update_animation()
            DISPLAYSURF.blit(font.render(str(monster.nbKill()), True, WHITE), (20, 350))
            if monster.nbKill() <= 0:
                pygame.mixer.music.set_volume(0)
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(
                    font_fin.render("CLICK DEUX FOIS POUR ALLER DANS RETOURNER DANS VOTRE MONDE", True, WHITE),
                    (20, 350))
                if event.type == pygame.MOUSEBUTTONUP:
                    pygame.time.wait(3000)
                    enVie = "first"
                    P1.health = P1.max_health
                    game.all_monsters.monster.remisZero()
            else:
                # appliquer les monstre
                game.all_monsters.draw((DISPLAYSURF))
                # Moves and  Re-draws
                for comet in game.comet_event.all_comets:
                    comet.fall()

                for entity in all_sprites:
                    DISPLAYSURF.blit(entity.image, entity.rect)
                    entity.moveforSecondWorld()

                    #Health Bar
                    game.player.update_health_bar(DISPLAYSURF)




        pygame.display.update()




