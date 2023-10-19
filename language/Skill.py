class Skill:
    def __init__(self, name):
        self.name = name
        self.pre_skills = []
        self.sub_skills = []

    def add_sub_skill(self, skill):
        self.sub_skills.append(skill)




