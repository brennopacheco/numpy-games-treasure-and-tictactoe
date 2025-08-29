import numpy as np

def colocar_peca(tabuleiro, linha, coluna, peca):
    '''
    Coloca a peça do jogador na posição escolhida
    '''
    tabuleiro[linha][coluna] = peca # Coloca a peça na posição escolhida


def verificar_vitoria(tabuleiro, peca):
    '''
    Verifica se o jogador ganhou a partida
    '''
    linha = np.any(np.all(tabuleiro == peca, axis=1)) # Verifica se alguma linha tem todas as posições iguais à peça do jogador
    coluna =np.any(np.all(tabuleiro == peca, axis=0)) # Verifica se alguma coluna tem todas as posições iguais à peça do jogador
    diagonais = np.all(np.diag(tabuleiro) == peca) or np.all(np.diag(np.fliplr(tabuleiro)) == peca) # Verifica as diagonais
    
    return linha or coluna or diagonais # Retorna True se o jogador ganhou, caso contrário retorna False

def imprimir_tabuleiro(tabuleiro):
    '''
    Imprime o tabuleiro na tela
    '''
    for linha in tabuleiro:
        print(' | '.join(str(x) if x != 0 else ' ' for x in linha)) # Substitui 0 por espaço em branco para melhor visualização
        print('-' * 8) # Imprime uma linha separadora

def jogo():
    '''
    Função principal do jogo da velha
    '''
    tabuleiro = np.zeros((3,3), dtype=int) # Cria um tabuleiro 3x3 vazio

    peca_atual = 1 # Começa com a peça 1 (X)
    vencedor = False
    empate = False

    while not vencedor and not empate:
        imprimir_tabuleiro(tabuleiro) # Imprime o tabuleiro atual

        while True:
            try:
                linha = int(input(f'Jogador {peca_atual}, escolha a linha (0, 1, 2): ')) # Solicita a linha ao jogador
                coluna = int(input(f'Jogador {peca_atual}, escolha a coluna (0, 1, 2): ')) # Solicita a coluna ao jogador

                # Verifica se a linha e coluna são válidas
                if linha not in [0,1,2] or coluna not in [0,1,2]: # Se a linha ou coluna não estiverem entre 0 e 2
                    print('\nEscolha linhas e colunas válidas! De 0 a 2\n')


                # Verifica se a posição já está ocupada
                if tabuleiro[linha][coluna] != 0: # Se a posição não for 0, está ocupada
                    print('\nPosição já ocupada! Tente novamente.\n')
                    continue

                colocar_peca(tabuleiro, linha, coluna, peca_atual) # Coloca a peça na posição escolhida
                vencedor = verificar_vitoria(tabuleiro, peca_atual) # Verifica se o jogador ganhou

                # Se houver empate
                if np.all(tabuleiro != 0):
                    empate = True

                break

            except ValueError:
                print('\nEntrada inválida! Por favor insira núumeros de 0 a 2.\n')
        
        # Troca o jogador
        if not vencedor and not empate:
            peca_atual = 2 if peca_atual == 1 else 1 # Alterna entre jogador 1 e 2

    imprimir_tabuleiro(tabuleiro) # Imprime o tabuleiro final

    if vencedor:
        print(f'\n\nParabéns! Jogador {peca_atual} venceu!')
    else:
        print('\n\nEmpate! Ninguém venceu.')


jogo()