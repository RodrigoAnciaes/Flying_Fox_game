# Flying_Fox_game
- Repositório criado para um projeto de design de software, onde devíamos projetar um jogo utilizando-se do pygame, culminando assim, na ideia do jogo Flying_Fox. Nosso jogo é baseado no clássico "Flappy Bird", onde o jogador precisa direcionar a raposa para que a mesma desvie dos obstáculos (no caso as árvores) e permaneça no ar o maior tempo possível. Para desviar das arvores que vem cada vez mais rápido em sua direção, o jogado utiliza a tecla "SPACE" para movimentar e fazer com que a "flying fox" se mantenha em um voo acrobático, fazendo um trajeto sem colisões. Com o tempo a velocidade aumenta e consequentemente a dificuldade, até que haja uma falha do jogador, fazendo com que a raposa colida com alguma árvore. Neste último cenário, a usuário é redirecionado a tela inicial e escolhe se quer jogar novamente.

-Vale ressaltar que as imagens utilizadas foram criadas pelo programa "paint", sendo todas autênticas de nosso trabalho.

# Desenvolvido em conjunto por:
- Rodrigo Anciães Patelli
- Guido Rosa
- Enzo Cunha

# Instalando o pygame e rodando o jogo:
- Para que seja possível rodar o jogo, é necessária a instalação do pygame no seu dispositivo. Para isso, o caminho mais fácil é utilizar a ferramenta "pip" e a bandeira "user", instalando dentro de um diretório local, e não global.

- Logo, basta colar "python3 -m pip install -U pygame --user" no terminal do seu dispositivo, clicar "enter" e o download é concluído.

- Para finalmente rodar o jogo, é necessário que se clone o repositório desse github, abrindo em algum programa que rode a linguagem "phyton", como o Visual Studio Code.
- Ao final, basta clicar no "play" do código "versao_final.py", localizado na pasta Flying_Fox_Game, que você será direcionado para a tela do pygame.

# Jogando o jogo:
- o jogo apesar de ser 100% inspirado no famoso jogo Flappy bird tem algumas diferenças fundamentais que serão apresentadas.

- Comandos base:

- 'Space_Bar' é a função de pular, simples e sem muitas novidades, aperte e solte o botão para pular para cima e deixe a gravidade te puxar de volta depois ou não, ppois você pode pular quantas vezes quizer, sem medo de bater no teto ou cai no chão, mas sempre evitando acertar os troncos.


# Pontuação:

- Falando em funções novas, aperte '0' para fazer um ataque de garra e acabar com as piranhas que venham te atacar, Obs. Não deixe as piranhas acertarem você.

- Falando em pontos, você pode ganahar pontos de diversas maneiras:

- Sobrevivendo por um periodo de tempo, a pontuação pr tempo fica mais rápida assim como os troncos, piranhas e moedas conforme o tempo passa.

- Coletando moedas.

- Matando as piranhas antes que elas acertem você.

# No fim de tudo:

- não fique triste se você for atingido na cabeça por um troco ou comido por uma piranha, apenas recomece o jogo e tente alcançar a maior pontuação possível novamente!

# Referencias:

- Agradeço ao canal do Youtube: Programador Sagaz, por nos explicar e mostrar em seu vídeo partes nescessárias para o funcionamento do código de geração de troncos/ barreiras aleátórias, que está incluso na classe Meteor e na finção get_randon_sizes_for_walls que construimos no código.
- segue o link para o vpideo onde a função foi apresentada: https://www.youtube.com/watch?v=WbmHcbcSwnA&list=WL&index=139