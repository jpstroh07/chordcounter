class Chord:
    def __init__(self, name, frets, fingers):
        self.name = name
        self.frets = frets
        self.fingers = fingers
        
    def __str__(self):
        return f'{self.name}: {self.frets}'
    
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