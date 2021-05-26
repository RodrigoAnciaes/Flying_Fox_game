from Folder_de_Testes.base import Fox_HEIGHT, Fox_WIDTH
import pygame

#Parametros gerais

WIDTH = 880
HEIGHT = 400


class Fox(pygame.sprite.Sprite):

    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        Fox_WIDTH = 70
        Fox_HEIGHT = 70

        
        Fox1 = pygame.image.load('Folder_de_Testes/assets/img/raposafinal.png').convert_alpha()
        Fox1 = pygame.transform.scale(Fox1, (Fox_WIDTH, Fox_HEIGHT))
        Fox2 = pygame.image.load('Folder_de_Testes/assets/img/snowflake.png').convert_alpha()
        Fox2 = pygame.transform.scale(Fox2, (Fox_WIDTH, Fox_HEIGHT))
        Fox3 = pygame.image.load('Folder_de_Testes/assets/img/Fox.jpeg').convert_alpha()
        Fox3 = pygame.transform.scale(Fox3, (Fox_WIDTH, Fox_HEIGHT))

        self.images = [Fox1,Fox2,Fox3]

        
        self.image = Fox1
        
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 4
        self.rect.bottom = HEIGHT - 200
        self.speedy = 4 
        
        self.now_on_windon = 0
    def update(self):
        
        self.rect.y += self.speedy 

        self.now_on_windon = (self.now_on_windon + 1) % 3
        self.image = self.images[self.now_on_windon]

                # Atualização da posição da nave
        # Mantem dentro da tela
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            #game = False
        if self.rect.top < 0:
           self.rect.top = 0
            #game = False

fox_group = pygame.sprite.Group()
fox = Fox()
fox_group.add(fox)







class Wall:

    def __init__(self,img,colision_sound):

        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()



class Invible_wall:

    def __init__(self,img):

        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()