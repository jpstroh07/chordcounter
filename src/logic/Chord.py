import re

class Chord:
    def __init__(self, name, frets, fingers):
        self.name = name
        self.frets = frets
        self.fingers = fingers
        
    def __str__(self):
        fretboard = [['|' for _ in range(5)] for _ in range(6)]

        # Loop through the fingers list and populate the matrix with the finger numbers
        for finger_data in self.fingers:
            fret = int(finger_data['fret'])
            string = 'EADGBe'.index(finger_data['string'])
            finger = finger_data['finger']

            # Only populate the matrix if the fret is within the displayed range (1-5)
            if 1 <= fret <= 5:
                fretboard[string][fret - 1] = finger

        # Convert the matrix to a string representation
        
        s = self.frets
        s = re.sub(r",", " ", s)
        s = re.sub(r"[1-9]", " ", s)
        
        fretboard_str = s + '\n'
        
        for row in zip(*fretboard):
            fretboard_str += ' '.join(row) + '\n'

        # Return the string representation
        return f'     {self.name}\n' + fretboard_str
    
    @classmethod
    def from_xml(cls, xml_element):
        name = xml_element.attrib['name']
        frets = xml_element.attrib['frets']
        fingers = []
        
        for finger in xml_element.findall('finger'):
            finger_data = {
                'finger': finger.get('finger'),
                'fret': finger.get('fret'),
                'string': finger.get('string')
            }
            fingers.append(finger_data)
            
        return cls(name, frets, fingers)