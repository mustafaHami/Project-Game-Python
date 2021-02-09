import pygame
import random

eat = ["strawberry", "kiwi","orange","banana","coconut","grape","green_apple"]
eat2 = ["strawberry", "kiwi","orange","banana","coconut","grape","green_apple", "chainsaw"]

class Fruits(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.damage = 30
        self.bonus = 1
        self.image_name = "kiwi"
        self.image = pygame.image.load("images/"+random.choice(eat)+".png")
        self.rect = self.image.get_rect()
        self.rect.x = 900 + random.randint(0, 700)
        self.rect.y = 550
        self.velocity = 5
        self.score = 0

    def damage(self, amount):
        self.health -= amount
    
    def getVelocity(self):
        return self.velocity
    
    def myScore(self):
        return self.score
    
    def forward(self):
        if self.image_name != "chainsaw":
            #if the player does not collide a fruit
            if not self.game.check_collision(self, self.game.all_players):
                self.rect.x -= self.velocity
                if self.rect.x <= -200:
                    self.image_name = random.choice(eat2)
                    self.image = pygame.image.load("images/"+self.image_name+".png")
                    self.rect.x = 1300 + random.randint(0,100)
            else:
                
                #if the player does collide a fruit:
                #the velocity is increased little by little
                self.velocity += 0.2
                if self.velocity > 25:
                    self.velocity = 25
                self.game.score = self.game.score + 10 + int(self.velocity)
                self.score = self.game.score + 10 + int(self.velocity)
                self.image_name = random.choice(eat2)
                if(self.game.player.health <= 97):
                    self.game.player.bonus(self.bonus)
                self.rect.x = 1300 + random.randint(0,100)
                self.image = pygame.image.load("images/"+self.image_name+".png")

                position = random.randint(1,2)

                if position == 1:
                    self.rect.y = 400
                    self.image = pygame.image.load("images/"+self.image_name+".png")
                else:
                    self.rect.y = 550
                    self.image = pygame.image.load("images/"+self.image_name+".png")
                position = random.randint(1,2)
                
   


        elif self.image_name == "chainsaw":
            #if the player does not collide a fruit
            if not self.game.check_collision(self, self.game.all_players):
                self.rect.x -= self.velocity
                if self.rect.x <= -200:
                    self.image_name = random.choice(eat2)
                    self.rect.x = 1300 + random.randint(0,100)
                    self.image = pygame.image.load("images/"+self.image_name+".png")
            else:
                self.velocity += 0.2
                if self.velocity > 25:
                    self.velocity = 25
                self.game.score = self.game.score - 10
                self.score = self.game.score - 10
                self.image_name = random.choice(eat2)
                self.game.player.damage(self.damage)
                self.rect.x = 1300 + random.randint(0,100)
                self.image = pygame.image.load("images/"+self.image_name+".png")

                position = random.randint(1,2)

                if position == 1:
                    self.rect.y = 400
                    self.image = pygame.image.load("images/"+self.image_name+".png")
                else:
                    self.rect.y = 550
                    self.image = pygame.image.load("images/"+self.image_name+".png")
                position = random.randint(1,2)

