import pygame
import random

eat = ["strawberry", "kiwi","orange","banana","coconut","grape","green_apple","chainsaw"]

class Fruits(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 1
        self.image = pygame.image.load("images/"+random.choice(eat)+".png")
        self.rect = self.image.get_rect()
        self.rect.x = 900 + random.randint(0, 700)
        self.rect.y = 550
        self.velocity = 5
        self.score = 0

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.rect.x = 900
    
    def scoreAdd(self):
        if self.game.check_collision(self, self.game.all_players):
            self.score += 10
            print(4)
        return self.score
    
    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
            if self.rect.x <= -200:
                self.rect.x = 1300 + random.randint(0,200)
                self.image = pygame.image.load("images/"+random.choice(eat)+".png")
        else:
            self.scoreAdd
            self.velocity += 0.10
            if self.velocity == 10:
                self.velocity = 10
            self.image = pygame.image.load("images/"+random.choice(eat)+".png")
            self.rect.x = 1300 + random.randint(0,200)
            position = random.randint(1,2)

            if position == 1:
                self.rect.y = 400
                self.image = pygame.image.load("images/"+random.choice(eat)+".png")
            else:
                self.rect.y = 550
                self.image = pygame.image.load("images/"+random.choice(eat)+".png")

   

            

