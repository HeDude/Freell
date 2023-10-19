class Prerequisite:
    def __init__(self, name):
        self.name = name
        self.sub_prerequisites = []

    def add_sub_prerequisites(self, prerequisite):
        self.sub_prerequisites.append(prerequisite)




