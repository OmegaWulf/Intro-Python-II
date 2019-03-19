# Implement a class to hold room information. This should have name and
# description attributes.

import item

class room:
    name: str
    description: str

    items: [item] = []

    def __init__(self, name, desc):
        self.name = name
        self.description = desc


    def addItem(self, item):
        self.items.append(item)