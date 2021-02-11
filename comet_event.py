import pygame
from comet import Comet

class CometFallEvent:

    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 70
        self.all_comets = pygame.sprite.Group()
        self.game = game
    def add_percent(self):
        self.percent += self.percent_speed/100

    def is_full_loded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def comet(self):
        self.all_comets.add(Comet(self))

    def attempt_fall(self):
        if self.is_full_loded():
            self.comet()
            self.reset_percent()

    def update_bar(self, surface):
        self.add_percent()
        # declench le pluie
        self.attempt_fall()
        #bare noir
        pygame.draw.rect(surface, (0,0,0), [
            0, # axe x
            surface.get_height() -20,# axe Y
            surface.get_width(),# longeur de la fenetre
            10 # epaisseur de la barre
        ])
        # barre rouge
        pygame.draw.rect(surface, (187,11,11), [
            0, # axe x
            surface.get_height() -20,# axe Y
            (surface.get_width() / 100) * self.percent,# longeur de la fenetre
            10 # epaisseur de la barre
        ])