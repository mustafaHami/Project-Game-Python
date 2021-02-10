import pygame

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(f'animation/{sprite_name}.png'),(75,125))
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False
    
    def start_animation(self):
        self.animation = True
    
    def stop_animation(self):
        self.animation = False

    def animate(self):

        if self.animation:

            self.current_image += 1

            if self.current_image >= len(self.images):
                self.current_image = 0

            self.image = self.images[self.current_image]       



def load_animation_images(sprite_name):

    images = []

    path = f'animation/{sprite_name}/{sprite_name}'

    for num in range(1,28):
        image_path = path + str(num) + '.png'
        images.append(pygame.transform.scale(pygame.image.load(image_path),(75,125)))

    
    return images


animations = {
    'ArmatureWalk' : load_animation_images('ArmatureWalk')
}

