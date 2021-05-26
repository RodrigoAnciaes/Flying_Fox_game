# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 880
HEIGHT = 800
Fox_WIDTH = 70
Fox_HEIGHT = 70

gravity = 1


window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flying_Fox')

background = pygame.image.load('Folder_de_Testes/assets/img/snow_day.jpeg').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# ----- Inicia estruturas de dados
game = True


class Fox(pygame.sprite.Sprite):

    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        
        
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
        self.speedy = 1
        
        self.now_on_windon = 0
    def update(self):
        
        self.rect.y += self.speedy 

        self.speedy += gravity + 0.1 * (-self.speedy)

        self.now_on_windon = (self.now_on_windon + 1) % 3
        self.image = self.images[self.now_on_windon]

                
        # Mantem dentro da tela
        if self.rect.bottom > HEIGHT:
            #pygame.QUIT()
            self.rect.bottom = HEIGHT
            #game = False
        if self.rect.top < 0:
           #pygame.QUIT()
           self.rect.top = 0
            

    def pulo(self):
        
        self.speedy += -18



fox_group = pygame.sprite.Group()
fox = Fox()
fox_group.add(fox)
clock = pygame.time.Clock()

FPS = 30
# ===== Loop principal =====
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_SPACE:
                Fox.pulo(fox)
    # ----- Gera saídas
    window.blit(background, (0,0))

    fox_group.update()
    fox_group.draw(window)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados