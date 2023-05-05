from persistence.Chordsparser import Chordsparser
import random

class Chordhandler:
    def __init__(self):
        self.chordparser = Chordsparser()
    
    def get2RandomChords(self):
        chords = self.chordparser.getChords()
        chord1 = random.choice(chords)
        chord2 = random.choice(chords)
        
        if(chord2.name == chord1.name):
            while(chord2.name == chord1.name):
                chord2 = random.choice(chords)
        
        return chord1, chord2