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
    for linha in mapa_com_jogador:
        print(' '.join(linha))


# Fluxo Princial