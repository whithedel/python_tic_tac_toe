#Miltiplayer Tic-tac-toe game
import random

turn = ' '
player1 = ''
player2 = ''
gameOn = True

# m = {
#         1:' ',
#         2:' ',
#         3:' ',
#         4:' ',
#         5:' ',
#         6:' ',
#         7:' ',
#         8:' ',
#         9:' ',
#     }

board = '#'


def display_board(board):
    patterns = {
        1:'         *         *         ',
        2:'*****************************',
        3:f'    {m[1]}    *    {m[2]}    *    {m[3]}    ',
        4:f'    {m[4]}    *    {m[5]}    *    {m[6]}    ',
        5:f'    {m[7]}    *    {m[8]}    *    {m[9]}    ',
}
    shape = {board:[1,3,1,2,1,4,1,2,1,5,1]}
    for pattern in shape[board[0]]:
        print(patterns[pattern])

def player_input():
    global player1
    global player2
    player1 = "X" if input('Please pick a marker "X" or "O" \n') == "x"or"X" else "O"
    player2 = "O" if player1 == "X" else "X"
    print(f'Player 1 : {player1}')
    print(f'Player 2 : {player2}')

def place_marker(board, marker, m):
    player_position = marker()
    display_board(board)
    position = 0
    while position not in range(1,10):
        try:
            position = int(input('Please insert the position of where you would like to place your marker \n'))
        except:
            print("Posiotion available are between 1 and 9, please try again.")
            
    m[position] = player_position
    print(chr(27) + "[2J")


def win_check(m):
    setChecker = [
        set([m[1],m[2],m[3]]),
        set([m[4],m[5],m[6]]),
        set([m[7],m[8],m[9]]),
        set([m[1],m[4],m[7]]),
        set([m[2],m[5],m[8]]),
        set([m[3],m[6],m[9]]),
        set([m[1],m[5],m[9]]),
        set([m[3],m[5],m[7]])
    ]
    global gameOn
    for x in setChecker:
        if x == {'X'}:
            print('Player "X" has won the game.')
            gameOn = False
            return True
        elif x == {'O'}:
            print('Player "O" has won the game.')
            gameOn = False
            return True
        elif setChecker[0] == {'X','O'} and setChecker[1] == {'X','O'} and setChecker[2] == {'X','O'}:
            gameOn = False
            print("Draw game!")
            return True
        else:
            continue


def choose_first():
    global turn
    if turn == ' ':
        turn = random.choice([player1,player2])
        # print(f'Your turn player {turn}')
        return turn
    elif turn == 'X':
        turn = 'O'
        print(f'Your turn player {turn}')
        return turn
    else:
        turn = 'X'
        print(f'Your turn player {turn}')
        return turn

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


while True:
    m = {
        1:' ',
        2:' ',
        3:' ',
        4:' ',
        5:' ',
        6:' ',
        7:' ',
        8:' ',
        9:' ',
    }
    player_input()
    turn_choice = choose_first()
    condition1 = turn_choice == "X"
    condition2 = turn_choice == "O"
    while condition1 or condition2:
        place_marker(board, choose_first, m)
        if win_check(m):
            display_board(board)
            break
    if not replay():
        break


