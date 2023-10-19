class Resource:
    def __init__(self, name):
        self.name = name
        self.sub_resources = []

    def add_sub_resources(self, resource):
        self.sub_resources.append(resource)




