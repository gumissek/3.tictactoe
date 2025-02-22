import random


def print_tictactoe():
    for level in table:
        print(level)

table = [['', '', ''], ['', '', ''], ['', '', '']]
marks=['X','O']
player1=marks[0]
player2=marks[1]
players=[player1,player2]

print_tictactoe()
is_game_on=True
current_player=random.choice(players)
while is_game_on:



    print(f'Obency gracz to: {current_player}')
    col=int(input('Podaj kolumne do ktorej chcesz wpisac'))
    row=int(input('podaj wiersz do ktorego chcesz wpisac'))


    # sprawdzenie czy komorka jest zajeta
    try:
        cell=table[row-1][col-1]
    except IndexError:
        print('Nie ma takiej komorki wybierz inna')
    else:
        if table[row-1][col-1]=='':
            table[row-1][col-1]=current_player
            if current_player==player1:
                current_player=player2
            else:
                current_player=player1
            print('Zmiana gracza')
        else:
            print('Pole jest zajete, wybierz inne')


    print_tictactoe()