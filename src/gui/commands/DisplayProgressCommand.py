from logic.Handler import Handler
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
        
        result = self.handler.getProgress(chord1, chord2)
        
        if len(result) == 0:
            print(f"No progress found for {chord1} -> {chord2}")
        else:
            print(f"Chord Progression: {result}")
        
        input("Press any key to continue...")