class Start:
    def __init__(self):
        self.display = 'X'
        self.message = ""
    def step(self,game):
        return True

class End:
    def __init__(self):
        self.display = 'Y'
        self.message = "\nYou walked into a wall. Oof!\n"
    def step(self, game):
        if game.player.row < 0 or game.player.col < 0:
            return True
        self.message = "\n\nYou conquer the treacherous maze set up by the Fire Nation and "\
        "reclaim the Honourable Furious Forest Throne, "\
        "restoring your hometown back to its former glory of "\
        "rainbow and sunshine! Peace reigns over the lands."
        return False

class Air:
    def __init__(self):
        self.display = ' '
        self.message = ""
    def step(self,game):
        return True

class Wall:
    def __init__(self):
        self.display = '*'
        self.message = "\nYou walked into a wall. Oof!\n"

    def step(self,game):
        return True


class Fire:
    def __init__(self):
        self.display = 'F'
        self.message = "\nWith your strong acorn arms, you throw a water bucket at the fire."\
        " You acorn roll your way through the extinguished flames!\n"

    def step(self,game):
        if game.player.num_water_buckets>0:
            game.player.num_water_buckets-=1
            game.filename[game.player.row][game.player.col] = Air()
            return True
        else:
            game.filename[game.player.row][game.player.col] = Air()
            return False

class Water:
    def __init__(self):
        self.display = 'W'
        self.message = "\nThank the Honourable Furious Forest, you've found a bucket of water!\n"

    def step(self, game):
        game.player.num_water_buckets += 1
        game.filename[game.player.row][game.player.col] = Air()
        return True

class Teleport:
    def __init__(self,num):
        self.display = num
        self.message = "\nWhoosh! The magical gates break Physics "\
        "as we know it and opens a wormhole through space and time.\n"
    def step(self, game):
        parse = game.filename
        com = 0
        i=0
        while i < len(parse):
            j=0
            while j < len(parse[i]):
                if parse[i][j].display == parse[game.player.row][game.player.col].display:
                    if game.player.row != i or game.player.col != j:
                        game.player.row = i
                        game.player.col = j
                        com += 1
                        break
                j+=1
            if com == 1:
                break
            i+=1
        return True
