from pygame.locals import *
from projectile import Projectile
import time
import pygame
import animation



class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("ArmatureWalk")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.healthbar = True
        self.attack = 10
        self.velocity = 5
        self.all_projectile = pygame.sprite.Group()
        self.jump = 5
        self.rect = self.image.get_rect()
        self.rect.x = 70
        self.rect.y = 550
        self.game = game
        self.mouvement = True
        self.name = '' 
        self.gameover = False

    def projectile(self):
        if self.gameover == False:
            self.all_projectile.add(Projectile(self))

    def damage(self, amount):
        if self.health > amount:
            self.health -= amount
        else:
            self.game.game_over()
        

    def bonus(self, amount):
        self.health += amount

    def update_animation(self):
        self.animate()

        
    def update_health_bar(self, surface):    
        if self.healthbar == True:
            pygame.draw.rect(surface,(30,30,30),[5, 5, self.max_health * 5 + 10, 30])
            pygame.draw.rect(surface,((100 - self.health) * 255 / 100, self.health* 255 / 100 ,0),[10,10,self.health * 5,20])


    def moveforSecondWorld(self):
        pressed_keys = pygame.key.get_pressed()
        if not self.game.check_collision(self, self.game.all_monsters):
            if self.rect.right < 1024:
                if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
                    self.rect.move_ip(9, 0)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT] or pressed_keys[K_q]:
                self.rect.move_ip(-9, 0)



    def move(self):
       
        if self.mouvement == True:

            pressed_keys = pygame.key.get_pressed()
            # if pressed_keys[K_UP]:
            # self.rect.move_ip(0, -5)
            # if pressed_keys[K_DOWN]:
            # self.rect.move_ip(0,5)
            if self.rect.left > 0:
                if pressed_keys[K_LEFT] or pressed_keys[K_q]:
                    self.rect.move_ip(-9, 0)
            if self.rect.right < 1024:
                if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
                    self.rect.move_ip(9, 0)

    def jumpy(self,saut):
        if self.mouvement == True:   
            if saut != -20:
                    self.rect.y -= saut
                    self.stop_animation()

