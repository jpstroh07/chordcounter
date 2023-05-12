import xml.etree.ElementTree as ET
from logic.Chord import Chord
import os
from pathlib import Path

progress_path = "src/persistence/db/progress.xml"

class Chordsparser:
    def __init__(self):
        if not os.path.exists(progress_path):
            with open(progress_path, 'wb') as file:
                file.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
                file.write(b'<progress>\n\n</progress>')
    
    def getChords(self):
        tree = ET.parse('src/persistence/db/chords.xml')
        root = tree.getroot()
        chords = []
        for chord_elem in root.findall('chord'):
            chord = Chord.from_xml(chord_elem)
            chords.append(chord)
        return chords