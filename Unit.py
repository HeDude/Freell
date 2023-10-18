from Method import Method
from Skill import Skill

class Unit:
    def __init__(self, type, name, level):
        self.type = type
        self.name = name
        self.level = level
        self.sub_units = []  # List to hold other Un
        self.methods = []
        self.skills = []

    def add_sub_unit(self, unit):
        self.sub_units.append(unit)
    
    def add_method(self, method):
        self.skills.append(method)

    def add_skill(self, skill):
        self.skills.append(skill)



