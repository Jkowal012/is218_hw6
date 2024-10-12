# app/commands/__init__.py

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
            print("Goodbye!")
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
                print(f"Error: {e}")
        else:
            print(f"Unknown command: {command_name}")
