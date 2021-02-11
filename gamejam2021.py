import pygame, sys
import os 
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

def rungame():
    if len(name_entry.get()) != 0:
        P1.name = name_entry.get()
        window.destroy()
        game.start()

def tutorial():
    tuto_window = Toplevel()
    tuto_window.title("Tutorial")
    tuto_window.geometry("1024x768")
    tuto_window.config(background ="#008000")

    inst = Label(tuto_window,text="Escape the forest !",font=("Courrier",50), bg = "#008000",fg="black")
    inst.grid(row=0,column=0,sticky=W) 
    inst2 = Label(tuto_window,text="Avoid the cursed purple fruits, they reduce your sleep bar !",font=("Courrier",15), bg = "#008000",fg="black")
    inst2.grid(row=1,column=0,sticky=W) 
    inst3 = Label(tuto_window,text="Collect the normal fruits to increase your score and your life !",font=("Courrier",15), bg = "#008000",fg="black")
    inst3.grid(row=2,column=0,sticky=W) 
    inst4 = Label(tuto_window,text="If your sleep bar is empty, you will fall asleep",font=("Courrier",15), bg = "#008000",fg="black")
    inst4.grid(row=3,column=0,sticky=W) 
    inst5 = Label(tuto_window,text="You need to face the monsters of your nightmare to wake up and continue your escape",font=("Courrier",15), bg = "#008000",fg="black")
    inst5.grid(row=4,column=0,sticky=W)
    inst6 = Label(tuto_window,text="If you fail you die",font=("Courrier",15), bg = "#008000",fg="black")
    inst6.grid(row=5,column=0,sticky=W) 
    inst7 = Label(tuto_window,text="You can move left or right with directionnal buttons",font=("Courrier",15), bg = "#008000",fg="black")
    inst7.grid(row=6,column=0,sticky=W)
    inst8 = Label(tuto_window,text="Jump with the space bar or up button",font=("Courrier",15), bg = "#008000",fg="black")
    inst8.grid(row=7,column=0,sticky=W)


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

    image5 = PhotoImage(file="images/left_button.png")
    canvas5 = Canvas(tuto_window, width=widthe, height=heighte)
    canvas5.create_image(widthe/2,heighte/2,image=image5)
    canvas5.grid(row=6,column=1,sticky=W)

    image6 = PhotoImage(file="images/right_button.png")
    canvas6 = Canvas(tuto_window, width=widthe, height=heighte)
    canvas6.create_image(widthe/2,heighte/2,image=image6)
    canvas6.grid(row=6,column=2,sticky=W)

    image7 = PhotoImage(file="images/up_button.png")
    canvas7 = Canvas(tuto_window, width=widthe, height=heighte)
    canvas7.create_image(widthe/2,heighte/2,image=image7)
    canvas7.grid(row=7,column=1,sticky=W)

    image8 = PhotoImage(file="images/imageonline-co-resizedimage.png")
    canvas8 = Canvas(tuto_window, width=widthe, height=heighte)
    canvas8.create_image(widthe/2,heighte/2,image=image8)
    canvas8.grid(row=7,column=2,sticky=W)
    
    tuto_window.mainloop()

def credits():
    credit_window = Toplevel()
    credit_window.title("Credits")
    credit_window.geometry("1024x768")
    credit_window.config(background ="black")


    
    insta = Label(credit_window,text="Credits",font=("Courrier",50), bg = "black",fg="white")
    insta.grid(row=0,column=1,sticky=W) 
    inst = Label(credit_window,text="Gameplay programmers :",font=("Courrier",30), bg = "black",fg="#008000")
    inst.grid(row=1,column=0,sticky=W) 
    inst2 = Label(credit_window,text="- Ayache INZOUDDINE",font=("Courrier",15), bg = "black",fg="white")
    inst2.grid(row=2,column=0,sticky=W) 
    inst3 = Label(credit_window,text="- Kaan MARAZ",font=("Courrier",15), bg = "black",fg="white")
    inst3.grid(row=3,column=0,sticky=W) 
    inst4 = Label(credit_window,text="- Zinedine BOUARICHE",font=("Courrier",15), bg = "black",fg="white")
    inst4.grid(row=4,column=0,sticky=W) 
    inst5 = Label(credit_window,text="- Mustafa DEMIR\n",font=("Courrier",15), bg = "black",fg="white")
    inst5.grid(row=5,column=0,sticky=W)

    inst6 = Label(credit_window,text="Original soundtrack :",font=("Courrier",30), bg = "black",fg="#008000")
    inst6.grid(row=6,column=0,sticky=W) 
    inst7 = Label(credit_window,text="- Mustafa DEMIR\n",font=("Courrier",15), bg = "black",fg="white")
    inst7.grid(row=7,column=0,sticky=W)

    inst8 = Label(credit_window,text="Ressources :",font=("Courrier",30), bg = "black",fg="#008000")
    inst8.grid(row=8,column=0,sticky=W)
    inst9 = Label(credit_window,text="https://www.gamedevmarket.net/category/2d/",font=("Courrier",15), bg = "black",fg="white")
    inst9.grid(row=9,column=0,sticky=W)
    inst10 = Label(credit_window,text="https://www.pinterest.fr/",font=("Courrier",15), bg = "black",fg="white")
    inst10.grid(row=10,column=0,sticky=W)

    credit_window.mainloop()


#/////////////////////////////MENU WINDOW//////////////////////////////////////////////////////////
window = Tk()

#Menu 
window.title("Main Menu")
window.geometry("1024x768")
window.config(background ="#008000")

#creating Frame 
frame = Frame(window,bg='#008000')

#creating image 
width = 500
height = 100 
image = PhotoImage(file="images/logo_size.png")
canvas = Canvas(window, width=width, height=height)
canvas.create_image(width/2,height/2,image=image)
canvas.pack()
#add text
label_title = Label(frame,text="Name ",font=("Courrier",40), bg = "#008000",fg="black")
label_title.grid(row=1,column=0,sticky=W)
name_entry = Entry(frame,font=("Courrier",40), bg = "white",fg="black")
name_entry.grid(row=1,column=1,sticky=W)

frame.pack(expand=YES)
#addign a button 
play_button = Button(window,text="Play",font=("Courrier",40), bg = "white",fg="green",command=rungame)
play_button.pack(fill=X)
play_button = Button(window,text="Tutorial",font=("Courrier",40), bg = "white",fg="green",command=tutorial)
play_button.pack(fill=X)
play_button = Button(window,text="Credits",font=("Courrier",40), bg = "white",fg="green",command=credits)
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

#P1.name = name_entry.get()


if game.is_playing == True:
    # Game Loop
    while True:

        if game.is_playing:
            game.player.update_animation()
            game.player.start_animation()
            P1.damage(0.01)
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
                        JumpSound = pygame.mixer.Sound("Music/Jump_sound.mp3")
                        JumpSound.play()

            if jump == True and saut >= -20:
                saut -= 1
                P1.jumpy(saut)
                game.player.stop_animation()

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

            #/////Dans la versione précedent il n' avais pas ces 4 lignes 
            for fruits in game.all_fruits:
                fruits.forward()
                game.update(DISPLAYSURF)
                pygame.display.update()

             # To be run if collision occurs between Player and Enemy
            if pygame.sprite.spritecollideany(P1, enemies):
                time.sleep(0.8)

            for fruits in game.all_fruits:
                fruits.forward()
                game.update(DISPLAYSURF)
                pygame.display.update()
            #dans une autre version il n'y a pas le if 
            # To be run if collision occurs between Player and Enemy
            if pygame.sprite.spritecollideany(P1, enemies):
                time.sleep(0.8)

                DISPLAYSURF.fill(RED)
                DISPLAYSURF.blit(game_over, (30, 250))

                pygame.display.update()
                for entity in all_sprites:
                    entity.kill()
                time.sleep(1.5)
                pygame.quit()
                sys.exit()
            FramePerSec.tick(FPS)

        else:   
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        if game.gameover == True:
            Police1 = pygame.font.Font("Fonts/Eczar-ExtraBold.ttf", 110)
            Police2 = pygame.font.Font("Fonts/Eczar-SemiBold.ttf", 50)
            Gameover = Police1.render("GAME OVER ", 0, (0,0,0)) 
            YourScore = Police2.render("YOUR SCORE", 1,(255,100,100))
            HighScore = Police2.render("HIGHEST SCORE" ,1,(255,100,100))
            NameScore1 = Police2.render(P1.name + "  " + str(game.score),1,(255,50,50))
            retry_button = pygame.image.load('images/refresh.png')
            retry_button = pygame.transform.scale(retry_button, (100, 100))
            retry_button_rect = retry_button.get_rect()
            Ranking = Police2.render("TOP 10",1,(0,0,0))

            #I set the list from the file 
            rep = game.setListFromFile()
            #add the new score to the list 
            game.list_players.update({P1.name : game.score})
            #set the file with the list with my score within 
            game.setFileFromList()
            #get the the top ten 
            #getTopTen uses set ListfromFile before 
            top_ten = game.getTopTen()
            #init the element to display (classement)
            elem_list = game.initElem()
            #get the max score 
            max_score = game.getMaxTopTen()
            NameScore2 = Police2.render(max_score,1,(255,50,50))

            DISPLAYSURF.blit(Gameover, (190, 50))
            DISPLAYSURF.blit(YourScore, (100,200))
            DISPLAYSURF.blit(NameScore1, (125,250))
            DISPLAYSURF.blit(HighScore,(625,200))
            DISPLAYSURF.blit(NameScore2, (650,250))
            DISPLAYSURF.blit(retry_button,(190,500))
            DISPLAYSURF.blit(Ranking,(300,370))
            posx = 300
            posy = 450
            i=0
            while i<len(elem_list):
                DISPLAYSURF.blit(elem_list[i],(posx,posy))
                posy +=30
                i+=1

            pygame.display.update()  
            for event in pygame.event.get():
    
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if retry_button_rect.collidepoint(event.pos):
                        game.is_playing = True
                        game.game_over = False 


        pygame.display.update()   
   
        
