from gui.commands import ChordChangeCommand
from gui.commands import ExitCommand

class CommandFactory:
    
    def getCommand(self, command):
        if command == "chordchange":
            return ChordChangeCommand.ChordChangeCommand()
        elif command == "exit":
            return ExitCommand.ExitCommand()
        else:
            raise ValueError(f"Command {command} is not valid.")