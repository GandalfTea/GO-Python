import PySimpleGUI as sg
import player_class as pc
import random

MAX_ROWS = MAX_COL = 19

board = [['' for j in range(MAX_COL)] for i in range(MAX_ROWS)]

# Import assets :

# stone_black.png is smaller
# stone_black2.pmg is bigger
st_black = './stone_black2.png'
st_white = './stone_white.png'
board_dots = './board_dot.png'
exit_button = './exit_button.png'


layout = []

# Exit button :
# This is stupid bad, haha 
layout += [[sg.Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t", background_color='white')] + [sg.Button(image_filename=exit_button, button_color=('white', 'white'),border_width=0, key='Exit')]]

board_dot_pos = [( 3,3), (3,9), (3,15), (9,3), (9,9), (9,15), (15,3), (15,9), (15,15)]


# Initialize playspace :
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


# Player data :

layout[14] += [sg.Text("\t", background_color='white')] + [sg.Image(filename=st_black)] + [sg.Text("   Captured : \t", background_color='white', text_color='black', font='lato')]
layout[15] += [sg.Text("\t", background_color='white')] + [sg.Image(filename=st_white)] + [sg.Text("   Captured : \t", background_color='white', text_color='black', font='lato')]

# Initialize window :

window = sg.Window('GO', layout, background_color='white', no_titlebar=True, grab_anywhere=True, resizable=True).Finalize()

# Initialize players :
white = pc.player('w')
black = pc.player('b')


# Make the keys in the matrix indexes and than access them.

move_idx = 1

# Event loop
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if window[event]:
        if move_idx % 2 == 0:
            window[event].update(board[event[0]][event[1]], button_color=('white', 'white'), image_filename=st_white)
            white.play(window[event].Key)
            move_idx += 1
        else:
            window[event].update(board[event[0]][event[1]], button_color=('white', 'white'), image_filename=st_black)
            black.play(window[event].Key)
            move_idx += 1



window.close()
