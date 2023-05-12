import sys
import os

class ExitCommand:
    def __str__(self):
        return "Exit Program"
    
    def execute(self):
        os.system('cls')
        
        print("----------------------------------------")
        print("Exit Program")
        print("----------------------------------------")
        print("Exiting...")
        
        sys.exit(0)