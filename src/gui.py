
from datetime import date
from datetime import datetime
import PySimpleGUI as sg
import time
from board import BRD_SIZE
import stone_class as sc
import player_class as pc

# Choices :
# grid or dot board
# board size

class Engine():

    def __init__(self):    

        # Size of board
        MAX_ROWS = MAX_COL = BRD_SIZE


        # Import assets :
        st_black = './assets/stone_black2_gray.png'
        st_white = './assets/stone_white_gray.png'
        stone_white_UI = './assets/stone_white_gray.png'
        stone_white_captured = './assets/stone_white_captured.png'
        stone_black_UI = './assets/stone_black2_gray.png'
        stone_black_captured = './assets/stone_black_captured.png'
        board_dot = './assets/board_dot_2_gray.png'
        board_dots = './assets/board_dot_big_gray.png'
        settings_button = './assets/settings_2.png'
        window_settings = './assets/window_settings.png'
        exit_button = './assets/exit_button_2.png'

        layout = []


        # Exit button :
        # This is stupid bad, haha 

        layout += [[sg.Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t", background_color='#F1F1F1')] \
                + [sg.Button(image_filename=window_settings, image_size=(17,17), border_width=0, key='WINDOW_Settings')] \
                + [sg.Text("", background_color='#F1F1F1')] \
                + [sg.Button(image_filename=exit_button, image_size=(17,17), 
                    button_color=('white', 'white'),border_width=0, key='Exit')]]

        # Bigger dot board positions
        board_dot_pos = [(3,3), (3,9), (3,15), (9,3), (9,9), (9,15), (15,3), (15,9), (15,15)]




        # Initialize board GUI :
        b = []
        for i in range(MAX_ROWS):
            a = []
            
            a += [sg.Text("  ", background_color='#F1F1F1')]

            for j in range(MAX_COL):
                if (i,j) in board_dot_pos:
                    a += [sg.Button("", button_color=('black', 'white'), 
                                    image_filename=board_dots, border_width=0,
                                    size=(4,2), key=(i,j), pad=(0,0))]
                else:
                    a += [sg.Button("", image_filename=board_dot, button_color=('black', 'white'),
                                    border_width=0 ,size=(4,2), key=(i,j), pad=(0,0))]
            b += [a]

        # Add board to the layout
        layout += b


        # Captured and resign UI elements :

        # Resign button :
        layout[13] += [sg.Text("      ", background_color='#F1F1F1')] \
                    + [sg.Button("", button_color=('black', 'white'), 
                                 image_filename=board_dot, border_width=0,
                                 size=(4,2), key=('-RESIGN-'), pad=(0,0))]

        # Capture UI elements :
        layout[16] += [sg.Text("     ", background_color='#F1F1F1')] \
                      + [sg.Button(image_filename=stone_black_UI, key='-ICON1-', border_width=0)] \
                      + [sg.Text(" Captured :", key='-TEXT_UI1-', background_color='#F1F1F1', text_color='black', font='lato')] \
                      + [sg.Text("0",key='-UI1-', background_color='#F1F1F1',text_color='black', font='lato')]


        layout[17] += [sg.Text("     ", background_color='#F1F1F1')] \
                       + [sg.Button(image_filename=stone_white_UI, key='-ICON2-', border_width=0)] \
                       + [sg.Text(" Captured  :", key='-TEXT_UI2-', background_color='#F1F1F1', text_color='black', font='lato')] \
                       + [sg.Text("0", background_color='#F1F1F1', key='-UI2-', text_color='black', font='lato')]


        layout += [[sg.Text("  ", background_color='#F1F1F1')]]


        # Debug window :
        layout2 = [[sg.Multiline("Debug initialized", key='-MULTILINE KEY-', size=(60,40))]]



        # Initialize windows :

        window = sg.Window('GO', layout, background_color='#F1F1F1', no_titlebar=True,
                            grab_anywhere=True, resizable=True).Finalize()

        window2 = sg.Window("Debugger", layout2, resizable=True, grab_anywhere=True,
                            keep_on_top=True, alpha_channel=0.7, background_color='white').Finalize()



        # Initialize players :
        white = pc.player('w')
        black = pc.player('b')


        # Save game moves :
        now = datetime.now()
        save_file = open(("./saves/" + str(date.today()) + now.strftime(", %H-%M-%S") + ".txt"), 'w')
        save_file.write("Game played on : " + str(date.today()) + " at : " + now.strftime("%H-%M-%S"))


        # Capture stones
        def capture_stones(group):
            if group == 0:
                return
            if group is not None:
                if len(group[2]) > 1:
                    for nb in group[2]:
                        window[(nb.x, nb.y)].Update(image_filename=board_dot) 
                    if group[0]=='w' : white.captured += group[1]
                    elif group[0]=='b' : black.captured += group[1]
                elif len(group[2]) == 1:
                    window[(group[2][0].x, group[2][0].y)].Update(image_filename=board_dot) 
                    if group[0]=='w' : white.captured += group[1]
                    elif group[0]=='b' : black.captured += group[1]



        # Move index
        move_idx = 1


        # Event loop
        while True:
            event, values = window.read()

            # Close main window
            if event in (sg.WIN_CLOSED, 'Exit'):
                break

            # Do not respons to 'Captured' Buttons.
            if window[event].Key == '-NONE-' or window[event].Key == '-NONE2-':
                continue

            # Resign
            if window[event].Key == '-RESIGN-':

                    # Update 
                    if move_idx % 2 == 0:
                        window[event].update(button_color=('white', 'white'), image_filename=st_white)
                    else:
                        window[event].update("", button_color=('white', 'white'), image_filename=st_black)


                    # Update UI
                    window['-ICON1-'].Update(image_filename=stone_black_captured)
                    window['-TEXT_UI1-'].update(text_color='#909090')
                    window['-UI1-'].update(text_color='#909090')
            
                    window['-ICON2-'].Update(image_filename=stone_white_captured)
                    window['-TEXT_UI2-'].update(text_color='#909090')
                    window['-UI2-'].update(text_color='#909090')
                   

            # Play game
            if window[event] != '-NONE-' and window[event].Key != '-NONE2-' and window[event].Key != '-RESIGN-':


                # White
                if move_idx % 2 == 0:
                    a = time.time()

                    # Update UI
                    window['-ICON1-'].Update(image_filename=stone_black_UI)
                    window['-TEXT_UI1-'].update(text_color='black')
                    window['-UI1-'].update(text_color='black')
            
                    window['-ICON2-'].Update(image_filename=stone_white_captured)
                    window['-TEXT_UI2-'].update(text_color='#909090')
                    window['-UI2-'].update(text_color='#909090')

                    if window[event].Key not in sc._pl_st:

                        window[event].update(button_color=('white', 'white'), image_filename=st_white)

                        # Play stone :
                        st = white.play(window[event].Key)
                        save_file.write("\n" + str(window[event].Key))
                        
                        # Search for capture in self and neighbours :
                        temp = white.capture(st)
                        if temp is not None:
                            for group in temp:
                                capture_stones(group)

                        # Update the capture UI element :
                        window['-UI1-'].update(str(white.captured))

                        # Update debugger :
                        window2['-MULTILINE KEY-'].print("------------------------")

                        from stone_class import debug_buffer
                        for i in debug_buffer:
                            window2['-MULTILINE KEY-'].print(i)
                        
                        move_idx += 1

                    else:
                        window2['-MULTILINE KEY-'].print("Illigal move.")

                    # Calculate and display time elapsed.
                    b = time.time()
                    window2['-MULTILINE KEY-'].print("\nTime Elapsed :" + str(b-a))
                    debug_buffer.clear()



                # Black move
                else:
                    a = time.time()

                    # Update UI
                    window['-ICON2-'].Update(image_filename=stone_white_UI)
                    window['-TEXT_UI2-'].update(text_color='black')
                    window['-UI2-'].update(text_color='black')
            
                    window['-ICON1-'].Update(image_filename=stone_black_captured)
                    window['-TEXT_UI1-'].update(text_color='#909090')
                    window['-UI1-'].update(text_color='#909090')

                    if window[event].Key not in sc._pl_st:
                        window[event].update("", button_color=('white', 'white'), image_filename=st_black)

                        # Play stone :
                        st = black.play(window[event].Key)
                        save_file.write("\n" + str(window[event].Key))

                        # Search for capture in self and neighbours :
                        temp = black.capture(st)
                        if temp is not None:
                            for group in temp:
                                capture_stones(group)
                
                        # Update the capture UI element :
                        window['-UI2-'].update(str(black.captured))

                       # Update debugger :
                        window2['-MULTILINE KEY-'].print("------------------------")

                        from stone_class import debug_buffer
                        for i in debug_buffer:
                            window2['-MULTILINE KEY-'].print(i)
                        
                        move_idx += 1



                    # First move
                    elif move_idx == 1:
                        window[event].update("", button_color=('white', 'white'), image_filename=st_black)

                        # Play stone :
                        st = black.play(window[event].Key)
                        save_file.write("\n" + str(window[event].Key))

                        # Search for capture in self and neighbours :
                        temp = black.capture(st)
                        if temp is not None:
                            for group in temp:
                                capture_stones(group)

                        # Update the capture UI element :
                        window['-UI2-'].update(str(black.captured))

                       # Update debugger :
                        window2['-MULTILINE KEY-'].print("------------------------")

                        from stone_class import debug_buffer
                        for i in debug_buffer:
                            window2['-MULTILINE KEY-'].print(i)
                        
                        move_idx += 1

                    else:
                        window2['-MULTILINE KEY-'].print("Illigal move.")


                    # Calculate and display time elapsed :
                    b = time.time()
                    window2['-MULTILINE KEY-'].print("\nTime Elapsed :" + str(b-a))
                    debug_buffer.clear()




        save_file.close()
        window.close()

a = Engine()
