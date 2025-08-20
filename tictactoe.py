import numpy as np

def colocar_peca(tabuleiro, linha, coluna, peca):
    '''
    Coloca a peça do jogador na posição escolhida
    '''

    tabuleiro[linha][coluna] = peca