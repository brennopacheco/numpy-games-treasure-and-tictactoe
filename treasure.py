import numpy as np

# Mapa 5x5
mapa = np.random.randint(1, 10, size=(5,5)) # Gera um mapa 5x5 com valores aleatórios entre 1 e 9

# Posiciona o tesouro em local aleatório

while True:
    tesouro_linha, tesouro_coluna = np.random.randint(0, 5, size=2) # Gera uma posição aleatória para o tesouro
    if (tesouro_linha, tesouro_coluna) != (0, 0): # Garante que o tesouro não esteja na posição inicial do jogador
        break

posicao_jogador = (0, 0) # Posição inicial do jogador
pontuacao = 0 # Pontuação inicial

def mostrar_mapa(mapa, posicao_jogador):
    '''
    Mostra o mapa com a posição do jogador
    '''
    mapa_com_jogador = mapa.copy() # Cria uma cópia do mapa original
    linha, coluna = posicao_jogador # Obtém a posição atual do jogador
    mapa_com_jogador[linha, coluna] = -1 # Marca a posição do jogador com -1
    
    # Tenta substituir o -1 por um caractere 'P'
    mapa_com_jogador_str = np.char.mod('%2d', mapa_com_jogador) # Converte a matriz para string para facilitar a substituição
    mapa_com_jogador_str[mapa_com_jogador == '-1'] = 'P' # Substitui -1 por 'P' para representar o jogador

    print('\nMapa Atual:')
    for linha in mapa_com_jogador_str: # Imprime cada linha do mapa
        print(' '.join(linha)) # Junta os elementos da linha com espaço para melhor visualização


# Fluxo Princial
while True:
    mostrar_mapa(mapa, posicao_jogador) # Mostra o mapa com a posição atual do jogador

    direcacao = str(input('Informe a direção que você deseja se mover? (WASD)\n')).strip().upper() # Solicita a direção do movimento ao jogador

    movimentos = { # Dicionário de movimentos
        'W':(-1, 0),
        'A':(0, -1),
        'S':(1, 0),
        'D':(0, 1),
    }

    if direcacao in movimentos:
        nova_posicao = (posicao_jogador[0] + movimentos[direcacao][0], posicao_jogador[1] + movimentos[direcacao][1]) # Calcula a nova posição do jogador
    else:
        print('Direção Inválida! Tente novamente.')

    # Verifica se a nova posição é válida.
    if not (0 <= nova_posicao[0] < mapa.shape[0] and 0 <= nova_posicao[1] < mapa.shape[1]): 
        print('Movimento fora dos limites! Tente novmante.')
        continue

    posicao_jogador = nova_posicao # Atualiza a posição do jogador
    pontuacao += 1 # Incrementa a pontuação a cada movimento

    # Verifica se o jogador encontrou o tesouro
    if posicao_jogador == (tesouro_linha, tesouro_coluna): # Se a posição do jogador for igual à posição do tesouro
        mostrar_mapa(mapa, posicao_jogador) # Mostra o mapa final com a posição do jogador
        print('\n\n========Parabéns!! Você encontrou o tesouro!=========') 
        print(f'Pontuação Final: {pontuacao}')
        print(f'O Tesouro estava na posição: {(tesouro_linha+1, tesouro_coluna+1)}')
        break