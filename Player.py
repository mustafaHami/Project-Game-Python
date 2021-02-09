from pygame.locals import *
import time
import pygame



class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.jump = 5
        self.image = pygame.image.load('images/tree_player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 70
        self.rect.y = 550

    def damage(self, amount):
        self.health -= amount

    def bonus(self, amount):
        self.health += amount

    def update_health_bar(self, surface):    
        pygame.draw.rect(surface,(30,30,30),[5, 5, self.max_health * 5 + 10, 30])
        pygame.draw.rect(surface,((100 - self.health) * 255 / 100, self.health* 255 / 100 ,0),[10,10,self.health * 5,20])


    def move_right(self):
        if not self.game.check_collision(self, self.game.all_fruits):
            self.rect.x += self.velocity
        for fruit in self.player.game.check_collision(self, self.player.game.all_fruits):
            fruit.damage(10)


    def move(self):
        pressed_keys = pygame.key.get_pressed()
        # if pressed_keys[K_UP]:
        # self.rect.move_ip(0, -5)
        # if pressed_keys[K_DOWN]:
        # self.rect.move_ip(0,5)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-9, 0)
        if self.rect.right < 1024:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(9, 0)



    def jumpy(self,saut):
        if saut != -20: 
            self.rect.y -= saut
