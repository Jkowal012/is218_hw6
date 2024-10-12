from app.commands import Command
from app.calculator.operations import multiply

class MultiplyCommand(Command):
    def execute(self, *args):
        if len(args) != 2:
            print("Usage: multiply <num1> <num2>")
            return
        try:
            num1 = float(args[0])
            num2 = float(args[1])
            result = multiply(num1, num2)
            print(f"Result: {result}")
        except ValueError:
            print("Please enter valid numbers")

plugin_name = 'multiply'
plugin_class = MultiplyCommand
