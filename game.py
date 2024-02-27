import pygame
import time
from sys import exit
import tictactoe as ttt

pygame.init()
pygame.display.set_caption('Tic-tac-toe')
screen = pygame.display.set_mode((500, 600))
large_font = pygame.font.Font('OpenSans-Regular.ttf', 60)
medium_font = pygame.font.Font('OpenSans-Regular.ttf', 30)

user = None
board = ttt.initial_state()
AI_turn = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill('Black')

    #player choice
    if user == None:

        title = large_font.render('Tic-tac-toe', True, 'White')
        title_rect = title.get_rect(center=(250, 100))
        screen.blit(title, title_rect)

        playerX_button = pygame.Rect(175, 250, 150, 50)
        playerX = medium_font.render('Play as X', True, 'Black')
        playerX_rect = playerX.get_rect(center=(250, 275))
        pygame.draw.rect(screen, 'White', playerX_button)
        screen.blit(playerX, playerX_rect)

        playerO_button = pygame.Rect(175, 350, 150, 50)
        playerO = medium_font.render('Play as O', True, 'Black')
        playerO_rect = playerX.get_rect(center=(250, 375))
        pygame.draw.rect(screen, 'White', playerO_button)
        screen.blit(playerO, playerO_rect)

        click, _, _ = pygame.mouse.get_pressed()
        if click:
            mouse = pygame.mouse.get_pos()
            if playerX_rect.collidepoint(mouse):
                time.sleep(0.2)
                user = ttt.X
            if playerO_rect.collidepoint(mouse):
                time.sleep(0.2)
                user = ttt.O

    else:

    #Draw a board
        grid = []
        for i in range(3):
            row = []
            for j in range(3):
                rect = pygame.Rect(
                    100 + 100 * i, 
                    150 + 100 * j, 
                    100, 100)
                pygame.draw.rect(screen, 'White', rect, 3)
                row.append(rect)
            grid.append(row)

        for i, row in enumerate(grid):
            for j, rect in enumerate(row):
                if board[i][j] != ttt.EMPTY:
                    move = large_font.render(board[i][j], True, 'White')
                    move_rect = move.get_rect(center=(rect[0]+50, rect[1]+50))
                    screen.blit(move, move_rect)


        game_over = ttt.terminal(board)
        player = ttt.player(board)

    # Draw title
        if game_over:
            winner = ttt.winner(board)
            if winner != None:
                title = f'{winner} wins.'
            else:
                title = 'Game over. Tie.'
    
        elif user == player:
            title = 'Your turn...'

        else:
            title = 'Wait for computer move...'

        title = medium_font.render(title, True, 'White')
        title_rect = title.get_rect(center=(250, 100))
        screen.blit(title, title_rect)    

    #Game over
        if game_over:
            again_button = pygame.Rect(175, 500, 150, 50)
            again = medium_font.render('Play again', True, 'Black')
            again_rect = playerX.get_rect(center=(240, 525))
            pygame.draw.rect(screen, 'White', again_button)
            screen.blit(again, again_rect)

            click, _, _ = pygame.mouse.get_pressed()
            if click:
                mouse = pygame.mouse.get_pos()
                if again_rect.collidepoint(mouse):
                    board = ttt.initial_state()
                    AI_turn = False
                    user = None    

    #User move
        click, _, _ = pygame.mouse.get_pressed()
        if click and user == player and not game_over:
            mouse = pygame.mouse.get_pos()
            for i, row in enumerate(grid):
                for j, rect in enumerate(row):
                    if rect.collidepoint(mouse) and board[i][j] == ttt.EMPTY:
                        board = ttt.result(board, (i, j))

    # AI move
        if user != player and not game_over:
            if AI_turn == True:
                time.sleep(0.5)
                v, move = ttt.minimax(board)
                board = ttt.result(board, move)
                AI_turn = False
            else:
                AI_turn = True

    pygame.display.flip()
