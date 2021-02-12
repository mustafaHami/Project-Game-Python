import pygame
import random

class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load("images/asteroid.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(5,550)
        self.tailleY = random.randint(80,130)
        self.tailleX = self.tailleY
        self.image = pygame.transform.scale(self.image,(self.tailleX,self.tailleY))
        self.velocity = random.randint(5,15)
        self.rect.y = - random.randint(0,770)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)

    def fall(self):
        self.rect.y += self.velocity

        if self.rect.y >= 650:
            self.remove()

        # verifier si le meteroirt touche le jouer
        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_players
        ):
            # disparaitre la meteroite
            self.remove()
            # enlever des vie au joueur
            self.comet_event.game.player.damage(50)