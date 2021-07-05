from os import system
import time
import random
class Grid:
    def __init__(self, length: int, grid_start: tuple):
        '''Makes a grid with given length'''
        self.square_array = [[0 for _ in range(length)] for _ in range(length)]
        self.length = length
        self.start = grid_start
           
    def __str__(self):
        string = ''
        for square_list in self.square_array:
            for square in square_list:
                if square == 0:
                    string += '   '
                else:
                    string += ' ▢ '
            string += '\n'
            
        return string
    def clear(self):
        '''Clears the Grid'''
        self.square_array = [[0 for _ in range(length)] for _ in range(length)]
    def withinBounds(self, pair: tuple):
        '''Checks to see if a coordinate pair can be found within the bounds of the grid'''
        x = pair[0]
        y = pair[1]
        return x > 0 and y > 0 and x < self.length and y < self.length
    def isAlive(self, pair: tuple):
        '''Checks if cell at given pair is alive'''

        if self.withinBounds(pair):
            return self.square_array[pair[0]][pair[1]] == 1
        else:
            return False
    def setAlive(self, pair: tuple):
        '''Sets square at given coordinate to alive'''
        x = pair[0]
        y = pair[1]
        if not self.withinBounds(pair):
            return
        else:
            self.square_array[x][y] = 1
    def setDead(self, pair: tuple):
        '''Sets square at given coordinate to dead'''
        x = pair[0]
        y = pair[1]
        if not self.withinBounds(pair):
            return
        else:
            self.square_array[x][y] = 0
    def getSurroundingSum(self, pair: tuple) -> int:
        '''Returns sum of surrounding squares'''
        x = pair[0]
        y = pair[1]
        count = 0
        if x != 0:
            if y != 0:
                count += self.square_array[x - 1][y - 1]
            if y != self.length - 1:
                count += self.square_array[x - 1][y + 1]
            count += self.square_array[x - 1][y]
        if y != 0:
            count += self.square_array[x][y - 1]
        if y != self.length - 1:
            count += self.square_array[x][y + 1]
        if x != self.length - 1:
            if y != 0:
                count += self.square_array[x + 1][y - 1]
            if y != self.length - 1:
                count += self.square_array[x + 1][y + 1]
            count += self.square_array[x + 1][y]    
        return count
    def turn(self):
        '''One turn of the game of life'''
        live_set = set()
        dead_set = set()
        for x, square_list in enumerate(self.square_array):
            for y, square in enumerate(square_list):
                sum = self.getSurroundingSum((x, y))
                if self.isAlive((x, y)):
                    if sum < 2:
                        dead_set.add((x, y))
                    elif sum > 3:
                        dead_set.add((x, y))
                else:
                    if sum == 3:
                        live_set.add((x, y))
        for square in live_set:
            self.setAlive(square)
        for square in dead_set:
            self.setDead(square)
    def generateRandomBoard(self, chanceToBeLive: float):
        '''Generates random board where percentage of squares are live'''
        for x in range(self.length):
            for y in range(self.length):
                rand_num = random.randrange(100)
                if rand_num < int(100 * chanceToBeLive):
                    self.square_array[x][y] = 1
    def generateGliderGun(self):

        '''Generates a Glider Gun at the top left of the grid if space allows'''
        if self.length < 38:
            print('Glider Gun could not be generated within bounds of grid')
        else:
            x = self.start[0]
            y = self.start[1]
            self.generateSquare((5 + x, 1 + y))
            self.generateSquare((3 + x, 35 + y))
            self.generateBlinker((6 + x, 11 + y), False)

            self.square_array[4 + x][12 + y] = 1
            self.square_array[8 + x][12 + y] = 1
            self.square_array[3 + x][13 + y] = 1
            self.square_array[9 + x][13 + y] = 1
            self.square_array[9 + x][14 + y] = 1
            self.square_array[3 + x][14 + y] = 1
            self.square_array[6 + x][15 + y] = 1
            self.square_array[4 + x][16 + y] = 1
            self.square_array[8 + x][16 + y] = 1
            self.generateBlinker((6 + x, 17 + y), False)
            self.square_array[6 + x][18 + y] = 1
            self.generateBlinker((4 + x, 21 + y), False)
            self.generateBlinker((4 + x, 22 + y), False)
            self.square_array[2 + x][23 + y] = 1
            self.square_array[6 + x][23 + y] = 1
            self.square_array[1 + x][25 + y] = 1
            self.square_array[2 + x][25 + y] = 1
            self.square_array[6 + x][25 + y] = 1
            self.square_array[7 + x][25 + y] = 1         
    def generateSquare(self, topLeftCorner: tuple):
        '''Generates a square with the specified coordinate being the top left corner'''
        topLeftCornerX = topLeftCorner[0]
        topLeftCornerY = topLeftCorner[1]
        if topLeftCornerX >= 0 and topLeftCornerX < self.length - 1 and topLeftCornerY > 0 and topLeftCornerY < self.length - 2:
            self.square_array[topLeftCornerX][topLeftCornerY] = 1
            self.square_array[topLeftCornerX][topLeftCornerY + 1] = 1
            self.square_array[topLeftCornerX + 1][topLeftCornerY] = 1
            self.square_array[topLeftCornerX + 1][topLeftCornerY + 1] = 1
        else:
            print('Square could not be generated within bounds of grid')
    def generateBlinker(self, center: tuple, isHorizontal: bool):
        '''Generates a horizontal or vertical blinker with the center coordinates provided'''
        centerX = center[0]
        centerY = center[1]
        if isHorizontal:
            if centerY > 0 and centerY < self.length - 1 and centerX >= 0 and centerX < self.length:
                self.square_array[centerX][centerY] = 1
                self.square_array[centerX][centerY + 1] = 1
                self.square_array[centerX][centerY - 1] = 1
            else:
                print('Blinker could not be generated within grid')
        else:
            if centerX > 0 and centerX < self.length - 1 and centerY >= 0 and centerY < self.length:
                self.square_array[centerX][centerY] = 1
                self.square_array[centerX + 1][centerY] = 1
                self.square_array[centerX - 1][centerY] = 1
            else:
                print('Blinker could not be generated within grid')
    def generateGlider(self, center: tuple):
        '''Generates a glider with the center coordinates provided'''
        centerX = center[0]
        centerY = center[1]
        if centerX > 0 and centerX < self.length - 1 and centerY > 0 and centerY < self.length - 1:
            self.square_array[centerX][centerY + 1] = 1
            self.square_array[centerX - 1][centerY] = 1
            self.generateBlinker((centerX + 1, centerY), True)
        else:
            print("Glider could not be generated within grid bounds")