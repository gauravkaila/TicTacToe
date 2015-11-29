# This is a two player tic tac toe game

import random

board = {'topL':' ','topC':' ','topR':' ','cenL':' ','cenC':' ','cenR':' ','botL':' ',
         'botC':' ','botR':' '}

def printBoard(board):
    print (board['topL'] + '|' + board['topC'] + '|' + board['topR'])
    print ('-----')
    print (board['cenL'] + '|' + board['cenC'] + '|' + board['cenR'])
    print ('-----')
    print (board['botL'] + '|' + board['botC'] + '|' + board['botR'])
    

players = ['X','O']
player = random.choice(players)

for i in range(1,10):
    move = input(str(i) + ' turn. Turn of: ' + player + ' Which location will you play: ')
    
    # check to see if incorrect location is entered    
    if move != 'topL' and move !=  'topC' and move != 'topR' and move != 'cenL' and move !=  'cenC' and move != 'cenR' and move != 'botL' and move !=  'botC' and move != 'botR':
        move = input( 'This is an incorrect location. Please enter a correct location: ')

    # check to see if the location is already filled
    if board[move] != ' ':
        move = input('This location is already filled. Please select an empty location: ')
    
    board[move] = player
    printBoard(board)
    if player == 'X':
        player = 'O'
    elif player == 'O':
        player = 'X'

    if (board['topL'] == 'X' and board['topC'] == 'X' and  board['topR'] == 'X'):
        print 'X' + ' won'
        break
    elif (board['topL'] == 'O' and board['topC'] == 'O' and  board['topR'] == 'O'):
        print 'O' + ' won'
        break
    elif (board['cenL'] == 'X' and board['cenC'] == 'X' and  board['cenR'] == 'X'):
        print 'X' + ' won'
        break
    elif (board['botL'] == 'O' and board['botC'] == 'O' and  board['botR'] == 'O'):
        print 'O' + ' won'
        break
    elif (board['topL'] == 'X' and board['cenL'] == 'X' and board['botL'] == 'X'):
        print 'X' + ' won'
        break
    elif (board['topC'] == 'X' and board['cenC'] == 'X' and board['botC'] == 'X'):
        print 'X' + ' won'
        break
    elif (board['topR'] == 'X' and board['cenR'] == 'X' and board['botR'] == 'X'):
        print 'X' + ' won'
        break
    elif (board['topL'] == 'O' and board['cenL'] == 'O' and board['botL'] == 'O'):
        print 'O' + ' won'
        break
    elif (board['topC'] == 'O' and board['cenC'] == 'O' and board['botC'] == 'O'):
        print 'O' + ' won'
        break
    elif (board['topR'] == 'O' and board['cenR'] == 'O' and board['botR'] == 'O'):
        print 'O' + ' won'
        break
    elif (board['topL'] == 'X' and board['cenC'] == 'X' and board['botR'] == 'X'):
        print 'X' + ' won'
        break
    elif (board['botL'] == 'X' and board['cenC'] == 'X' and board['topR'] == 'X'):
        print 'X' + ' won'
        break
    elif (board['topL'] == 'O' and board['cenC'] == 'O' and board['botR'] == 'O'):
        print 'O' + ' won'
        break
    elif (board['botL'] == 'O' and board['cenC'] == 'O' and board['topR'] == 'O'):
        print 'O' + ' won'
        break

input('Press enter to exit')

