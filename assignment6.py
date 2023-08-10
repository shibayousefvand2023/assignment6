
def show():
    for row in game_board:
        for cell in row:
            print(cell, end= '/')
            print()

def test_game1():
    # vertical test 1
    if game_board[0][0] == 'z' and game_board[1][0] == 'z' and game_board[2][0] == 'z':
        print('winner: player 1 (z)')
        return True
    # vertical test 2
    if game_board[0][1] == 'z' and game_board[1][1] == 'z' and game_board[2][1] == 'z':
        print('winner: player 1 (z)')
        return True
        # vertical test3
    if game_board[0][2] == 'z' and game_board[1][2] == 'z' and game_board[2][2] == 'z':
        print('winner: player 1 (z)')
        return True
    # Horizantal test1
    if game_board[0][0] == 'z' and game_board[0][1] == 'z' and game_board[0][2] == 'z':
        print('winner: player 1 (z)')
        return True
    # Horizantal test2
    if game_board[1][0] == 'z' and game_board[1][1] == 'z' and game_board[1][2] == 'z':
       print('winner: player 1 (z)')
       return True
    # Horizantal test3
    if game_board[2][0] == 'z' and game_board[2][1] == 'z' and game_board[2][2] == 'z':
        print('winner: player 1 (z)')
        return True
    # cross test1
    if game_board[0][0] == 'z' and game_board[1][1] == 'z' and game_board[2][2] == 'z':
        print('winner: player 1 (z)')
        return True
    # cross test2
    if game_board[0][2] == 'z' and game_board[1][1] == 'z' and game_board[2][0] == 'z':
        print('winner: player 1 (z)')
        return True
    return False


def test_game2():
    # vertical test 1
    if game_board[0][0] == 'c' and game_board[1][0] == 'c' and game_board[2][0] == 'c':
        print('winner: player 2 (c)')
        return True
    # vertical test 2
    if game_board[0][1] == 'c' and game_board[1][1] == 'c' and game_board[2][1] == 'c':
        print('winner: player 2 (c)')
        return True
        # vertical test3
    if game_board[0][2] == 'c' and game_board[1][2] == 'c' and game_board[2][2] == 'c':
        print('winner: player 2 (c)')
        return True
    # Horizantal test1
    if game_board[0][0] == 'c' and game_board[0][1] == 'c' and game_board[0][2] == 'c':
        print('winner: player 2 (c)')
        return True
    # Horizantal test2
    if game_board[1][0] == 'c' and game_board[1][1] == 'c' and game_board[1][2] == 'c':
        print('winner: player 2 (c)')
        return True
    # Horizantal test3
    if game_board[2][0] == 'c' and game_board[2][1] == 'c' and game_board[2][2] == 'c':
        print('winner: player 2 (c)')
        return True
    # cross test1
    if game_board[0][0] == 'c' and game_board[1][1] == 'c' and game_board[2][2] == 'c':
        print('winner: player 2 (c)')
        return True
    # cross test2
    if game_board[0][2] == 'c' and game_board[1][1] == 'c' and game_board[2][0] == 'c':
        print('winner: player 2 (c)')
        return True
    return False


from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('Tic_Tac_Toe'))


game_board= [['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']]

show()

turns = 0

while True:
    # player1
    print('player1:')
    row = int(input('Enter row:' ))
    col = int(input('Enter col:'))
    if 0 <= row <= 2 and 0 <= col <= 2:
        if game_board[row][col] == '.':
            game_board[row][col] == 'z'
            show()
            if test_game1():
                break
            turns += 1
        else:
            print('choose another one num')
    else:
        print('you can choose between 0 and 2')
        
    # check for tie
    if turns == 9:
        print('No winner')
        break

# player2
    print('player2:')
    row = int(input('Enter row:' ))
    col = int(input('Enter col:'))
    if 0 <= row <= 2 and 0 <= col <= 2:
        if game_board[row][col] == '.':
            game_board[row][col] == 'c'
            show()
            if test_game2():
                break
            turns += 1
        else:
            print('choose another one num')
    else:
        print('you can choose between 0 and 2')
        
    # check for tie
    if turns == 9:
        print('No winner')
        break
