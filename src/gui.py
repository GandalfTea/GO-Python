import PySimpleGUI as sg
import time
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
stone_white_UI = './stone_white_UI.png'
stone_black_UI = './stone_black_UI.png'


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

layout[14] += [sg.Text("\t", background_color='white')] + [sg.Button(image_filename=stone_black_UI, border_width=0)] + [sg.Text("   Captured : \t",key='-UI1-', background_color='white', text_color='black', font='lato')]
layout[15] += [sg.Text("\t", background_color='white')] + [sg.Button(image_filename=stone_white_UI, border_width=0)] + [sg.Text("   Captured : \t",key='-UI2-', background_color='white', text_color='black', font='lato')]

# Debug window :
layout2 = [[sg.Multiline("Debug initialized", key='-MULTILINE KEY-', size=(60,40))]]

# Initialize window :
# Main window

window = sg.Window('GO', layout, background_color='white', no_titlebar=True, grab_anywhere=True, resizable=True).Finalize()

window2 = sg.Window("Debugger", layout2, resizable=True, grab_anywhere=True, keep_on_top=True, alpha_channel=0.7, background_color='white').Finalize()

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
            a = time.time()
            window[event].update(board[event[0]][event[1]], button_color=('white', 'lightgray'), image_filename=st_white)
            white.play(window[event].Key)
            
            window2['-MULTILINE KEY-'].print("------------------------")

            from stone_class import debug_buffer
            for i in debug_buffer:
                window2['-MULTILINE KEY-'].print(i)

            b = time.time()
            window2['-MULTILINE KEY-'].print("\nTime Elapsed :" + str(b-a))
            debug_buffer.clear()
            move_idx += 1

        else:
            a = time.time()
            window[event].update(board[event[0]][event[1]], button_color=('white', 'lightgray'), image_filename=st_black)
            black.play(window[event].Key)
            window2['-MULTILINE KEY-'].print("------------------------")

            from stone_class import debug_buffer
            for i in debug_buffer:
                window2['-MULTILINE KEY-'].print(i)

            b = time.time()
            window2['-MULTILINE KEY-'].print("\nTime Elapsed :" + str(b-a))
            debug_buffer.clear()
            move_idx += 1



window.close()
