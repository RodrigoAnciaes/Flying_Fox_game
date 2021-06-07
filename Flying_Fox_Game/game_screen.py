def game_screen(window):
        # ===== Inicialização =====
    # ----- Importa e inicia pacotes
    import pygame
    import random

    pygame.init()
    pygame.mixer.init()
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
    background = pygame.image.load('Flying_Fox_Game/assets/img/snow_day.jpeg').convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    coin_sound =  pygame.mixer.Sound('Flying_Fox_Game/assets/sounds/super-mario-coin-sound.mp3')
    pygame.mixer.music.load('Flying_Fox_Game/assets/sounds/otaldosom.mp3')
    pygame.mixer.music.set_volume(10000000.0)
    pygame.mixer.music.play(loops=-1)


    score_font = pygame.font.Font('Flying_Fox_Game/assets/img/PressStart2P.ttf', 28)

    #----------------------------------------------------------------------------------------------------------------------------
    

   

    # ----- Inicia estruturas de dados
    # Definindo os novos tipos
    

    #---------------------------------------------------------------------------------------------------------------------------------------

    #                                  definindo parametros e grupos que serão utilizados
    score = 0
    score_coin = 0
    score_kills = 0
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

        # utilizando do loop para fazer com que toda vez que a barreira voltasse para o começo ela fosse diferente
        meteorite = meteor[0]
        in_meteor = meteor[1]

        if meteorite.rect.right < 0 or meteorite.rect.left > WIDTH:
            meteorite.kill()
            meteor = randon_sizes_for_walls(WIDTH * 0 + 800)
            #print(i)
            all_meteors.add(meteor[0])
            all_meteors.add(meteor[1])

        fpdif = FPS + difficult

        #================================== adiciona um novo predador após certo tempo ============================================


        if fpdif > 40 and added == True:
            #print(added)

            predator = Predator()
            all_predators.add(predator)
            all_sprites.add(predator)
            added = False



    #========================================= modifica a dificuldade/velocidade com o tempo =============================================

        #print(fpdif)
        clock.tick(fpdif)
        #print(clock)
        difficult += 0.01

        if fpdif > 68:
            fpdif = 68

        #print(int(fpdif))

        score = int(difficult) + score_coin + score_kills



        #================================================= Trata eventos =================================================================
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

        #====================================== Colisão da função de ataque e adiciona pontos =======================================================

        hits_pred = pygame.sprite.groupcollide(all_predators, all_scratchs, True, False, pygame.sprite.collide_mask)
        for predator in hits_pred: # As chaves são os elementos do primeiro grupo (meteoros) que colidiram com alguma bala
                    # O meteoro e destruido e precisa ser recriado

            predator = Predator()
            all_sprites.add(predator)
            all_predators.add(predator)



                    # No lugar do meteoro antigo, adicionar uma explosão.

                    # Ganhou pontos!
            score_kills += 50

        #================================================ define as colisões letais =====================================================

        hits = pygame.sprite.spritecollide(player,all_meteors,True, pygame.sprite.collide_mask)
        if len(hits) > 0:
            game = False
        hits = pygame.sprite.spritecollide(player,all_predators,True, pygame.sprite.collide_mask)
        if len(hits) > 0:
            game = False

    #============================================ define as colisãoes com as moedas que dão pontos =========================================

        colect_coin = pygame.sprite.spritecollide(player,all_coins,True, pygame.sprite.collide_mask)

        for coin in colect_coin:
            coin_sound.play()
            score_coin += 10
            c = Coin()
            all_coins.add(c)
            all_sprites.add(c)



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
