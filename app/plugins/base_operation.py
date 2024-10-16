# app/plugins/base_operation.py
import logging
from app.commands import Command

class BaseOperationCommand(Command):
    operation = None  # To be defined in subclasses

    def execute(self, *args):
        if len(args) != 2:
            command_name = self.__class__.__name__.replace('Command', '').lower()
            logging.warning(f"Usage: {command_name} <num1> <num2>")
            return
        try:
            num1 = float(args[0])
            num2 = float(args[1])
        except ValueError:
            logging.error("Please enter valid numbers")
            return
        try:
            result = self.operation(num1, num2)
            logging.info(f"Result: {result}")
        except Exception as e:
            logging.error(f"Error: {e}")
