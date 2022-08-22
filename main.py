from telaPrincipal import *
from telaLogin import *

App()



"""
# Imports
import PySimpleGUI as sg

# Funcitons
def verify_password(password):
    if password == '1':
        return True
    pass

def verify_user(user):
    if user == 'g':
        return True
    pass

# Layout 
layout = [
    [sg.Text('User')],
    [sg.Input(key = '-USER-')],
    [sg.Text('Password')],
    [sg.Input(key = '-PASSWORD-', password_char='*')],
    [
        sg.Button('Login'), sg.Button('Create Account') 
    ]
]

window = sg.Window("Login System", layout = layout)

# Main Loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Login':
        if str(values['-PASSWORD-']) == "" or values['-USER-'] == "":
            sg.popup("Error, all fields are required!")
        elif verify_password(str(values['-PASSWORD-'])) and verify_user(values['-USER-']):
            sg.popup("Welcome, >>" + values['-USER-']+"<<")
            break
        else:
            sg.popup("Invalid username or password!")
window.close()
"""