from os import system
import time
from grid.Grid import Grid as LifeGrid
from tkinter import *



master = Tk()
master.title('Game of Life')
window_width = 1400
window_height = 900
square_length = 20
options_space = 30
window_offset = 3
sleep_time = 0
w = Canvas(master, width=window_width + window_offset - 2, height=window_height + options_space)
running = False
def fillRect(pair: tuple, w: Canvas, fil: str, stroke: str):
    '''Fill the rectangle at the given coordinate with specified fill and stroke colors'''
    i = pair[1]
    j = pair[0]
    rect_x_1 = i * square_length + window_offset
    rect_y_1 = j * square_length + window_offset
    rect_x_2 = ((i +  1) * square_length) + window_offset
    rect_y_2 = ((j + 1) * square_length) + window_offset
    w.create_rectangle(rect_x_1, rect_y_1, rect_x_2, rect_y_2, fill=fil, outline=stroke)
def drawBoard(grid: Grid, w: Canvas):
    '''Draw the board to reflect the grid cells'''
    for i in range(int(window_height / square_length)):
        for j in range(int(window_width / square_length)):
            alive = grid.square_array[i + gridStart[0]][j + gridStart[1]]
            if alive == 1:
                fillRect((i, j), w, 'black', 'black')
            else:
                fillRect((i, j), w, 'white', 'black')
def onStart():
    '''Run when button is pressed, runs the simulation'''
    running = True

    while (running):
        w.delete(ALL)
        grid.turn()
        drawBoard(grid, w)
        w.pack()
        master.update()
        time.sleep(sleep_time)
def onStop():
    '''Pauses generation calculation'''    
    running = False
def gliderGun():
    '''Glider Gun Preset to generate Glider Gun on board'''
    running = False
    grid.clear()
    grid.generateGliderGun()
    drawBoard(grid, w)
def randomBoard():
    '''Random Board preset'''
    running = False
    grid.clear()
    grid.generateRandomBoard()
    drawBoard(grid, w)



#make a grid thats double the longest length in squares
grid_length = 0
if window_width > window_height:
    grid_length = window_width // square_length
else:
    grid_length = window_height // square_length


gridStart = ((grid_length // 2) - (window_width // square_length) // 2 , (grid_length // 2) - (window_height // square_length) // 2)
grid = LifeGrid(grid_length * 2, gridStart)
#random generation for now
# grid.generateRandomBoard(0.5)
grid.generateGliderGun()
drawBoard(grid, w)
start = Button(master, text='Start', command=onStart)
stop = Button(master, text='Stop', command=onStop)
glider_gun_button = Button(master, text='Glider Gun', command=gliderGun)
random_board = Button(master, text='Random Board', command=randomBoard)
w.pack()
start.pack()

stop.pack()
glider_gun_button.pack()
random_board.pack()
master.update()

input()
#life time


