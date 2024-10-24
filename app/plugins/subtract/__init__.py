from app.plugins.base_operation import BaseOperationCommand
from app.calculator.operations import subtract

class SubtractCommand(BaseOperationCommand):
    operation = staticmethod(subtract)

plugin_name = 'subtract'
plugin_class = SubtractCommand
