
from pygame import *


class Fox:

    def __init__(self,img,flappy_sound):

        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()








class Wall:

    def __init__(self,img,colision_sound):

        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()



