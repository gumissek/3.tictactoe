
def print_tictactoe():
    print(table[0])
    print(table[1])
    print(table[2])

table = [['', '', ''], ['', '', ''], ['', '', '']]

print_tictactoe()
col=int(input('Podaj kolumne do ktorej chcesz wpisac'))
row=int(input('podaj wiersz do ktorego chcesz wpisac'))


# sprawdzenie czy komorka jest zajeta
if table[col][row]=='':

else:
    print('Pole jest zajete, wybierz inne')
