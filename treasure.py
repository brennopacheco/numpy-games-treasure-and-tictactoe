import numpy as np

# Mapa 5x5
mapa = np.random.randint(1, 10, size=(5,5)) 

# Posiciona o tesouro em local aleatório

while True:
    tesouro_linha, tesouro_coluna = np.random.randint(0, 5, size=2)
    if (tesouro_linha, tesouro_coluna) != (0, 0):
        break

posicao_jogador = (0, 0)
pontuacao = 0

def mostrar_mapa(mapa, posicao_jogador):
    mapa_com_jogador = mapa.copy() 
    linha, coluna = posicao_jogador
    mapa_com_jogador[linha, coluna] = -1
    
    # Tenta substituir o -1 por um caractere 'P'
    mapa_com_jogador_str = np.char.mod('%2d', mapa_com_jogador) # Converte a matriz para string
    mapa_com_jogador_str[mapa_com_jogador == '-1'] = 'P'

    print('\nMapa Atual:')
    for linha in mapa_com_jogador_str:
        print(' '.join(linha))


# Fluxo Princial
while True:
    mostrar_mapa(mapa, posicao_jogador)

    direcacao = str(input('Informe a direção que voc6e deseja se mover? (WASD)\n')).strip().upper()

    movimentos = {
        'W':(-1, 0),
        'A':(0, -1),
        'S':(1, 0),
        'D':(0, 1),
    }

    if direcacao in movimentos:
        nova_posicao = (posicao_jogador[0] + movimentos[direcacao][0], posicao_jogador[1] + movimentos[direcacao][1])
    else:
        print('Direção Inválida! Tente novamente.')

    # Verifica se a nova posição é válida.
    if not (0 <= nova_posicao[0] < mapa.shape[0] and 0 <= nova_posicao[1] < mapa.shape[1]):
        print('Movimento fora dos limites! Tente novmante.')
        continue

    posicao_jogador = nova_posicao
    pontuacao += 1

    # Verifica se o jogador encontrou o tesouro
    if posicao_jogador == (tesouro_linha, tesouro_coluna):
        mostrar_mapa(mapa, posicao_jogador)
        print('\n\n========Parabéns!! Você encontrou o tesouro!=========')
        print(f'Pontuação Final: {pontuacao}')
        print(f'O Tesouro estava na posição: {(tesouro_linha+1, tesouro_coluna+1)}')
        break