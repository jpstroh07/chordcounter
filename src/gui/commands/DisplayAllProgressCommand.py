from logic.Handler import Handler
from errors.ProgressNotFoundError import ProgressNotFoundError

import os

class DisplayAllProgressCommand:
    def __init__(self):
        self.handler = Handler()

    def __str__(self):
        return "Display All Progress"

    def execute(self):
        os.system('cls')
        print("----------------------------------------")
        print("Display All Progress")
        print("----------------------------------------")

        try:
            for progress in self.handler.getAllProgress():
                print(progress)
        except ProgressNotFoundError as e:
            print(e)

        input("Press enter to continue...")