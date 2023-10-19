class Method:
    def __init__(self, level, name):
        self.level = level  # e.g., "Strategy", "Tactic", "Operational"
        self.name = name
        self.expert_rules = []
        self.sub_methods = []

    def add_expert_rule(self, rule):
        self.expert_rules.append(rule)

    def add_sub_method(self, method):
        self.sub_methods.append(method)



