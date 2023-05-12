from gui import ChordChangeCommand

class CommandFactory():
    
    def getCommand(self, command):
        if command == "chordchange":
            return ChordChangeCommand.ChordChangeCommand()
        else:
            raise ValueError(f"Command {command} is not valid.")