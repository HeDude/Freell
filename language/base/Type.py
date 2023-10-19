class Type:
    def __init__(self, name):
        self.name = name
        self.items = []  # List to hold instances of derived classes

    def add_item(self, item):
        if isinstance(item, Type):
            self.items.append(item)
        else:
            raise ValueError(f"Item must be an instance of Type, got {type(item)}")

    def remove_item(self, item):
        self.items.remove(item)

