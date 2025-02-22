import random


def print_tictactoe():
    for level in TABLE:
        print('_______')
        print(f'{level[0]} | {level[1]} | {level[2]}')
    print('_______')

# def check_win():
#     global player1_score
#     global player2_score
#     # skosy / \ diagonal
#     if TABLE[0][0] == player1 and TABLE[1][1] == player1 and TABLE[2][2] == player1:
#         print(f'Player {player1} scores a point :3')
#         player1_score += 1
#         return True
#     elif TABLE[0][2] == player1 and TABLE[1][1] == player1 and TABLE[2][0] == player1:
#         print(f'Player {player1} scores a point :3')
#         player1_score += 1
#         return True
#     if TABLE[0][0] == player2 and TABLE[1][1] == player2 and TABLE[2][2] == player2:
#         print(f'Player {player2} scores a point :3')
#         player2_score += 1
#         return True
#     elif TABLE[0][2] == player2 and TABLE[1][1] == player2 and TABLE[2][0] == player2:
#         print(f'Player {player2} scores a point :3')
#         player2_score += 1
#         return True
#     # kolumny | | | columns
#     if TABLE[0][0] == player1 and TABLE[1][0] == player1 and TABLE[2][0] == player1 or TABLE[0][1] == player1 and \
#             TABLE[1][1] == player1 and TABLE[2][1] == player1 or TABLE[0][2] == player1 and TABLE[1][2] == player1 and \
#             TABLE[2][2] == player1:
#         print(f'Player {player1} scores a point :3')
#         player1_score += 1
#         return True
#     elif TABLE[0][0] == player2 and TABLE[1][0] == player2 and TABLE[2][0] == player2 or TABLE[0][1] == player2 and \
#             TABLE[1][1] == player2 and TABLE[2][1] == player2 or TABLE[0][2] == player2 and TABLE[1][2] == player2 and \
#             TABLE[2][2] == player2:
#         print(f'Player {player2} scores a point :3')
#         player2_score += 1
#         return True
#     # wiersze --- rows
#     for level in TABLE:
#         if level[0] == player1 and level[1] == player1 and level[2] == player1:
#             print(f'Gracz {player1} scores a point :3')
#             player1_score += 1
#             return True
#         elif level[0] == player2 and level[1] == player2 and level[2] == player2:
#             print(f'Gracz {player2} scores a point :3')
#             player2_score += 1
#             return True

def checking_win(player):
    # skosy / \ diagonal
    if (TABLE[0][0] == player and TABLE[1][1] == player and TABLE[2][2] == player) or (
            TABLE[0][2] == player and TABLE[1][1] == player and TABLE[2][0] == player):
        return True
    # kolumny | | | columns
    for column in range(len(TABLE[0])):
        if TABLE[0][column] == player and TABLE[1][column] == player and TABLE[2][column] == player:
            return True
    # wiersze --- rows
    for row in TABLE:
        if row[0] == player and row[1] == player and row[2] == player:
            return True


def is_table_full(table):
    for row in table:
        if '' in row:
            return False
    return True


def reset_table():
    for wiersz in TABLE:
        for index in range(len(wiersz)):
            wiersz[index] = ''


TABLE = [['', '', ''], ['', '', ''], ['', '', '']]
marks = ['X', 'O']
player1 = marks[0]
player2 = marks[1]
players = [player1, player2]
player1_score = 0
player2_score = 0

is_game_on = True
current_player = random.choice(players)

while is_game_on:
    keep_playing = 'Y'
    while keep_playing == 'Y':
        print_tictactoe()
        print(f'Current score X: {player1_score}')
        print(f'Current score O: {player2_score}')
        print('---------------------------------')
        print(f'Current player is: {current_player}')

        chosen_row = int(input('Type a row you want to pick: '))
        chosen_column = int(input('Type a column you want to pick: '))

        # checking if cell is empty
        try:
            cell = TABLE[chosen_row - 1][chosen_column - 1]
        except IndexError:
            print('\n' * 20)
            print('That cell doesn`t exist, pick another')
        else:
            if cell == '':

                TABLE[chosen_row - 1][chosen_column - 1] = current_player

                if current_player == player1:
                    current_player = player2
                    print('\n' * 20)
                else:
                    current_player = player1
                    print('\n' * 20)
            else:
                print('\n' * 20)
                print('That cell is not empty, choose another')
        if checking_win(player1):
            print(f'Player {player1} scores a point')
            player1_score += 1
            reset_table()
            keep_playing = input('Do you want to play tictactoe? type Y for yes or N for no: ').upper()
        if checking_win(player2):
            print(f'Player {player2} scores a point')
            player2_score += 1
            reset_table()
            keep_playing = input('Do you want to play tictactoe? type Y for yes or N for no: ').upper()
        if is_table_full(TABLE):
            print('DRAW')
            reset_table()
            keep_playing = input('Do you want to play tictactoe? type Y for yes or N for no: ').upper()
    else:
        print('Thanks for playing ~Piotr')
        quit()
