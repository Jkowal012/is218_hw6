from app.plugins.base_operation import BaseOperationCommand
from app.calculator.operations import add

class AddCommand(BaseOperationCommand):
    operation = staticmethod(add)

plugin_name = 'add'
plugin_class = AddCommand
