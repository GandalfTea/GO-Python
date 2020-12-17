import PySimpleGUI as sg
import random


MAX_ROWS = MAX_COL = 19
a = ('O', '@') 
board = [[random.choices(a) for j in range(MAX_COL)] for i in range(MAX_ROWS)]

layout = []
#layout += [[sg.Image(r'C:\Users\maria\Desktop\fun\PythonGame\src\stone_black.png', size=(100,100),)]]

b = []

for i in range(MAX_ROWS):
    a = []
    # Row index
    #a += [sg.Text(str(i+1), text_color='black', background_color='white')]

    # 2 choices for display :
    # grid : " | \n-----|-----\n | "
    # interpunct : u"\xb7"

    for j in range(MAX_COL):
        a += [sg.Button(u"\xb7", button_color=('black', 'white'),border_width=0 ,size=(4,2), key=(i,j), pad=(0,0))]
    b += [a]
layout += b
layout[1] += [sg.Text("\tDebug Console\t\t", background_color = 'white', text_color='black', font='TimesNewRoman')]

layout[2] +=[sg.Text("\t", background_color ='white')] + [sg.Multiline("Debug in progress...")]

window = sg.Window('GO', layout, background_color='white')
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    window[event].update(board[event[0]][event[1]], button_color=('black', 'white'))

window.close()
