# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item

class Room:
    name: str
    description: str

    items: [Item] = []

    def __init__(self, name, desc):
        self.name = name
        self.description = desc


    def addItem(self, item):
        self.items.append(item)