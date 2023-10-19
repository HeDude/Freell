class Actor:
    def __init__(self, name):
        self.name = name
        self.sub_actors = []

    def add_sub_actors(self, actor):
        self.sub_actors.append(actor)




