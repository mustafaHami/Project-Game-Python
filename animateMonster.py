import pygame

class AnimateMonsterSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'images_ennemies/{sprite_name}.png')
        self.tailleY = 130
        self.tailleX = 130
        self.image = pygame.transform.scale(self.image,(self.tailleX,self.tailleY))
        self.current_image = 0
        self.images = animation.get(sprite_name)

    # animer le sprite
    def animate(self):
        # passer a l'image suivante
        self.current_image += 1
        if self.current_image >= len(self.images):
            self.current_image = 0

        self.image = self.images[self.current_image]

def load_animation_images(sprite_name):
    # charger les images
    images = []
    path = f"images_ennemies/{sprite_name}/{sprite_name}"

    for num in range(1, 24):
       images_path = path + str(num) + '.png'
       images.append(pygame.transform.scale(pygame.image.load(images_path),(100,100)))

    # renvoie la liste d'image
    return images


animation = {
    "Goblinrunleft" : load_animation_images('Goblinrunleft')
}