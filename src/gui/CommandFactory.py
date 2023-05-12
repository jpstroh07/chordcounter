from gui.commands import ChordChangeCommand
from gui.commands import ExitCommand
from gui.commands import DisplayProgressCommand

class CommandFactory:
    
    def getCommand(self, command):
        if command == "chordchange":
            return ChordChangeCommand.ChordChangeCommand()
        elif command == "exit":
            return ExitCommand.ExitCommand()
        elif command == "displayProgress":
            return DisplayProgressCommand.DisplayProgressCommand()
        else:
            raise ValueError(f"Command {command} is not valid.")