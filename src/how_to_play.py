import PySimpleGUI as sg


# How to play window


#   Window :
# Create a trasparent borderless window.
# Skip button closes the window.
# Continue button furthers the presentation.
# Back button

#   Slide :

# Video showing move
# Text explaining rules.


#   Order of slideshow :

# 1. How to place a stone.
# 2. Game mechanics (order of play).
# 3. Single capture.
# 4. Group Capture.
# 5. Concept of eyes.
# 6. Alive vs dead string.
# 7. Ko rule.
# 8. Resign.
# 9. Count teritory.

play_stone = './assets/animations/play_stone.gif'
tutorial_text_1 = './assets/tutorial_text_1.png'
skip_button = './assets/skip_button.png'
back_button = './assets/back_button.png'
forward_button = './assets/forward_button.png'

layout = []
layout += [[sg.Text("\n", background_color='#F1F1F1')]]

layout += [[sg.Image(filename=play_stone, background_color='#F1F1F1', key='-IMAGE-', right_click_menu=['UNUSED', 'Exit'])]]

layout[1] += [sg.Image(filename=tutorial_text_1, background_color='#F1F1F1')]

layout += [[sg.Text("\t\t\t\t\t\t\t    ", background_color='#F1F1F1')] \
        + [sg.Button(image_filename = skip_button, border_width=0, button_color=('#F1F1F1','#F1F1F1'), key='Exit')] \
        + [sg.Text("   ", background_color='#F1F1F1')] \
        + [sg.Button(image_filename = back_button, border_width=0, button_color=('#F1F1F1','#F1F1F1'), key='-BACK-')] \
        + [sg.Button(image_filename = forward_button, border_width=0, button_color=('#F1F1F1','#F1F1F1'), key='-NEXT-')]]

window = sg.Window("Tutorial" ,layout, no_titlebar=True, resizable=True, grab_anywhere=True, keep_on_top=True, background_color='#F1F1F1', alpha_channel=.9)

while True:
    event, values = window.read(timeout=10)
    if event in (sg.WIN_CLOSED, 'Exit', 'Cancel'):
        break
#    window['-IMAGE-'].update_animation(play_stone, time_between_frames=100)


#for i in range(100000):
    window['-IMAGE-'].UpdateAnimation(play_stone, time_between_frames = 40)

