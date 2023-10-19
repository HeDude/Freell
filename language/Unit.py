from Actor import Actor
from Action import Action
from Method import Method
from Prerequisite import Prerequisite
from Resource import Resource
from Skill import Skill

class Unit:
    def __init__(self, type, name, level):
        self.type = type
        self.name = name
        self.level = level
        self.sub_units = []  # List to hold other Un
        self.actors = []
        self.actions = []
        self.methods = []
        self.prerequisites = []
        self.resources = []
        self.skills = []

    def add_sub_unit(self, unit):
        self.sub_units.append(unit)
    
    def add_actor(self, actor):
        self.skills.append(actor)
        
    def add_action(self, action):
        self.skills.append(action)

    def add_method(self, method):
        self.skills.append(method)

    def add_prerequisite(self, prerequisite):
        self.prerequisites.append(prerequisite)

    def add_resource(self, resource):
        self.skills.append(resource)
 
    def add_skill(self, skill):
        self.skills.append(skill)



