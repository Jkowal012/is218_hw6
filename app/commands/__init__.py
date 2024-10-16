# app/commands/__init__.py
import logging 

class Command:
    def execute(self, *args):
        raise NotImplementedError("Execute method not implemented")

class CommandHandler:
    def __init__(self):
        self.commands = {}
    
    def register_command(self, name, command):
        self.commands[name] = command
    
    def execute_command(self, input_line):
        if input_line.lower() == 'exit':
            logging.info("Goodbye!")
            exit(0)
        parts = input_line.strip().split()
        if not parts:
            return
        command_name, *args = parts
        command = self.commands.get(command_name)
        if command:
            try:
                command.execute(*args)
            except Exception as e:
                logging.error(f"Error: {e}")
        else:
            logging.warning(f"Unknown command: {command_name}")
