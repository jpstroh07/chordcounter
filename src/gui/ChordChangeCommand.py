from gui.Command import Command
from logic.Chordhandler import Chordhandler
import time
import sys
import os

header = "--------------------------------------------------\n"
header += "Chord Change Exercise\n"
header += "--------------------------------------------------"

class ChordChangeCommand(Command):
    def __init__(self):
        self.handler = Chordhandler()
        
    def execute(self):
        os.system('cls')
        print(header)
        
        chord1, chord2 = self.handler.get2RandomChords()

        time_limit = int(input("Enter time limit in seconds (default 60): "))
        
        os.system('cls')
        print(header)
        
        print(f"Chord 1:\n{chord1}")
        
        print(f"Chord 2:\n{chord2}")
        
        input(f"Press any key to start...")
        
        sys.stdout.write("\033[F")
        sys.stdout.write(" " * len("Press any key to start..."))
        sys.stdout.write("\033[F")
        print("")
        
        start_countdown = range(3, 0, -1)
        for i in start_countdown:
            sys.stdout.write(f"Starting in...\n{i}\n")
            time.sleep(1)
            if i != 1:
                sys.stdout.write("\033[F" * 2)  # Move up 2 lines in the console

        print("GO!")

        for i in range(time_limit, -1, -1):
           sys.stdout.write(f"Time left: {i}\n")
           time.sleep(1)
           if i != 0:
               sys.stdout.write("\033[F")  # Move up 4 lines in the console

        os.system('cls')
        print(header)
        print("Time's up!")
        num_changes = int(input("Enter the number of chord changes: "))