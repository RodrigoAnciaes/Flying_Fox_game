# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 880
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flying_Fox')

# ----- Inicia assets
METEOR_WIDTH = 50
METEOR_HEIGHT = random.randint(50, 250)
SHIP_WIDTH = 70
SHIP_HEIGHT = 70
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('Folder_de_Testes/assets/img/snow_day.jpeg').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
meteor_img = pygame.image.load('Folder_de_Testes/assets/img/Tronco1.png').convert_alpha()
meteor_img = pygame.transform.scale(meteor_img, (METEOR_WIDTH, METEOR_HEIGHT))
ship_img = pygame.image.load('Folder_de_Testes/assets/img/Fox.jpeg').convert_alpha()
ship_img = pygame.transform.scale(ship_img, (SHIP_WIDTH, SHIP_HEIGHT))

# ----- Inicia estruturas de dados
# Definindo os novos tipos
class Ship(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 4
        self.rect.bottom = HEIGHT - 200
        
        self.speedy = 4 * (self.rect.y * 0.01) 

    def update(self):
        # Atualização da posição da nave
        
        self.rect.y += self.speedy 

        # Mantem dentro da tela
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            #game = False
        if self.rect.top < 0:
            self.rect.top = 0
            #game = False

class Meteor(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = (WIDTH-METEOR_WIDTH)
        self.rect.y = random.randint(METEOR_HEIGHT,400)
        self.speedx = random.randint(-5, -3)
        

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = (WIDTH-METEOR_WIDTH)
            self.rect.y = random.randint(METEOR_HEIGHT,400)
            self.speedx = random.randint(-5, -3)
            

game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

# Criando um grupo de meteoros
all_sprites = pygame.sprite.Group()
# Criando o jogador
player = Ship(ship_img)
all_sprites.add(player)
# Criando os meteoros
for i in range(2):
    meteor = Meteor(meteor_img)
    all_sprites.add(meteor)

# ===== Loop principal =====
while game:
    clock.tick(FPS)
    

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_SPACE:
                player.speedy += -20
            
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_SPACE:
                player.speedy += 20
            

    # ----- Atualiza estado do jogo
    # Atualizando a posição dos meteoros
    all_sprites.update()

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    # Desenhando meteoros
    all_sprites.draw(window)

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados