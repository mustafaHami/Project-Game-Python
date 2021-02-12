import pygame, sys
import os 
from Player import Player
from Fruits import Fruits
from pygame.locals import *

from monster import Monster
from comet_event import CometFallEvent
DISPLAYSURF = pygame.display.set_mode((1024, 768))

class Game:

    def __init__(self):
        #define if the game is started or not 
        self.is_playing = True
        #player status
        #self.is_playing = False
        # generate a player
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.score = 0
        #self.highScore = 0
        self.top_ten =  {}
        self.list_players = {}
        #generate fruits
        self.all_fruits = pygame.sprite.Group()
        self.pressed = {}
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.spawn_monster()
        self.monster = Monster(self)
        #comet
        self.comet_event = CometFallEvent(self)
        self.enVie = "first"
        self.gameover = False
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.font_fin = pygame.font.SysFont("Verdana", 20)
        self.screen = pygame.display.set_mode((1024, 768))
        self.nbSom = 1
        self.event = pygame.event.get()
        self.arret = False
        self.sleep = True

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
    def start(self):
        self.is_playing = True
        for i in range(5):
            self.spawn_fruit()

    def game_over(self):

        if self.enVie == "first" and self.nbSom == 1:

            self.player.rect.x = -10000
            self.arret = True

            if self.sleep == True:
                pygame.mixer.music.load("son/sleep.mp3")
                pygame.mixer.music.play(-1)
                self.sleep = False

            self.player.healthbar = False
            for self.event in pygame.event.get():
                if self.event.type == pygame.MOUSEBUTTONUP:
                    self.arret = False
                    pygame.mixer.music.load("son/wordl22.mp3")
                    pygame.mixer.music.play(-1)
                    self.enVie = "second"
                    self.player.health = self.player.max_health
                    self.nbSom += 1
                    self.player.rect.x = 70
                    self.player.healthbar = True
        elif self.enVie == "second":
            self.player.mouvement = False
            self.monster.monstermouvement = False
            self.gameover = True
            self.player.gameover=True
            self.all_fruits = pygame.sprite.Group()
            self.player.healthbar = False
            self.player.mouvement = False
            self.player.rect.x = -10000
            self.player.affichage = False
            self.nbSom += 1
        else:
            self.player.mouvement = False
            self.monster.monstermouvement = False
            self.gameover = True
            self.player.gameover=True
            self.all_fruits = pygame.sprite.Group()
            self.player.healthbar = False
            self.player.mouvement = False
            self.player.rect.x = -10000
            self.player.affichage = False
            self.nbSom += 1




    def update(self):
        Police = pygame.font.Font("Fonts/bold_game_font_7.ttf", 20)
        Rendu = Police.render(f"Score : {self.score}", 1, (255,255,255)) 
        screen.blit(Rendu, (10, 40))

    def update_comet(self, screen):
        self.comet_event.update_bar(screen)
        self.comet_event.all_comets.draw(screen)

    def spawn_fruit(self):
        fruit = Fruits(self)
        self.all_fruits.add(fruit)


    def setListFromFile(self):
        #verify if the file exists
        if os.path.exists("scores.txt"):
            file = open("scores.txt",'r')
            line = file.readline()
            #if the first line is not empty it take the first line 
            # if line != '':
            #     tabline = line.split(' ')
            #     name = tabline[0]
            #     score = tabline[1]
            #     score = int(score)
            #     self.list_players.update({name : score})
            i = 0
                #while the line is not empty we take the players 
            while line != '':
                if line != '':
                    tabline = line.split(' ')
                    name = tabline[0]
                    score = tabline[1]
                    score = int(score)
                    self.list_players.update({name : score})
                line = file.readline()
            return self.list_players
            # else: 
            #     return "vide"
        else: 
            return "vide"

    def setFileFromList(self):
        file = open("scores.txt",'w+')
        top_ten = self.getTopTen()
        if type(top_ten) is not str:
            for name in top_ten:
                file.write(name)
                file.write(' ')
                file.write(str(top_ten[name]))
                file.write(' ')
                file.write('\n')
        else: 
                file.write(top_ten)
                file.write(' ')
                file.write('\n')


    # def highScore(self, score):
    #     for i in self.highest_score:
    #         if score > i:
    #             self.highest_score.insert(0,score)
    #             break
            

    # monster
    def spawn_monster(self):
        self.all_monsters.add(Monster(self))
    
        
    def getHighestScore(self):
        file = open("scores.txt",'r')
        line = file.readline()
        tabline = line.split(' ')
        file.close()

    def getMaxList(self):
        #initialize the list 
        max = 0 
        max_name  = ''
        for name in self.list_players:
            if self.list_players[name] > max: 
                max = self.list_players[name]
                max_name = name 
        #max et max name sont le meilleur score 
        max = str(max)
        best = max_name + ' ' + max
        return best 


    def getTopTen(self):
        code = self.setListFromFile()

        if code != "vide":
            list_size = len(self.list_players)
            i=0 
            while i  < list_size and i < 10:
                max_list = self.getMaxList()
                tabline = max_list.split(' ')
                name = tabline[0]
                score = tabline[1]
                score = int(score)        
                self.top_ten.update({name : score})
                self.list_players.pop(name)
                i+=1
            return self.top_ten
        else: 
            name_score = self.player.name + ' ' + str(self.score)
            return name_score


    def initElem(self):
        #self.setListFromFile()
        font = pygame.font.SysFont("Verdana", 30)
        elem_list = []
        top_ten  = self.getTopTen()
        i=0
        if type(top_ten) is not str : 
            for name in top_ten:
                elem_list.insert(i,font.render(name + ' ' + str(top_ten.get(name)),1,(0,0,0))) 
                i+=1
            return elem_list 
        else:
            elem_list.insert(0,font.render(top_ten,1,(0,0,0)))
            return elem_list

    def getMaxTopTen(self):
        top_ten = self.getTopTen()
        max = 0 
        max_name  = ''
        if type(top_ten) is not str: 
            for name in top_ten:
                    if top_ten[name] > max: 
                        max = top_ten[name]
                        max_name = name 
                #max et max name sont le meilleur score 
            max = str(max)
            best = max_name + ' ' + max
            return best
        else: 
            return top_ten
        
 

       
