class Action:
    def __init__(self, name):
        self.name = name
        self.sub_actions = []

    def add_sub_actions(self, action):
        self.sub_actions.append(action)




