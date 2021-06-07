import pygame
import random
WIDTH = 880
HEIGHT = 660
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
background = pygame.image.load('Flying_Fox_Game/assets/img/tela de inicio final.png').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background_rect = background.get_rect()

running = True
while running:

        # Ajusta a velocidade do jogo.
    clock.tick(60)

        # Processa os eventos (mouse, teclado, botão, etc).
    for event in pygame.event.get():
            # Verifica se foi fechado.
        if event.type == pygame.QUIT:
            state = False
            running = False

        if event.type == pygame.KEYUP:
            state = False
            running = False

        # A cada loop, redesenha o fundo e os sprites
        #screen.fill(BLACK)
    screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
    pygame.display.flip()


