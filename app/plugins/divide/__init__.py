from app.plugins.base_operation import BaseOperationCommand
from app.calculator.operations import divide
import logging

class DivideCommand(BaseOperationCommand):
    operation = staticmethod(divide)

plugin_name = 'divide'
plugin_class = DivideCommand
