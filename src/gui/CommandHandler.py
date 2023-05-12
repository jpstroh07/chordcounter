from . import Menu
import os

def start():
    menu = Menu.Menu()

    menu.addCommand("chordchange")
    menu.addCommand("exit")

    while True:
        os.system('cls')
        
        print("----------------------------------------")
        print("Guitar Practice - Main Menu")
        print("----------------------------------------")
        
        menu.displayCommands()
        menu.executeCommand(int(input("Enter command: ")))