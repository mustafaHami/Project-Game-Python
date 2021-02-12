import pygame, sys
from Player import Player
from Fruits import Fruits
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
        self.highest_score = [0]
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
            self.highScore(self.score) 
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
            self.highScore(self.score)
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

    def highScore(self, score):
        for i in self.highest_score:
            if score > i:
                self.highest_score.insert(0,score)
                break
            

    # monster
    def spawn_monster(self):
        self.all_monsters.add(Monster(self))
    
        
    def getHighestScore(self):
        file = open("scores.txt",'r')
        line = file.readline()
        tabline = line.split(' ')
        file.close()
        highest_score = tabline[1]
        return highest_score 
    
    def getTopTen(self):
        file = open("scores.txt",'r')
        line = file.readline()
        tabline = line.split(' ')
        file.close()
        highest_score = tabline[1]
        return highest_score 
       
