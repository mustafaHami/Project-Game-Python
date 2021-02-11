import pygame
import random
import animateMonster

class Monster(animateMonster.AnimateMonsterSprite):

    def __init__(self, game):
        super().__init__("Goblinrunleft")
        self.game = game
        self.health = 110
        self.max_health = 110
        self.attack = 0.2
        self.rect = self.image.get_rect()
        self.rect.x = 900 + random.randint(0, 200)
        self.rect.y = 560
        self.velocity = random.randint(2,5)
        self.nb = 10

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            self.nb -= 1
            self.attack += 0.2
            # réapparaitre le meme monstre
            self.tailleY += 20
            #self.image = pygame.transform.scale(self.image, (self.tailleX, self.tailleY))
            self.rect.x = 900 + random.randint(0, 200)
            self.rect.y -= 21
            self.max_health += 20
            self.velocity = random.randint(2,4)
            self.health = self.max_health
            for i in range(0, 23):
                self.images[i] = pygame.transform.scale(self.images[i], (self.tailleX, self.tailleY))

    def nbKill(self):
        return self.nb

    def update_animation(self):
        self.animate()

    def update_health_bar(self,surface):
        # definir une couleur pour la jauge(vert clair)
        bar_color = (111,210,46)
        # couleur pour l'arrière plan
        black_bar_color = (60,63,60)
        # definir la position de la jauge de vie largeur et épaisseur
        #bar_position = [x, y, w, h]

        bar_position =[self.rect.x, self.rect.y, self.health, 5]
        black_bar_position =[self.rect.x, self.rect.y, self.max_health, 5]

        # draw bar
        pygame.draw.rect(surface, black_bar_color, black_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):

        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # monstre colision avec le joueur

        else:
            self.game.player.damage(self.attack)

    def remisZero(self):
        self.rect.y = 560
        self.max_health = 110
        self.health = 110
        self.nb = 10
        self.attack = 0.2
