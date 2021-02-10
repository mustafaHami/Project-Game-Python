import pygame, sys
import os 
from Player import Player
from Fruits import Fruits
DISPLAYSURF = pygame.display.set_mode((1024, 768))

class Game:

    def __init__(self):
        #define if the game is started or not 
        self.is_playing = False
        # generate a player 
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.score = 0
        self.highest_score = [0]
        #generate fruits
        self.all_fruits = pygame.sprite.Group()
        self.pressed = {}
    
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
    def start(self):
        self.is_playing = True
        for i in range(5):
            self.spawn_fruit()

    def game_over(self):
        self.all_fruits = pygame.sprite.Group()
        self.player.healthbar = False
        self.is_playing = False
        self.player.mouvement = False
        print("Game Over !")
        self.highScore(self.score) 
        #open the score file to get the highest score 
        if os.path.exists("scores.txt"):
            file = open("scores.txt",'r')
            line = file.readline()
            tabline = line.split(' ')
            file.close()
            highest_score = tabline[1]

            if self.score > int(highest_score):
                file = open("scores.txt","w")
                file.write(self.player.name)
                file.write(' ')
                file.write(str(self.score))
                file.write('\n')
                file.close()
        else:
            file = open("scores.txt","w")
            file.write(self.player.name)
            file.write(' ')
            file.write(str(self.score))
            file.write('\n')
            file.close()

    def update(self, screen):
        Police = pygame.font.Font("Fonts/bold_game_font_7.ttf", 40)
        Rendu = Police.render(f"Score : {self.score}", 1, (255,255,255)) 
        screen.blit(Rendu, (10, 40))

    def spawn_fruit(self):
        fruit = Fruits(self)
        self.all_fruits.add(fruit)

    def highScore(self, score):
        for i in self.highest_score:
            if score > i:
                self.highest_score.insert(0,score)
                break
    
        
    def getHighestScore(self):
        file = open("scores.txt",'r')
        line = file.readline()
        tabline = line.split(' ')
        file.close()
        highest_score = tabline[1]
        return highest_score 
       