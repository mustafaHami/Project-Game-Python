from tkinter import * 
import pygame, sys
import os 
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

        self.moving_speed = 7

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
    inst3 = Label(tuto_window,text="Collect the normal fruits and vegetables to increase your score and your sleep bar !",font=("Courrier",15), bg = "#008000",fg="black")
    inst3.grid(row=2,column=0,sticky=W) 
    inst4 = Label(tuto_window,text="If your sleep bar is empty, you will fall asleep",font=("Courrier",15), bg = "#008000",fg="black")
    inst4.grid(row=3,column=0,sticky=W) 
    inst5 = Label(tuto_window,text="You need to face the monsters of your nightmare to wake up and continue your escape",font=("Courrier",15), bg = "#008000",fg="black")
    inst5.grid(row=4,column=0,sticky=W)
    inst6 = Label(tuto_window,text="If you fail, you die",font=("Courrier",15), bg = "#008000",fg="black")
    inst6.grid(row=5,column=0,sticky=W) 
    inst7 = Label(tuto_window,text="You can move left or right with directionnal buttons",font=("Courrier",15), bg = "#008000",fg="black")
    inst7.grid(row=6,column=0,sticky=W)
    inst8 = Label(tuto_window,text="Jump with the space bar or up button, and shoot with the space bar when you're asleep",font=("Courrier",15), bg = "#008000",fg="black")
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
#music = pygame.mixer.music.load("son/Wordl2.mp3")
# Game Loop

if game.is_playing == True:
    # Game Loop
    while True:
        if game.enVie == 'first':
            
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

                pygame.display.update()
                '''for entity in all_sprites:
                    entity.kill()
                time.sleep(1.5)
                pygame.quit()
                sys.exit()'''
          
        elif game.enVie == "second":
            
            
            DISPLAYSURF.fill((30,30,30))
            DISPLAYSURF.blit(pygame.font.SysFont("Verdana", 35).render("CLICK DEUX FOIS POUR ALLER DANS L'AUTRE MONDE",True, (255,255,255)), (30,350))

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
            for projectile in game.player.all_projectile:
                projectile.move()
            # appliquer les porjectile
            game.player.all_projectile.draw(DISPLAYSURF)

            # recupere les monstres
            for monster in game.all_monsters:
                monster.forward()
                monster.update_health_bar(DISPLAYSURF)
                monster.update_animation()
                DISPLAYSURF.blit(font.render(str(monster.nbKill()), True, WHITE), (20, 350))
                if monster.nbKill() == 0 and game.game_over == False:
                    pygame.mixer.music.set_volume(0)
                    DISPLAYSURF.fill(BLACK)
                    DISPLAYSURF.blit(
                    font_fin.render("CLICK DEUX FOIS POUR ALLER DANS RETOURNER DANS VOTRE MONDE", True, WHITE),
                    (20, 350))                    
                    if event.type == pygame.MOUSEBUTTONUP:
                        game.enVie = "first"
                        P1.health = P1.max_health


                    # game over
                    '''if game.game_over = True:
                    for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()'''
                else:
                    # appliquer les monstre
                    game.all_monsters.draw((DISPLAYSURF))
                    # Moves and  Re-draws
                    for comet in game.comet_event.all_comets:
                        comet.fall()

                    for entity in all_sprites:
                        DISPLAYSURF.blit(entity.image, entity.rect)
                        entity.moveforSecondWorld()
                    game.player.update_health_bar(DISPLAYSURF)

        if game.gameover == True:
            Police1 = pygame.font.Font("Fonts/Eczar-ExtraBold.ttf", 110)
            Police2 = pygame.font.Font("Fonts/Eczar-SemiBold.ttf", 50)
            Gameover = Police1.render("GAME OVER ", 0, (0,0,0))
            YourScore = Police2.render("YOUR SCORE", 1,(255,100,100))
            HighScore = Police2.render("HIGH SCORE" ,1,(255,100,100))
            NameScore1 = Police2.render(P1.name + "  " + str(game.score),1,(255,50,50))
            retry_button = pygame.image.load('images/refresh.png')
            retry_button = pygame.transform.scale(retry_button, (100, 100))
            retry_button_rect = retry_button.get_rect()


            if os.path.exists("scores.txt"):
                if os.path.getsize("scores.txt") == 0:
                    file = open("scores.txt","w")
                    file.write(game.player.name)
                    file.write(' ')
                    file.write(str(game.score))
                    file.write(' ')
                    file.write('\n')
                    file.close()
                    file = open("scores.txt",'r')
                    line = file.readline()
                    tabline = line.split(' ')
                    file.close()
                    name = tabline[0]
                    highest_score = tabline[1]
                    Score2 = Police2.render(name + "  " + str(int(highest_score)),1,(255,50,50))
                else:
                    file = open("scores.txt",'r')
                    line = file.readline()
                    tabline = line.split(' ')
                    file.close()
                    name = tabline[0]
                    highest_score = tabline[1]
                    NameScore2 = Police2.render(name + "  " + highest_score,1,(255,50,50))
                    if game.score > int(highest_score):
                        Score2 = Police2.render(name + "  " + str(game.score),1,(255,50,50))
                        file = open("scores.txt","w")
                        file.write(game.player.name)
                        file.write(' ')
                        file.write(str(game.score))
                        file.write(' ')
                        file.write('\n')
                        file.close()                                
            else:
                file = open("scores.txt","w")
                file.write(game.player.name)
                file.write(' ')
                file.write(str(game.score))
                file.write(' ')
                file.write('\n')
                NameScore2 = Police2.render(game.player.name + "  " + str(game.score),1,(255,50,50))
                file.close()           
            DISPLAYSURF.blit(Gameover, (190, 50))
            DISPLAYSURF.blit(YourScore, (100,225))
            DISPLAYSURF.blit(NameScore1, (125,350))
            DISPLAYSURF.blit(HighScore,(625,225))
            DISPLAYSURF.blit(NameScore2, (650,350))
            DISPLAYSURF.blit(retry_button,(190,500))
        
        pygame.display.update()
        FramePerSec.tick(FPS)



        
   
        
