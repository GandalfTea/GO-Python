import PySimpleGUI as sg
import random

MAX_ROWS = MAX_COL = 19
a = ('O', '@') 
board = [['' for j in range(MAX_COL)] for i in range(MAX_ROWS)]
board_dot_pos = [( 3,3), (3,9), (3,15), (9,3), (9,9), (9,15), (15,3), (15,9), (15,15)]
layout = []

# stone_black.png is smaller
# stone_black2.pmg is bigger
st_black = './stone_black2.png'
board_dots = './board_dot.png'

b = []
for i in range(MAX_ROWS):
    a = []
    # Row index
    #a += [sg.Text(str(i+1), text_color='black', background_color='white')]

    # 2 choices for display :
    # grid : " | \n-----|-----\n | "
    # interpunct : u"\xb7"

    for j in range(MAX_COL):
        if (i,j) in board_dot_pos:
            a += [sg.Button("", button_color=('black', 'white'), image_filename=board_dots, border_width=0, size=(4,2), key=(i,j), pad=(0,0))]
        else:
            a += [sg.Button(u"\xb7", button_color=('black', 'white'),border_width=0 ,size=(4,2), key=(i,j), pad=(0,0))]
    b += [a]

layout += b

window = sg.Window('GO', layout, background_color='white').Finalize()


while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    window[event].update(board[event[0]][event[1]], button_color=('white', 'white'), image_filename=st_black)


window.close()
