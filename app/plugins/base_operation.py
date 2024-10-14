from app.commands import Command

class BaseOperationCommand(Command):
    operation = None  # To be defined in subclasses

    def execute(self, *args):
        if len(args) != 2:
            command_name = self.__class__.__name__.replace('Command', '').lower()
            print(f"Usage: {self.__class__.__name__.replace('Command', '').lower()} <num1> <num2>")
            return
        try:
            num1 = float(args[0])
            num2 = float(args[1])
            result = self.operation(num1, num2)
            print(f"Result: {result}")
        except ValueError:
            print("Please enter valid numbers")
        except Exception as e:
            print(f"Error: {e}")
