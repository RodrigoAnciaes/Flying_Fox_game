# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()
assets = []
# ----- Gera tela principal
WIDTH = 880
HEIGHT = 660
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flying_Fox')
gravity = 1
difficult = 0

count_fox = 0
# ----- Inicia assets
METEOR_WIDTH = 100
METEOR_HEIGHT = random.randint(300, 450)
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('Folder_de_Testes/assets/img/snow_day.jpeg').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
meteor_img = pygame.image.load('Folder_de_Testes/assets/img/Tree.png').convert_alpha()
meteor_img = pygame.transform.scale(meteor_img, (METEOR_WIDTH, METEOR_HEIGHT))

score_font = pygame.font.Font('Folder_de_Testes/assets/img/PressStart2P.ttf', 28)

# ----- Inicia estruturas de dados
# Definindo os novos tipos
class Fox(pygame.sprite.Sprite):

    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        count_fox = 0
        Fox_WIDTH = 170
        Fox_HEIGHT = 100
        Fox1 = pygame.image.load('Folder_de_Testes/assets/img/raposa 1.png').convert_alpha()
        Fox1 = pygame.transform.scale(Fox1, (Fox_WIDTH, Fox_HEIGHT))
        Fox2 = pygame.image.load('Folder_de_Testes/assets/img/raposa2.png').convert_alpha()
        Fox2 = pygame.transform.scale(Fox2, (Fox_WIDTH, Fox_HEIGHT))
        Fox3 = pygame.image.load('Folder_de_Testes/assets/img/raposa 3.png').convert_alpha()
        Fox3 = pygame.transform.scale(Fox3, (Fox_WIDTH, Fox_HEIGHT))

        self.images = [Fox1,Fox2,Fox3]

        self.count_fox = count_fox
        self.image = Fox1
        
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 4
        self.rect.bottom = HEIGHT - 100
        self.speedy = 1
        
        self.now_on_windon = 0
    def update(self):
        
        self.rect.y += self.speedy 

        self.speedy += gravity + 0.1 * (-self.speedy)

        
        self.mask = pygame.mask.from_surface(self.image)

        self.count_fox += 1



        
        if self.count_fox == 10:

            self.now_on_windon = (self.now_on_windon + 1) % 3
            self.image = self.images[self.now_on_windon]
            self.count_fox = 0


                
        # Mantem dentro da tela
        if self.rect.bottom > HEIGHT:
            pygame.QUIT
            self.rect.bottom = HEIGHT
            #game = False
        if self.rect.top < 0:
           pygame.QUIT
           self.rect.top = 0
            

    def pulo(self):
        
        self.speedy += -18
        

class Meteor(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        METEOR_HEIGHT = random.randint(50, 250)
        self.image = img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = (WIDTH-METEOR_WIDTH)
        self.rect.y = (500)
        self.speedx = random.randint(-5, -3)
        METEOR_HEIGHT = random.randint(50, 250)
        
        

    def update(self):
        # Atualizando a posição do meteoro
        METEOR_HEIGHT = random.randint(50, 250)
        self.rect.x += self.speedx
        
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = (WIDTH-METEOR_WIDTH)
            self.rect.y = (500)
            self.speedx = random.randint(-5, -3)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        coin_HEIGHT = 50
        coin_WIDTH = 50
        self.image = pygame.image.load('Folder_de_Testes/assets/img/coin.png').convert_alpha()
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
            
score = 0
score_coin = 0
game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30 

# Criando um grupo de meteoros
all_sprites = pygame.sprite.Group()
all_meteors = pygame.sprite.Group()
all_coins =   pygame.sprite.Group()
# Criando o jogador
player = Fox()
all_sprites.add(player)
# Criando os meteoros
for i in range(1):
    meteor = Meteor(meteor_img)
    all_sprites.add(meteor)
    all_meteors.add(meteor)

coin = Coin()
all_coins.add(coin)
all_sprites.add(coin)

# ===== Loop principal =====
while game:
    fpdif = FPS + difficult
    #print(fpdif)
    clock.tick(fpdif)
    #print(clock)
    difficult += 0.01

    if fpdif > 68:
        fpdif = 68

    print(int(fpdif))

    score = int(difficult) + score_coin

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
        
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_SPACE:
                Fox.pulo(player)
                
            

    # ----- Atualiza estado do jogo
    # Atualizando a posição dos meteoros
    all_sprites.update()
    
    hits = pygame.sprite.spritecollide(player,all_meteors,True, pygame.sprite.collide_mask)
    
    colect_coin = pygame.sprite.spritecollide(player,all_coins,True, pygame.sprite.collide_mask)

    for coin in colect_coin:
        score_coin += 10
        c = Coin()
        all_coins.add(c)
        all_sprites.add(c)
        #Coin.self.rect.x =  (WIDTH-50)


    if len(hits) > 0:
        game = False
    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    # Desenhando meteoros
    all_sprites.draw(window)

    text_surface = score_font.render("{:08d}".format(score), True, (255, 255, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (WIDTH / 2,  10)
    window.blit(text_surface, text_rect)

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados