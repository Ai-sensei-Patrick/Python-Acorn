from game_parser import read_lines
from grid import grid_to_string
from player import Player


class Game:
    def __init__(self,filename):
        self.filename = read_lines(filename)
        self.player = Player()
        self.win = 0
        self.ls = []

    def gameMove(self,move):
        if move in ['S','s','A','D','d','W','w','a','q','e']:
            self.player.move(move)
            #Take out the message of the cell
            msg = self.filename[self.player.row][self.player.col].message
            bool = self.filename[self.player.row][self.player.col].step(self)
            #Find out whether the cell would end the game or not
            if bool:
                #Find out if the cell is a wall or not
                if self.player.the_wall(move,self.filename):
                    self.add(move)
                return msg
            else:
                #determine win or not
                if self.filename[self.player.row][self.player.col].display=='Y':
                    msg = self.filename[self.player.row][self.player.col].message
                    self.win = 2
                    return msg
                else:
                    msg = self.filename[self.player.row][self.player.col].message
                    self.win = 1
                    return msg
        else:
            return '\nPlease enter a valid move (w, a, s, d, e, q).\n'


    def end_game(self,move):
#game end when stepping on End cell
        if self.win == 2:
            if self.count() == 1:
                print('''\nYou made 1 move.
Your move: {}\n
=====================
====== YOU WIN! =====
====================='''.format(self.add(move)))
            else:
                print('''\nYou made {} moves.
Your moves: {}\n
=====================
====== YOU WIN! =====
====================='''.format(self.count(),self.add(move)))
            return True

#If game end when step on fire
        elif self.win == 1:
            print('''\nYou step into the fires and watch your dreams disappear :(.
\nThe Fire Nation triumphs! The Honourable Furious Forest is reduced to a pile of ash '''\
'''and is scattered to the winds by the next storm... You have been roasted.
\nYou made {} moves.
Your moves: {}\n
=====================
===== GAME OVER =====
====================='''.format(self.count(),self.add(move)))
            return True
        else:
            return False

#make the first board
    def start_game(self):
        self.player.starting(self.filename)
        return grid_to_string(self.filename,self.player)

#make a list that show the player move
    def add(self,move):
        self.ls.append(move.lower())
        return ', '.join(self.ls)

#count number of move
    def count(self):
        return len(self.ls) + 1

#print out the board
    def grid(self,move):
        msg = self.gameMove(move)
        return grid_to_string(self.filename,self.player) + msg
