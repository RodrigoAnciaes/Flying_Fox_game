# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
WIDTH = 1300
HEIGHT = 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flying Fox')

# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
fundo= pygame.image.load('Folder_de_Testes/assets/img/snow_day.jpeg').convert()
fundo = pygame.transform.scale(fundo, (WIDTH, HEIGHT))
fox = pygame.image.load('Folder_de_Testes/assets/img/Fox.jpeg').convert()
fox = pygame.transform.scale(fox, (80, 80))

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(fundo, (0, 0))
    window.blit(fox, (200, 350))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados