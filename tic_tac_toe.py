# A game of Tic Tac Toe

import random

# values on the baord
board = {"top-L":' ', 'top-M':' ', 'top-R':' ',
         'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
         'low-L':' ', 'low-M':' ', 'low-R':' '}


keys = [key for key in board]

# create the board
def print_board(board):
    print(board["top-L"] + '|' + board['top-M'] + '|' + board['top-R'])
    print("-+-+-")
    print(board["mid-L"] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print("-+-+-")
    print(board["low-L"] + '|' + board['low-M'] + '|' + board['low-R'])

def player_choice():
#    turn = input("\n Select 'X' to go first and 'O' to go second:")
#    if turn == "X":
#        print("\n You have chosen 'X', player will go first.")
#        player_game(turn)
#    else:
#        print("\n You have chosen 'O', computer will fo first.")
#        turn = 'X'
#        computer_game(turn)
    turn = 'X'
    print("Player will go first with 'X'")
    player_game(turn)


def computer_game(turn):

    for i in range(9):

        move = random.choice(keys)

        if board[move] != " " and board[move]:
            continue
        else:
            break

    board[move] = turn
    print_board(board) 

    if turn == 'O':
        turn = 'X'
        player_game(turn)
    else:
        player_game(turn)
        turn = 'O'


def player_game(turn):

    for i in range(9):

        if turn == "X":
            print("\nTurn for " + turn + ", move on which place?")
            move = input()

            if board[move] != " " and board[move]:
                print("You cannot play on this location, choose another location.")
                continue
            else:
                break
    board[move] = turn


    if turn == 'X':
        turn = 'O'
        computer_game(turn)
    else:
        computer_game(turn)
        turn = 'X'
    print_board(board)

def win_check(board):
    pass
    

def new_game():
    print("\nNew Game\n")

    print_board(board)
    player_choice()
new_game()
