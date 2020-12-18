import PySimpleGUI as sg


class Log:
    layout = [[sg.Multiline("Debugger", key='-MULTILINE KEY-', size=(45,20))]]
    window = sg.Window("Debugger", layout, background_color = 'white').Finalize()
    def Print(self, string):
        window['-MULTILINE KEY-'].print(string)

Log = Log()
Log.Print("asdasd")
    
