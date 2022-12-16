import pygame
from checkers.constants import WIDTH, HEIGHT, TAMANHO_CASA, BOLDGRAY, WHITE
from checkers.game import Game
from minimax.algorithm import minimax

# FPS é importado diretamente do pygame, da mesma forma que algumas outras funções como WIN, bind, etc... que serão utilizadas no código
FPS = 60

# Window definida na tela do observador
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# Nome da janela
pygame.display.set_caption('Checker with Minimax (Authors: Marco Damo, Vinicius Muller and João Detoni)')

def pegar_posicao_escolhida_mouse(pos):
    x, y = pos
    # Define qual a posição que a peça está (ex: se x=600 e y=450 então 600/75 e 450/75 portanto a posição é A[8,6]) em relação a resolução escolhida
    linhas_ = y // TAMANHO_CASA
    colunas_ = x // TAMANHO_CASA
    return linhas_, colunas_

# Onde o jogo é rodado (codado em módulos)
def main():
    run = True
    
    # Colocar um "clock" faz com que o jogo rode normalmente, impedindo que ocorram eventos onde o jogo rode muito rápido
    # ou muito devagar em partes essenciais do jogo.
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 3, WHITE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False

        # Verifica os eventos de interação com a janela do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Biblioteca do pygame que identifica ações do mouse
                pos = pygame.mouse.get_pos()
                linhas_, colunas_ = pegar_posicao_escolhida_mouse(pos)
                game.select(linhas_, colunas_)

        game.update()
    
    pygame.quit()

main()