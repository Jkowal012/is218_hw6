class Calculation: 
    def __init__(self,first, second, operation):
        self.first = first
        self.second = second
        self.operation = operation

    def get_ans(self):
        return self.operation(self.first, self.second)
