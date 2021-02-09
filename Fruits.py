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
        self.rect.x = 900 + random.randint(0, 500)
        self.rect.y = 600
        self.velocity = 5

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.rect.x = 900
    
    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.rect.x = 1300

