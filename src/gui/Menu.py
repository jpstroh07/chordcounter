from . import CommandFactory

class Menu:
    def __init__(self):
        self.commands = []
        self.commandFactory = CommandFactory.CommandFactory()
        
    def addCommand(self, command):
        self.commands.append(self.commandFactory.getCommand(command))
        
    def displayCommands(self):
        for i, command in enumerate(self.commands):
            print(f"{i+1}. {command}")
            
    def executeCommand(self, command):
        self.commands[command-1].execute()