from persistence.Chordsparser import Chordsparser
from persistence.ProgressHandler import ProgressHandler
import random

class Handler:
    def __init__(self):
        self.chordparser = Chordsparser()
        self.progresshandler = ProgressHandler()
    
    def get2RandomChords(self):
        chords = self.chordparser.getChords()
        chord1 = random.choice(chords)
        chord2 = random.choice(chords)
        
        if(chord2.name == chord1.name):
            while(chord2.name == chord1.name):
                chord2 = random.choice(chords)
        
        return chord1, chord2
    
    def insertProgress(self, chord1, chord2, time):
        self.progresshandler.insertProgress(chord1, chord2, time)
        
    def getProgress(self, chord1, chord2):
        return self.progresshandler.getProgress(chord1, chord2)
    
    def getAllProgress(self):    
        return self.progresshandler.getAllProgress()