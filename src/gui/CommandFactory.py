from gui.commands import ChordChangeCommand
from gui.commands import ExitCommand
from gui.commands import DisplayProgressCommand
from gui.commands import DisplayAllProgressCommand

class CommandFactory:
    
    def getCommand(self, command):
        if command == "chordchange":
            return ChordChangeCommand.ChordChangeCommand()
        elif command == "exit":
            return ExitCommand.ExitCommand()
        elif command == "displayProgress":
            return DisplayProgressCommand.DisplayProgressCommand()
        elif command == "displayAllProgress":
            return DisplayAllProgressCommand.DisplayAllProgressCommand()
        else:
            raise ValueError(f"Command {command} is not valid.")