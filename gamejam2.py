import pygame
from Game import Game
pygame.init()

# genere la fenetre
pygame.display.set_caption("DarkForest")
fenetre = pygame.display.set_mode((1024, 680))

# l'arrière plan
background = pygame.image.load('images/day_forest.png')

# charger le jeu
game = Game()

running = True
while running:
    # appliquer l'arriere plan
    fenetre.blit(background, (0, 0))
    # applique le joueur du jeu
    fenetre.blit(game.player.image, game.player.rect)
    # mes a jour la fenetre
    pygame.display.flip()
    # traiter chaque touche du joueur
    for event in pygame.event.get():
        # fermer la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fin du jeu")
        # lacher une touche
        elif event.type == pygame.KEYDOWN:
            # quelle touche a été utilisé
            if event.key == pygame.K_RIGHT:
                print("droite")
            elif event.key == pygame.K_LEFT:
                print("gauche")
            elif event.key == pygame.K_UP:
                print("haut")
