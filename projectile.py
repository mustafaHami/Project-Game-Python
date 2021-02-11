import pygame
import random

eat = ["strawberry", "kiwi", "orange", "banana", "coconut", "grape", "green_apple", "Cabbage", "Carrot", "Broccoli",
       "Cucumber", "Pumpkin", "Tomato"]
eat2 = ["strawberry", "kiwi", "orange", "banana", "coconut", "grape", "green_apple", "Cabbage", "Carrot", "Broccoli",
        "Cucumber", "Pumpkin", "Tomato", "cursed_apple", "cursed_strawberry", "cursed_banana"]

class Projectile(pygame.sprite.Sprite):

    def __init__(self,player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load("images/" + random.choice(eat) + ".png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = self.player.rect.x + 60
        self.rect.y = self.player.rect.y + 40
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 10
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectile.remove(self)

    def move(self):    
        self.rect.x += self.velocity
        self.rotate()

        # colision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            monster.damage(self.player.attack)


        # verifier si le projectile a toucher un ennemies
        if self.rect.x > 1000:
            self.remove()