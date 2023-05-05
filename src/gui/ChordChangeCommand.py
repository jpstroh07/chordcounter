from gui.Command import Command
from logic.Chordhandler import Chordhandler
import time
import threading
import os

class ChordChangeCommand(Command):
    def __init__(self):
        self.handler = Chordhandler()
        
    def execute(self):
        os.system('cls')
        time_limit = input("Enter time limit in seconds (default 60): ")
        if not time_limit:
            time_limit = 60
        else:
            time_limit = int(time_limit)

        chord1, chord2 = self.handler.get2RandomChords()

        print(f"Change from {chord1.name} ({chord1.frets}) to {chord2.name} ({chord2.frets})")

        input("Press any key to start...")
        print("Starting in...")
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)
        print("GO!")
        
        timer_thread = threading.Thread(target=display_time_left, args=[time_limit])
        timer_thread.start()

        start_time = time.time()
        while time.time() - start_time < time_limit:
            pass
            
        timer_thread.join()


        num_changes = int(input("Enter the number of chord changes: "))

        # save progress to storage
        # self.handler.save_progress(num_changes)
        
def display_time_left(time_left):
    while time_left > 0:
        print("Time left:", time_left)
        time_left -= 1
        time.sleep(1)