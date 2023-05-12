import xml.etree.ElementTree as ET
from logic.Chord import Chord

class Chordsparser:
    
    def getChords(self):
        tree = ET.parse('src/persistence/db/chords.xml')
        root = tree.getroot()
        chords = []
        for chord_elem in root.findall('chord'):
            chord = Chord.from_xml(chord_elem)
            chords.append(chord)
        return chords