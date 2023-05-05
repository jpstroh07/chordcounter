from logic.Chordhandler import Chordhandler

class ChordChange:
    def __init__(self):
        self.handler = Chordhandler()
        
    def Execute_Exercise(self):
        chords = self.handler.get2RandomChords()
        