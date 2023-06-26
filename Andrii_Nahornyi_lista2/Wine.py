
class Wine:
    def __init__(self, variables, target):
        self.variables = variables
        self.target = target

    def __repr__(self):
        return f"Wine(variables = {self.variables}, target = {self.target})"