from logic.Handler import Handler
import time
import sys
import os

header = "--------------------------------------------------\n"
header += "Chord Change Exercise\n"
header += "--------------------------------------------------"

class ChordChangeCommand:
    def __init__(self):
        self.handler = Handler()
        
    def __str__(self):
        return "Chord Change Exercise"
        
    def execute(self):
        os.system('cls')
        print(header)
        
        chord1, chord2 = self.handler.get2RandomChords()

        time_limit = 12
        
        os.system('cls')
        print(header)
        
        print(f"Chord 1:\n{chord1}")
        
        print(f"Chord 2:\n{chord2}")
        
        input(f"Press enter to start...")
        
        sys.stdout.write("\033[F")
        sys.stdout.write(" " * len("Press any key to start..."))
        sys.stdout.write("\033[F")
        print("")
        
        start_countdown = range(3, 0, -1)
        for i in start_countdown:
            sys.stdout.write(f"Starting in... {i}\n")
            time.sleep(1)
            if i != 1:
                sys.stdout.write("\033[F")

        sys.stdout.write("\033[F")
        sys.stdout.write(" " * len("starting in 3..."))
        sys.stdout.write("\033[F")
        print("")
        sys.stdout.write("Go!\n")

        time.sleep(1)
        sys.stdout.write("\033[F")
        
        for i in range(time_limit, -1, -1):
            if i >= 10:
                sys.stdout.write(f"Time left: {i}\n")
            else:
                sys.stdout.write(f"Time left:  {i} \n")
            time.sleep(1)
            if i != 0:
                sys.stdout.write("\033[F")

        os.system('cls')
        print(header)
        print("Time's up!")
        
        num_changes = int(input("Enter the number of chord changes: "))
        self.handler.insertProgress(chord1.name, chord2.name, num_changes)