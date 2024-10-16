from app.plugins.base_operation import BaseOperationCommand
from app.calculator.operations import multiply
import logging

class MultiplyCommand(BaseOperationCommand):
    operation = staticmethod(multiply)

plugin_name = 'multiply'
plugin_class = MultiplyCommand
