from logic.Handler import Handler
from errors.ProgressNotFoundError import ProgressNotFoundError
import os

class DisplayProgressCommand:
    def __init__(self):
        self.handler = Handler()
    
    def __str__(self):
        return "Display Progress"
    
    def execute(self):
        os.system('cls')
        print("----------------------------------------")
        print("Display Progress")
        print("----------------------------------------")
        
        chord1 = input("Enter first chord: ")
        chord2 = input("Enter second chord: ")
        
        try:
            result = self.handler.getProgress(chord1, chord2)
        except ProgressNotFoundError as e:
            print(e)
            input("Press enter key to continue...")
            return

        print(result)
        
        input("Press enter key to continue...")