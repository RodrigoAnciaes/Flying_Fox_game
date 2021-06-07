

# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME, QUIT
from first_screen import init_screen
#from instructions_screen import instruc_screen
from game_screen import gaming_screen
from death_screen import end_screen

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flying Fox')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    #elif state == TUTO:
        #state = instruc_screen(window)
    elif state == GAME:
        state = gaming_screen(window)
    else:
        state = end_screen(window)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados