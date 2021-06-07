
import pygame
import random
WIDTH = 880
HEIGHT = 660
Fox_WIDTH = 170
Fox_HEIGHT = 100
claw_WIDTH = 150
claw_HEIGHT = 200
wall_HEIGHT = 480
wall_WIDTH = 80
coin_HEIGHT = 50
coin_WIDTH = 50

def load_assets():
    assets = {}
    assets['Fox1'] = pygame.image.load('Flying_Fox_Game/assets/img/raposa 1.png').convert_alpha()
    assets['Fox1'] = pygame.transform.scale(assets['Fox1'], (Fox_WIDTH, Fox_HEIGHT))
    assets['Fox2'] = pygame.image.load('Flying_Fox_Game/assets/img/raposa2.png').convert_alpha()
    assets['Fox2'] = pygame.transform.scale(assets['Fox2'], (Fox_WIDTH, Fox_HEIGHT))
    assets['Fox3'] = pygame.image.load('Flying_Fox_Game/assets/img/raposa 3.png').convert_alpha()
    assets['Fox3'] = pygame.transform.scale(assets['Fox3'], (Fox_WIDTH, Fox_HEIGHT))
    assets['flying_one'] =  pygame.image.load('Flying_Fox_Game/assets/img/raposa_voando.png').convert_alpha()
    assets['flying_one'] = pygame.transform.scale(assets['flying_one'], (Fox_WIDTH, Fox_HEIGHT + 50))
    assets['Claw_img'] = pygame.image.load('Flying_Fox_Game/assets/img/scratch.png').convert_alpha()
    assets['Claw_img']  = pygame.transform.scale(assets['Claw_img'], (claw_WIDTH, claw_HEIGHT))
    assets['Tronco'] = pygame.image.load('Flying_Fox_Game/assets/img/Tronco1.png').convert_alpha()
    assets['Tronco'] = pygame.transform.scale(assets['Tronco'], (wall_WIDTH, wall_HEIGHT))
    assets['Coin'] = pygame.image.load('Flying_Fox_Game/assets/img/coin.png').convert_alpha()
    assets['Coin'] = pygame.transform.scale(assets['Coin'], (coin_WIDTH, coin_HEIGHT))
    assets['Predator'] = pygame.image.load('Flying_Fox_Game/assets/img/piranha.png').convert_alpha()
    assets['Predator'] = pygame.transform.scale(assets['Predator'], (coin_WIDTH, coin_HEIGHT))
    return assets