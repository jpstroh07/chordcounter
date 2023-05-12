from logic.Chordhandler import Chordhandler

c = Chordhandler()

while True:
    chord1, chord2 = c.get2RandomChords()
    print(chord1)
    print(chord2)
    input()