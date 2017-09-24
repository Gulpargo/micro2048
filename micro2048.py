# github.com/Gulpargo
# NOTA: [width][height] == [rows][colums]
import random
import time
import os  

class Micro2048(object):
    BASE = 2
    table = []
    gameOver = False

    def __init__(self, width=4, height=4, base=2):
        self.ROWS = width
        self.COLS = height
        self.BASE = base
        for y in range(self.ROWS):
            self.table.append([0 for x in range(self.COLS)])
        super().__init__()

    #Will print the table to stdout
    def debug_print(self):
        for i in range(0,self.ROWS):
            for j in range(0,self.COLS):
                if self.table[i][j] == 0:
                    print('. ', end='')
                else:
                    print(str(self.table[i][j]) + ' ', end='')
            print()
        print()

    #returns true if there is any zero
    def anyZero(self):
        return any(0 in element for element in self.table);

    #will change Game Over variable
    def checkGameOver(self):
        if not self.anyZero() and not self.possibleMove('w') and not self.possibleMove('s') and not self.possibleMove('a') and not self.possibleMove('d'):
            self.gameOver = True
        else:
            self.gameOver = False

    #Spawns BASE variale on random location.       
    def spawn(self):
        if(self.anyZero()):
            #Generate some numbers...
            x = random.randint(0,self.ROWS-1)
            y = random.randint(0,self.COLS-1)
            while self.table[x][y] != 0:
                x = random.randint(0,self.ROWS-1)
                y = random.randint(0,self.COLS-1)
            #Slight change of getting a 4 instead of 2 depending on chance
            if random.randint(1,1000) > 990:
                self.table[x][y] = self.BASE*2
            else:
                self.table[x][y] = self.BASE
            
    #Will execute a tick untill the invalid tick. If there was any valid tick, spawn.
    def turn(self, direction):
        modified = self.tick(direction)
        while self.tick(direction):
            pass
        if modified:
            self.spawn()
            pass
        self.checkGameOver()
        
    #Tick will execute a movement and return false if it was not possible to move.
    def tick(self, way):
        modified = False
        wmap = {'w': [1, 0, 0, 0, -1, 0], 's': [0, -1, 0, 0, 1, 0], 'a': [0, 0, 1, 0, 0, -1], 'd': [0, 0, 0, -1, 0, 1]}
        if way  != 'w' and way  != 's' and way  != 'a' and way  != 'd':
            return False

        for i in range(wmap[way][0], self.ROWS + wmap[way][1]):
            for j in range(wmap[way][2], self.COLS + wmap[way][3]):
                if (self.table[i + wmap[way][4]][j + wmap[way][5]] == 0) and (self.table[i][j] != 0):
                    self.table[i + wmap[way][4]][j + wmap[way][5]] = self.table[i][j]
                    self.table[i][j] = 0
                    modified = True
                elif (self.table[i][j] != 0) and (self.table[i + wmap[way][4]][j + wmap[way][5]] == self.table[i][j]):
                    self.table[i + wmap[way][4]][j + wmap[way][5]] += self.table[i][j]
                    self.table[i][j] = 0
                    modified = True   
                else:
                    modified = False    
        return modified

    #Just like tick, but will return true if a move was possible
    def possibleMove(self, way):
        possibleMove = False
        wmap = {'w': [1, 0, 0, 0, -1, 0], 's': [0, -1, 0, 0, 1, 0], 'a': [0, 0, 1, 0, 0, -1], 'd': [0, 0, 0, -1, 0, 1]}

        for i in range(wmap[way][0], self.ROWS + wmap[way][1]):
            for j in range(wmap[way][2], self.COLS + wmap[way][3]):
                if (self.table[i + wmap[way][4]][j + wmap[way][5]] == 0) and (self.table[i][j] != 0):
                    possibleMove = True
                elif (self.table[i][j] != 0) and (self.table[i + wmap[way][4]][j + wmap[way][5]] == self.table[i][j]):
                    possibleMove = True       
        return possibleMove
