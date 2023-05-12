from logic.Handler import Handler

class ChordChange:
    def __init__(self):
        self.handler = Handler()
        
    def Execute_Exercise(self):
        chords = self.handler.get2RandomChords()
        