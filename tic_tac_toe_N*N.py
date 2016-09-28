#!/usr/bin/python
''' ---------------------- Tic Tac Toe Game ----------- #
# Author : Shanshan zhang
# Date   : 27/09/2016
# Email  : xiangxiangster@hotmail.com
# ------------------------------------------------------------
'''

import sys

'''
# init the value
'''

game_over = False

'''
# Check the game is finished or not (who is win or draw)
# Also check with player want to continue or exit
''' 
    
    
def check_if_finished(x, y, matrix):
    status = False
    status_game_over = False

    # angle-direction:
    if y >= 2 and x <= matrix -3:
        if chess_tab[y][x] == chess_tab[y-1][x+1] == chess_tab[y-2][x+2]:
            status = True   
    
    if y >= 1 and x>=1 and x <= matrix -2 and y <= matrix -2: 
        if chess_tab[y][x] ==  chess_tab[y-1][x+1]  == chess_tab[y+1][x-1]:
            status = True   
        
    if x >= 2 and y <= matrix -3: 
        if chess_tab[y][x] == chess_tab[y+2][x-2] == chess_tab[y+1][x-1]:
            status = True   

    # di-angle-direction:
    if y >= 2 and x >= 2:
        if chess_tab[y][x] == chess_tab[y-1][x-1] == chess_tab[y-2][x-2]:
            status = True   
    
    if y >= 1 and x>=1 and x <= matrix -2 and y <= matrix -2: 
        if chess_tab[y][x] ==  chess_tab[y+1][x+1]  == chess_tab[y-1][x-1]:
            status = True   
        
    if x <= matrix -3 and y <= matrix -3: 
        if chess_tab[y][x] == chess_tab[y+2][x+2] == chess_tab[y+1][x+1]:
            status = True 
            
    # x-direction:
    if y>=2:
        if chess_tab[y][x] == chess_tab[y-1][x] == chess_tab[y-2][x]:
            status = True   
    
    if y>=1 and y<= matrix - 2:
        if chess_tab[y+1][x] == chess_tab[y-1][x] == chess_tab[y][x]:
            status = True   
    
    if y<= matrix - 3:
        if chess_tab[y+1][x] == chess_tab[y+2][x] == chess_tab[y][x]:
            status = True   
    
    # y-direction:
    if x>=2:
        if chess_tab[y][x] == chess_tab[y][x-1] == chess_tab[y][x-2]:
            status = True   
    
    if x>=1 and x<= matrix - 2:
        if chess_tab[y][x+1] == chess_tab[y][x-1] == chess_tab[y][x]:
            status = True   
    
    if x <= matrix - 3:
        if chess_tab[y][x+1] == chess_tab[y][x+2] == chess_tab[y][x]:
            status = True   
    
    if status:
        print ('******************************************')
        if chess_tab[y][x] == 'X':
            print ('Congratulations {}! You have won'.format(player1))
        else:
            print ('Congratulations {}! You have won'.format(player2))
        print ('******************************************')
                        
    if status == False:
        for i in range (matrix):
            for j in range (matrix):
                if chess_tab[i][j] != 'X' and chess_tab[i][j] != 'O':
                    return status, status_game_over
        print ('******************************************')
        print('this round Draw')
        print ('******************************************')        
        status = True   
        
    if status:
        print '\r'
        rtn = raw_input('Do u want play again?[y/n]:')
        if rtn == 'y':
            status_game_over = False            
        elif rtn == 'n':
            status_game_over = True            
        else:
            status_game_over = True
    
    return status, status_game_over
    
'''
# Show the current chess for each round
'''
def show_chess(matrix):
    for i in range(matrix):
        for j in range(matrix):
            print chess_tab[matrix-1-i][j],
            if j != matrix - 1:
                print '|',
        print ''
        for k in range(matrix):
            print'----', 
        print ''
        
        
'''
# Main solution
''' 
player1 = raw_input('Enter name of player 1:')
player2 = raw_input('Enter name of player 2:')
try:
    matrix = int(input('Enter the matrix you want play(>=3):'))
except:
    print('Please entry the number!')
    print 'Bye'
    sys.exit()
    
    
while not game_over:
    player = 'X'
    player_name = player1
    one_round_finished = False
    key = 1
    chess_tab = [[0 for x in range(matrix)] for y in range(matrix)] 
    for i in range (matrix):
        for j in range (matrix):
            chess_tab[i][j] = key
            key = key+1
     
    while not one_round_finished:
        show_chess(matrix)
        shifted = False
        while not shifted:
            try:
                print ('{}, choose a box to place an {} into:'.format(player_name, player))
                location = input('>>')
                if location <= matrix*matrix and location > 0:
                    horiz = location%matrix
                    vert = location/matrix
                    if horiz == 0:
                        horiz = matrix-1
                        vert -=1
                    else:
                        horiz -=1
                                             
                    if chess_tab[vert][horiz] != 'X' and chess_tab[vert][horiz] != 'O':
                        chess_tab[vert][horiz] = player
                        shifted = True    
                        one_round_finished, game_over = check_if_finished(horiz,vert,  matrix)

                        if one_round_finished == False:
                            if player == 'X':
                                player_name = player2
                                player = 'O'
                            else:
                                player_name = player1
                                player = 'X'
                    else:
                        print('Please choose another place, this is already accupied')                    
                else:
                    print('Please enter the correct value [1-{}]'.format(matrix*matrix))
            except KeyboardInterrupt:
                print '\r'
                print 'Bye'
                sys.exit()
            except:
                print('Please enter the correct value [1-{}]'.format(matrix*matrix))
                print '\r'
                
                
