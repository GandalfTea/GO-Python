import PySimpleGUI as sg


# How to play window
class Tutorial:
    def __init__(self):
    
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

        # Imports
        play_stone = './assets/animations/play_stone.gif'
        play_order = './assets/animations/order.gif'
        show_turn = './assets/animations/show_turn.gif'
        capture_solo = './assets/animations/single_capture.gif'
        capture_group_no_eye = './assets/animations/capture_group_no_eye.gif'
        capture_group_eye = './assets/animations/capture_group_eye.gif'

        play_stone_text = './assets/text/place_stone_text.png'
        order_text = './assets/text/order_text.png'
        show_turn_text = './assets/text/see_turn_text.png'
        capture_solo_text = './assets/text/single_capture_text.png'
        group_capture_no_eye_text = './assets/text/group_capture_no_eye_text.png'
        eyes_text = './assets/text/eye_text.png'
        group_capture_eye_text = './assets/text/group_capture_eye_text.png'
        alive_text = './assets/text/alive_text.png'

        skip_button = './assets/skip_button.png'
        back_button = './assets/back_button.png'
        forward_button = './assets/forward_button.png'

        # Add all gifs and texts to container and than iterate with index.
        gifs = [play_stone, play_order, show_turn, capture_solo, capture_group_no_eye, capture_group_eye]

        texts = [play_stone_text, order_text, show_turn_text, capture_solo_text, group_capture_no_eye_text, group_capture_eye_text]

        # Layout 
        layout = []
        layout += [[sg.Text("\n", background_color='#F1F1F1')]]


        # Gif
        layout += [[sg.Image(filename=gifs[0], background_color='#F1F1F1', key='-IMAGE-', right_click_menu=['UNUSED', 'Exit'])]]


        # Text
        layout[1] += [sg.Image(filename=texts[0], background_color='#F1F1F1', key='-TEXT-')]


        # Buttons
        layout += [[sg.Text("\t\t\t\t\t\t\t    ", background_color='#F1F1F1')] \
                + [sg.Button(image_filename = skip_button, border_width=0, button_color=('#F1F1F1','#F1F1F1'), key='Exit')] \
                + [sg.Text("   ", background_color='#F1F1F1')] \
                + [sg.Button(image_filename = back_button, border_width=0, button_color=('#F1F1F1','#F1F1F1'), key='-BACK-')] \
                + [sg.Button(image_filename = forward_button, border_width=0, button_color=('#F1F1F1','#F1F1F1'), key='-NEXT-')] \
                + [sg.Text("\n", background_color='#F1F1F1')]]

        window = sg.Window("Tutorial" ,layout, no_titlebar=True, resizable=True, grab_anywhere=True, keep_on_top=True, background_color='#F1F1F1', alpha_channel=.9)


        index = 0

        while True:
            event, values = window.read(timeout=10)
            if event in (sg.WIN_CLOSED, 'Exit', 'Cancel'):
                break
            if event == '-NEXT-':
                if index + 1 < len(gifs):
                    index += 1
                window['-IMAGE-'].Update(filename=gifs[index])
                window['-TEXT-'].Update(filename=texts[index])
            if event == '-BACK-':
                if index - 1 >= 0:
                    index -= 1
                window['-IMAGE-'].Update(filename=gifs[index])
                window['-TEXT-'].Update(filename=texts[index])

            window['-IMAGE-'].UpdateAnimation(gifs[index], time_between_frames = 40)


a = Tutorial()
