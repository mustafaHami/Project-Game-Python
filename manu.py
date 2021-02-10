import pygame, sys
from pygame.locals import *
from Game import Game
from Game import Background
import time
from tkinter import * 

# Initializing
pygame.init()
#///////////////////////////////////////DISPLAY PARAMETERS////////////////////////////////////////////////////////
# Creating colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Setting up fonts that will be used
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, (0,0,0))

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((1024, 768))
#DISPLAYSURF.fill(WHITE)

#import banner 
banner = pygame.image.load('images/night_forest.png')
banner = pygame.transform.scale(banner, (1024, 768))

#import logo forescape
logo = pygame.image.load('images/logo_size.png')
logo = pygame.transform.scale(logo, (500, 100))

#import button 
play_button = pygame.image.load('images/power.png')
play_button = pygame.transform.scale(play_button,(70,70))
play_button_rect = play_button.get_rect()
play_button_rect.x = 700
play_button_rect.y = 250


DISPLAYSURF.blit(banner,(0,0))
DISPLAYSURF.blit(logo,(100,100))

pygame.display.set_caption("Forescape")
#///////////////////////////////////////DISPLAY PARAMETERS////////////////////////////////////////////////////////
game = Game()
P1 = game.player

def rungame():
    if len(name_entry.get()) != 0:
        window.destroy()
        game.is_playing = True

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

frame.pack(expand=YES)
#addign a button 
play_button = Button(window,text="Play",font=("Courrier",40), bg = "white",fg="green",command=rungame)
play_button.pack(fill=X)

window.mainloop()
#/////////////////////////////MENU WINDOW//////////////////////////////////////////////////////////

# Setting up Sprites
back_ground = Background() 

saut = 20
jump = False
# Game Loop

# Creating Sprites Groups
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)

# Other Variables for use in the program
SPEED = 5
SCORE = 0

#/////////////////////////////////////THE GAME IS RUNNING///////////////////////////////////////////////////////
# Every game events
while True:

    if game.is_playing == True:
        for event in pygame.event.get():
            if event.type == INC_SPEED:
                SPEED += 0.5
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP and saut == 20:
                    jump = True

        if jump == True and saut >= -20:
            saut -= 1
            P1.jumpy(saut)

        if saut == -19:
            saut = 20
            jump = False

        back_ground.update()
        back_ground.render()

        # screen.blit(background, (0,0))
        scores = font_small.render(str(SCORE), True, BLACK)
        DISPLAYSURF.blit(scores, (10, 10))
        # Add fruits
        game.all_fruits.draw(DISPLAYSURF)
        # Moves and Re-draws
        for entity in all_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()

        for fruits in game.all_fruits:
            fruits.forward()

        # To be run if collision occurs between Player and Enemy
        if pygame.sprite.spritecollideany(P1, enemies):
            pygame.mixer.Sound('crash.wav').play()
            time.sleep(0.8)

            screen.fill(RED)
            screen.blit(game_over, (30, 250))

            pygame.display.update()
            for entity in all_sprites:
                entity.kill()
            time.sleep(1.5)
            pygame.quit()
            sys.exit()


            pygame.display.update()
            pygame.time.Clock().tick(60)
        #if the game didn't start


    pygame.display.update()
    
#/////////////////////////////////////THE GAME IS RUNNING///////////////////////////////////////////////////////
