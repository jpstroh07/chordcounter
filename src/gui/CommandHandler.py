from . import Menu
import os

def start():
    menu = Menu.Menu()

    menu.addCommand("chordchange")
    menu.addCommand("displayProgress")
    menu.addCommand("displayAllProgress")
    menu.addCommand("exit")

    while True:
        try:
            os.system('cls')
        
            print("----------------------------------------")
            print("Guitar Practice - Main Menu")
            print("----------------------------------------")
        
            menu.displayCommands()
            menu.executeCommand(int(input("Enter command: ")))
        except Exception:
            print("Enter a valid command!")
            input("Press enter to continue...")