# A game of Tic Tac Toe

import random

# values on the baord
board = {"top_L":' ', 'top_M':' ', 'top_R':' ',
         'mid_L':' ', 'mid_M':' ', 'mid_R':' ',
         'low_L':' ', 'low_M':' ', 'low_R':' '}

# create the board
def print_board(board):
    print(board["top_L"] + '|' + board['top_M'] + '|' + board['top_R'])
    print("-+-+-")
    print(board["mid_L"] + '|' + board['mid_M'] + '|' + board['mid_R'])
    print("-+-+-")
    print(board["low_L"] + '|' + board['low_M'] + '|' + board['low_R'])

def player_choice():
    turn = input("\n Select 'X' to go first and 'O' to go second:")
    if turn == "X":
        print("\n You have chosen X, player will go first.")
        playing_game(turn)
    else:
        print("\n You have chosen O, computer will fo first.")


def playing_game(turn):
    for i in range(9):
        print("\nTurn for " + turn + ", move on which place?\n")
        move = input()
        if board[move] != " ":
            print("You cannot play on this location, choose another location.")
            continue
        board[move] = turn

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    print_board(board)

def new_game():
    print("\nNew Game\n")

    print_board(board)
    player_choice()
new_game()
