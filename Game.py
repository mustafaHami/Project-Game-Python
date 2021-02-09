import pygame
from Player import Player
<<<<<<< HEAD


from Fruits import Fruits


=======
from Fruits import Fruits

>>>>>>> 293d8569f15e4a46cca40bc40b5c6be6b7ed0f6a
class Game:

    def __init__(self):
        #player status
        #self.is_playing = False
        # generate a player 
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #generate fruits
        self.all_fruits = pygame.sprite.Group()
        self.pressed = {}
        for i in range(3):
            self.spawn_fruit()
    
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_fruit(self):
        fruit = Fruits(self)
        self.all_fruits.add(fruit)