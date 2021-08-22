class Player:
    def __init__(self):
        self.display = 'A'
        self.num_water_buckets = 0
        self.col = 0
        self.row = 0

#player starting position
    def starting(self,parse):
        i=0
        while i < len(parse):
            j=0
            while j < len(parse[i]):
                if parse[i][j].display == 'X':
                    self.row = i
                    self.col = j
                j+=1
            i+=1
#player move
    def move(self,move):
        if move == 'w' or move == 'W':
            self.row -= 1
        elif move == 'a' or move == 'A':
            self.col -= 1
        elif move == 's' or move == 'S':
            self.row += 1
        elif move == 'd' or move == 'D':
            self.col += 1
        elif move == 'e':
            self.row
            self.col

#Wall cell check
    def the_wall(self,move,grid):
        if move == 'w' or move == 'W':
            if grid[self.row][self.col].display == '*' or self.row < 0 or self.col < 0:
                self.row += 1
                return False
            else:
                return True
        elif move == 'a' or move == 'A':
            if grid[self.row][self.col].display == '*' or self.row < 0 or self.col < 0:
                self.col += 1
                return False
            else:
                return True
        elif move == 's' or move == 'S':
            if grid[self.row][self.col].display == '*' or self.row < 0 or self.col < 0:
                self.row -= 1
                return False
            else:
                return True
        elif move == 'd' or move == 'D':
            if grid[self.row][self.col].display == '*' or self.row < 0 or self.col < 0:
                self.col -= 1
                return False
            else:
                return True
        return True
