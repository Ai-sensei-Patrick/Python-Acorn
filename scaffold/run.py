from game import Game
import os
import sys
#define the self
try:
    game = Game(sys.argv[1])
except FileNotFoundError:
    print('{} does not exist!'.format(sys.argv[1]))
    sys.exit()
except ValueError as e:
    print(e)
    sys.exit()
#start of game
print(game.start_game())
a = input('Input a move: ')
#looping until end of game
while True:
    os.system("clear")
    if a == 'q':
        print('\nBye!')
        sys.exit()
    else:
        print(game.grid(a))
        if game.end_game(a):
            sys.exit()
        a=input('Input a move: ')
    os.system("clear")
