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
difficult = 0
count_fox = 0
# ----- Inicia assets
METEOR_WIDTH = 100
METEOR_HEIGHT = random.randint(300, 450)
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('Folder_de_Testes/assets/img/snow_day.jpeg').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
pygame.mixer.music.load('assets/sounds/otaldosom2.ogg')
pygame.mixer.music.set_volume(1.0)

score_font = pygame.font.Font('Folder_de_Testes/assets/img/PressStart2P.ttf', 28)


def randon_sizes_for_walls(xpos):
    protection = 100
    #print(xpos)
    altura = random.randint(0, 400)
    #print(altura)
    wall = Meteor(False, xpos, altura)
    inversal_wall = Meteor(True, xpos,HEIGHT + altura - protection)
    return [wall,  inversal_wall]

# ----- Inicia estruturas de dados
# Definindo os novos tipos
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
        self.flying_one = pygame.image.load('Folder_de_Testes/assets/img/fly_fox.png').convert_alpha()
        self.flying_one = pygame.transform.scale(self.flying_one, (100, 100))

        self.images = [Fox1,Fox2,Fox3]

        self.count_fox = count_fox 
        self.image = Fox1
        self.fly_sound =  pygame.mixer.Sound('Folder_de_Testes/assets/sounds/Efeito sonoro pulo do Mário.mp3') #descobri que arquivos de sound efects tem que ser .wav
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 4
        self.rect.bottom = HEIGHT - 100
        self.speedy = 1
        
        self.now_on_windon = 0

        self.speed_modifier = 0.0

        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 500
        self.last_jump_sound = pygame.time.get_ticks()
        self.sound_ticks = 500

        

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
        if self.rect.bottom > HEIGHT + 18:
        
            self.rect.bottom = HEIGHT + 18
            #self.speedy = 1
            #game = False
        if self.rect.top < 0:
           
           self.rect.top = 0
            

    def pulo(self):

        self.speedy = -16 + self.speed_modifier
        now_sound = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        elapsedsound_ticks = now_sound - self.last_shot

        # Se já pode atirar novamente...
        if elapsedsound_ticks > self.sound_ticks:
            self.last_jump_sound = now_sound
            self.fly_sound.play()

    def Scratch(self):
        # Verifica se pode atirar
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = now - self.last_shot

        # Se já pode atirar novamente...
        if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
            self.last_shot = now
            # A nova bala vai ser criada logo acima e no centro horizontal da nave
            new_scratch = Claw(self.rect.top + 130, self.rect.centerx + 40)
            all_sprites.add(new_scratch)
            all_scratchs.add(new_scratch) 


class Claw(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self,bottom, centerx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        claw_WIDTH = 150
        claw_HEIGHT = 200
        self.image = pygame.image.load('Folder_de_Testes/assets/img/scratch.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (claw_WIDTH, claw_HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = 0  # Velocidade fixa para cima

        self.Scratch_time = 0

    def update(self):
        # A bala só se move no eixo y
        self.rect.y += self.speedy

        self.Scratch_time += 1

        # Se o tiro passar do inicio da tela, morre.
        if self.Scratch_time == 10:
            self.kill()
          
          
        
        

class Meteor(pygame.sprite.Sprite):
    def __init__(self, inversal,posx, posy):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.inversal = inversal
        wall_HEIGHT = 480
        wall_WIDTH = 80
        self.posx = posx
        self.posy = posy
        self.image = pygame.image.load('Folder_de_Testes/assets/img/Tronco1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (wall_WIDTH, wall_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect[0] = posx

        if inversal:

            self.image = pygame.transform.flip(self.image,False, True)
            self.rect[1] = (self.rect[3] - posy)
        else:
            self.rect[1] = HEIGHT - posy

        self.mask = pygame.mask.from_surface(self.image)

        self.speedx = -10

    def update(self):
        
        self.rect[0] += self.speedx
        
            


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
            self.rect.y = self.rect.y = random.randint(10, 600)
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
        self.rect.y = random.randint(10, 600)
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
            self.rect.y = random.randint(10, 600)
            self.speedx = random.randint(-5, -3)
            
score = 0
score_coin = 0
score_kills = 0
game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

# Criando um grupo de meteoros
all_sprites = pygame.sprite.Group()
all_meteors = pygame.sprite.Group()
all_coins =   pygame.sprite.Group()
all_predators = pygame.sprite.Group()
all_scratchs = pygame.sprite.Group()
# Criando o jogador
player = Fox()
all_sprites.add(player)
# Criando os meteoros
for i in range(1):
    meteor = randon_sizes_for_walls(WIDTH * i + 800)
    all_meteors.add(meteor[0])
    all_meteors.add(meteor[1])


coin = Coin()
all_coins.add(coin)
all_sprites.add(coin)


predator = Predator()
all_predators.add(predator)
all_sprites.add(predator)
added = True

# ===== Loop principal =====
while game:
    
    meteorite = meteor[0]
    in_meteor = meteor[1]

    if meteorite.rect.right < 0 or meteorite.rect.left > WIDTH:
        meteorite.kill()
        meteor = randon_sizes_for_walls(WIDTH * 0 + 800)
        #print(i)
        all_meteors.add(meteor[0])
        all_meteors.add(meteor[1])

    fpdif = FPS + difficult
  
    

    if fpdif > 40 and added == True:
        #print(added)
        
        predator = Predator()
        all_predators.add(predator)
        all_sprites.add(predator)
        added = False




    
    #print(fpdif)
    clock.tick(fpdif)
    #print(clock)
    difficult += 0.01

    if fpdif > 68:
        fpdif = 68

    #print(int(fpdif))

    score = int(difficult) + score_coin + score_kills

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
            if event.key == pygame.K_0:
                player.Scratch()
            

    # ----- Atualiza estado do jogo
    # Atualizando a posição dos meteoros
    all_sprites.update()
    all_meteors.update()



    hits_pred = pygame.sprite.groupcollide(all_predators, all_scratchs, True, False, pygame.sprite.collide_mask)
    for predator in hits_pred: # As chaves são os elementos do primeiro grupo (meteoros) que colidiram com alguma bala
                # O meteoro e destruido e precisa ser recriado
            
        predator = Predator()
        all_sprites.add(predator)
        all_predators.add(predator)
        
        

                # No lugar do meteoro antigo, adicionar uma explosão.
            
                # Ganhou pontos!
        score_kills += 50

    
    
    hits = pygame.sprite.spritecollide(player,all_meteors,True, pygame.sprite.collide_mask)
    if len(hits) > 0:
        game = False
    hits = pygame.sprite.spritecollide(player,all_predators,True, pygame.sprite.collide_mask)
    if len(hits) > 0:
        game = False
    
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
    all_meteors.draw(window)

    text_surface = score_font.render("{:08d}".format(score), True, (255, 255, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (WIDTH / 2,  10)
    window.blit(text_surface, text_rect)

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados