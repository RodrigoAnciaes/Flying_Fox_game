
import pygame
import random
WIDTH = 880
HEIGHT = 660

pygame.init()
pygame.mixer.init()

# Função para gerar os tamanhos e depois posicionamentos aleátorios dos troncos/barreiras
def randon_sizes_for_walls(xpos):
    protection = 100
    #print(xpos)
    altura = random.randint(0, 400)
    #print(altura)
    wall = Meteor(False, xpos, altura)
    inversal_wall = Meteor(True, xpos,HEIGHT + altura - protection)
    return [wall,  inversal_wall]

#----------------------------------------------------------------------------------------------------------------------------------

# ----- Inicia estruturas de dados
# Definindo os novos tipos de classes que existirão
class Fox(pygame.sprite.Sprite):
    
    def __init__(self):
        
        #================== define os parametros base ==============================
        pygame.sprite.Sprite.__init__(self)
        count_fox = 0
        Fox_WIDTH = 170
        Fox_HEIGHT = 100
        self.gravity = 1
        Fox1 = pygame.image.load('Flying_Fox_Game/assets/img/raposa 1.png').convert_alpha()
        Fox1 = pygame.transform.scale(Fox1, (Fox_WIDTH, Fox_HEIGHT))
        Fox2 = pygame.image.load('Flying_Fox_Game/assets/img/raposa2.png').convert_alpha()
        Fox2 = pygame.transform.scale(Fox2, (Fox_WIDTH, Fox_HEIGHT))
        Fox3 = pygame.image.load('Flying_Fox_Game/assets/img/raposa 3.png').convert_alpha()
        Fox3 = pygame.transform.scale(Fox3, (Fox_WIDTH, Fox_HEIGHT))
        self.flying_one = pygame.image.load('Flying_Fox_Game/assets/img/raposa_voando.png').convert_alpha()
        self.flying_one = pygame.transform.scale(self.flying_one, (Fox_WIDTH, Fox_HEIGHT + 50))

        self.images = [Fox1,Fox2,Fox3] # coloca as imagens dentro de uma lista para serem utilizadas na animação

        self.count_fox = count_fox  # Parametro da animação
        self.image = Fox1
        self.fly_sound =  pygame.mixer.Sound('Flying_Fox_Game/assets/sounds/Efeito sonoro pulo do Mário.mp3') # define o som do pulo
        self.cut_sound =  pygame.mixer.Sound('Flying_Fox_Game/assets/sounds/cut.mp3') # define o som do ataque
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 4 # posicionam a imagem e definem a velocidade de quda inicial
        self.rect.bottom = HEIGHT
        self.speedy = 1
        

        # Define parâmetros de calibragem essencias para a animação, pulo, velocidade
        self.now_on_windon = 0 

        self.speed_modifier = 0.0

        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 500

        self.ultimopulo = 500


    def update(self):
        
        self.rect.y += self.speedy 

        self.speedy += self.gravity + 0.1 * (-self.speedy) #aumenta a velocidade conforme a gravidade

        
        self.mask = pygame.mask.from_surface(self.image) #forma a máscara da imagem

        self.count_fox += 1

        #print(self.speed_modifier)

        if self.speed_modifier > -12:      # Esses parametros foram criados para regular o aumento excessivo da velocidade de queda conformde o aumento da velocidade
            self.speed_modifier -= 0.0024



        #==================Executa a animação do andar da raposa
        if self.count_fox >= 10 and  self.rect.bottom > HEIGHT:

            self.now_on_windon = (self.now_on_windon + 1) % 3
            self.image = self.images[self.now_on_windon]
            self.count_fox = 0
        # Animação do pulo
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
            

    def pulo(self):  # Faz a raposa pular se dentro de certo periodo de 'recarga'
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.ultimopulo
        if elapsed_ticks > 100:

            self.speedy = -16 + self.speed_modifier
            self.fly_sound.play()
            self.ultimopulo = now
        

    def Scratch(self): # Define o ataque da raposa
        # Verifica se pode atacar
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último ataque.
        elapsed_ticks = now - self.last_shot

        # Se já pode atacar novamente...
        if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
            self.last_shot = now
            # A novo arranhão vai ser criado logo acima e no centro horizontal e um pouco a direita da raposa
            new_scratch = Claw(self.rect.top + 130, self.rect.centerx + 60)

            self.cut_sound.play()
            
            return new_scratch
            #all_sprites.add(new_scratch)
            #all_scratchs.add(new_scratch) 
            

#-----------------------------------------------------------------------------------------------------------------------------------
class Claw(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self,bottom, centerx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        claw_WIDTH = 150
        claw_HEIGHT = 200
        self.image = pygame.image.load('Flying_Fox_Game/assets/img/scratch.png').convert_alpha()
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
          
          
#----------------------------------------------------------------------------------------------------------------------------------        
        

class Meteor(pygame.sprite.Sprite): #Classe responsável pelas barreiras/tronco
    def __init__(self, inversal,posx, posy):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.inversal = inversal
        wall_HEIGHT = 480
        wall_WIDTH = 80
        self.posx = posx
        self.posy = posy
        self.image = pygame.image.load('Flying_Fox_Game/assets/img/Tronco1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (wall_WIDTH, wall_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect[0] = posx

        if inversal: # Verica se a barreira/tronco será ou não ivertida

            self.image = pygame.transform.flip(self.image,False, True)
            self.rect[1] = (self.rect[3] - posy)
        else:
            self.rect[1] = HEIGHT - posy

        self.mask = pygame.mask.from_surface(self.image) # Define a marcara da barreira/tronco

        self.speedx = -10 # Velocidade de movimento horizontal da barreira/tronco

    def update(self):
        
        self.rect[0] += self.speedx # Atualiza a posição da barreira/tronco
        
            
#--------------------------------------------------------------------------------------------------------------------------------------

class Coin(pygame.sprite.Sprite): #Classe das moedas de pontuação
    def __init__(self):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        coin_HEIGHT = 50
        coin_WIDTH = 50
        self.image = pygame.image.load('Flying_Fox_Game/assets/img/coin.png').convert_alpha()
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

#---------------------------------------------------------------------------------------------------------------------------------------

class Predator(pygame.sprite.Sprite): #Constroi a piranha, o terrivel predador da raposa voadora
    def __init__(self):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        coin_HEIGHT = 50
        coin_WIDTH = 50
        Piranha = pygame.image.load('Flying_Fox_Game/assets/img/piranha.png').convert_alpha()
        Piranha = pygame.transform.scale(Piranha, (coin_WIDTH, coin_HEIGHT))
        Piranha2 = pygame.image.load('Flying_Fox_Game/assets/img/piranha3.png').convert_alpha()
        Piranha2 = pygame.transform.scale(Piranha2, (coin_WIDTH, coin_HEIGHT))
        self.images = [Piranha, Piranha2] # Coloca as imagens dentro de uma lista para serem utilizadas na animação
        self.image = Piranha
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = (WIDTH-coin_WIDTH)
        self.rect.y = random.randint(10, 600)
        self.speedx = random.randint(-5, -3)
        METEOR_HEIGHT = random.randint(50, 250)
        self.count_anim = 0
        self.counter = 0
        
        

    def update(self):
        # Atualizando a posição do meteoro
        if self.counter == 10: #se dentro do certo periodo -> executa a animação de abrir e fechar a boca
            self.image = self.images[(self.count_anim % 2)]
            self.mask = pygame.mask.from_surface(self.image)
            self.count_anim += 1
            self.counter = 0
        self.counter += 1
        METEOR_HEIGHT = random.randint(50, 250)
        self.rect.x += self.speedx
        coin_WIDTH = 50
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = (WIDTH-coin_WIDTH)
            self.rect.y = random.randint(10, 600)
            self.speedx = random.randint(-5, -3)



# Criando os grupo de sprites
all_sprites = pygame.sprite.Group()
all_meteors = pygame.sprite.Group()
all_coins =   pygame.sprite.Group()
all_predators = pygame.sprite.Group()
all_scratchs = pygame.sprite.Group()
# Criando o jogador
player = Fox()
all_sprites.add(player)
# Criando as barreiras/troncos
for i in range(1):
    meteor = randon_sizes_for_walls(WIDTH * i + 800)
    all_meteors.add(meteor[0])
    all_meteors.add(meteor[1])

#Cria as moedas
coin = Coin()
all_coins.add(coin)
all_sprites.add(coin)

#Crias os predadores
predator = Predator()
all_predators.add(predator)
all_sprites.add(predator)
added = True
