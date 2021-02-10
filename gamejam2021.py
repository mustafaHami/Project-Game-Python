import pygame, sys
from pygame.locals import *
from Game import Game
import time
import random
from tkinter import * 
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
game_over = font.render("Game Over", True, BLACK)

# Create a white screen
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
tutorial = False
def rungame():
    if len(name_entry.get()) != 0:
        window.destroy()
        game.is_playing = True

def tutorial():
    tuto_window = Toplevel()
    tuto_window.geometry("1024x768")
    tuto_window.config(background ="#97CE68")

    inst = Label(tuto_window,text="Escape the forest !",font=("Courrier",50), bg = "#97CE68",fg="black")
    inst.grid(row=0,column=0,sticky=W) 
    inst2 = Label(tuto_window,text="Avoid the cursed purple fruits they reduce your life bar",font=("Courrier",15), bg = "#97CE68",fg="black")
    inst2.grid(row=1,column=0,sticky=W) 
    inst3 = Label(tuto_window,text="Collect the normal ones to increase your score and your life",font=("Courrier",15), bg = "#97CE68",fg="black")
    inst3.grid(row=2,column=0,sticky=W) 
    inst4 = Label(tuto_window,text="If your life bar is empty you fall asleep",font=("Courrier",15), bg = "#97CE68",fg="black")
    inst4.grid(row=3,column=0,sticky=W) 
    inst5 = Label(tuto_window,text="You need to face the monsters of your nightmare to wake up and continue your escape",font=("Courrier",15), bg = "#97CE68",fg="black")
    inst5.grid(row=4,column=0,sticky=W)
    
    
    inst6 = Label(tuto_window,text="If you fail you die",font=("Courrier",15), bg = "#97CE68",fg="black")
    inst6.grid(row=5,column=0,sticky=W) 

    widthe = 100
    heighte = 100 
    image2 = PhotoImage(file="images/cursed_banana.png")
    canvas2 = Canvas(tuto_window, width=widthe, height=heighte)
    canvas2.create_image(widthe/2,heighte/2,image=image2)
    canvas2.grid(row=1,column=1,sticky=W)
    image3 = PhotoImage(file="images/banana.png")
    canvas3 = Canvas(tuto_window, width=widthe, height=heighte)
    canvas3.create_image(widthe/2,heighte/2,image=image3)
    canvas3.grid(row=2,column=1,sticky=W)
    image4 = PhotoImage(file="images/life_bar.PNG")
    canvas4 = Canvas(tuto_window, width=widthe, height=heighte)
    canvas4.create_image(widthe/2,heighte/2,image=image4)
    canvas4.grid(row=3,column=1,sticky=W)
    
    tuto_window.mainloop()

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

<<<<<<< HEAD
if game.is_playing == True:
    # Game Loop
    while True:

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
=======
# Game Loop
while True:

    game.player.update_animation()
    game.player.start_animation()

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
        game.player.stop_animation()

    if saut == -19:
        saut = 20
        jump = False
    
>>>>>>> 4d9c415f51ae78392a62f8d5f320f8f9ed80f3f5

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

<<<<<<< HEAD
        # To be run if collision occurs between Player and Enemy
        if pygame.sprite.spritecollideany(P1, enemies):
            time.sleep(0.8)
=======
>>>>>>> 4d9c415f51ae78392a62f8d5f320f8f9ed80f3f5

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
