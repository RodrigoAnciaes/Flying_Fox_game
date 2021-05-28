from Folder_de_Testes.base import Fox_HEIGHT, Fox_WIDTH
import pygame
import random

#Parametros gerais

WIDTH = 880
HEIGHT = 400
gravity = 1


class Fox(pygame.sprite.Sprite):

    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        count_fox = 0
        Fox_WIDTH = 170
        Fox_HEIGHT = 100
        self.gravity = 1
        Fox1 = pygame.image.load('Folder_de_Testes/assets/img/raposa 1.png').convert_alpha()
        Fox1 = pygame.transform.scale(Fox1, (Fox_WIDTH, Fox_HEIGHT))
        Fox2 = pygame.image.load('Folder_de_Testes/assets/img/raposa2.png').convert_alpha()
        Fox2 = pygame.transform.scale(Fox2, (Fox_WIDTH, Fox_HEIGHT))
        Fox3 = pygame.image.load('Folder_de_Testes/assets/img/raposa 3.png').convert_alpha()
        Fox3 = pygame.transform.scale(Fox3, (Fox_WIDTH, Fox_HEIGHT))
        self.flying_one = pygame.image.load('Folder_de_Testes/assets/img/raposafinal.png').convert_alpha()
        self.flying_one = pygame.transform.scale(self.flying_one, (100, 100))

        self.images = [Fox1,Fox2,Fox3]

        self.count_fox = count_fox 
        self.image = Fox1
        
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 4
        self.rect.bottom = HEIGHT - 100
        self.speedy = 1
        
        self.now_on_windon = 0

        self.speed_modifier = 0.0

    def update(self):
        
        self.rect.y += self.speedy 

        self.speedy += self.gravity + 0.1 * (-self.speedy)

        
        self.mask = pygame.mask.from_surface(self.image)

        self.count_fox += 1

        #print(self.speed_modifier)

        if self.speed_modifier > -12:
            self.speed_modifier -= 0.0024



        
        if self.count_fox >= 10 and  self.rect.bottom > HEIGHT:

            self.now_on_windon = (self.now_on_windon + 1) % 3
            self.image = self.images[self.now_on_windon]
            self.count_fox = 0

        elif self.speedy <0 :
            self.image = self.flying_one
            #print(self.speedy)
            #print(self.count_fox)


                
        # Mantem dentro da tela
        if self.rect.bottom > HEIGHT:
        
            self.rect.bottom = HEIGHT
            #self.speedy = 1
            #game = False
        if self.rect.top < 0:
           
           self.rect.top = 0
            

    def pulo(self):

        self.speedy = -16 + self.speed_modifier

fox_group = pygame.sprite.Group()
fox = Fox()
fox_group.add(fox)







class Wall_meteor_fisic(pygame.sprite.Sprite):
    
    
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        Wall_WIDTH = 50 
        Wall_HEIGHT = random.randint(50, 250)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = (WIDTH-Wall_WIDTH)
        self.rect.y = random.randint(10,300)
        self.speedx = random.randint(-5, -3)
        Wall_HEIGHT = random.randint(50, 250)
        
        

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        Wall_WIDTH = 50
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = (WIDTH-Wall_WIDTH)
            self.rect.y = random.randint(10,300)
            self.speedx = random.randint(-5, -3)



class Invible_wall:

    def __init__(self,img):

        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()


class Wall(pygame.sprite.Sprite):
    def __init__(self, inversal, WIDTH, HEIGHT):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('Folder_de_Testes/assets/img/Tree.png').convert_alpha()
        

        if inversal:

            self.image = pygame.transaform.flip(self.image,False, True)
        self.rect = self.image.get_rect()
        self.rectx = WIDTH



class Coin(pygame.sprite.Sprite):
    def __init__(self):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        coin_HEIGHT = 50
        coin_WIDTH = 50
        self.image = pygame.image.load('Folder_de_Testes/assets/img/coin.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = (WIDTH-coin_WIDTH)
        self.rect.y = (HEIGHT  - coin_HEIGHT)
        self.speedx = random.randint(-5, -3)
        METEOR_HEIGHT = random.randint(50, 250)
        
        

    def update(self):
        # Atualizando a posição do meteoro
        METEOR_HEIGHT = random.randint(50, 250)
        self.rect.x += self.speedx
        coin_WIDTH = 50
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = (WIDTH-coin_WIDTH)
            self.rect.y = (HEIGHT - METEOR_HEIGHT)
            self.speedx = random.randint(-5, -3)
            

class Predator(pygame.sprite.Sprite):
    def __init__(self):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        coin_HEIGHT = 50
        coin_WIDTH = 50
        self.image = pygame.image.load('Folder_de_Testes/assets/img/piranha.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (coin_WIDTH, coin_HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = (WIDTH-coin_WIDTH)
        self.rect.y = random.randint(10, 300)
        self.speedx = random.randint(-5, -3)
        METEOR_HEIGHT = random.randint(50, 250)
        
        

    def update(self):
        # Atualizando a posição do meteoro
        METEOR_HEIGHT = random.randint(50, 250)
        self.rect.x += self.speedx
        coin_WIDTH = 50
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = (WIDTH-coin_WIDTH)
            self.rect.y = (HEIGHT - METEOR_HEIGHT)
            self.speedx = random.randint(-5, -3)