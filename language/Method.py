class Method:
    def __init__(self, level, name):
        self.level = level  # e.g., "Strategy", "Tactic", "Operational"
        self.name = name
        self.sub_methods = []

    def add_sub_method(self, method):
        self.sub_methods.append(method)



