# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item


class Room:
    # items: [Item] = []

    # linkedRooms = {}

    def __init__(self, name, desc):
        self.name = name
        self.description = desc
        self.items = []
        self.linkedRooms = {}


    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        for i in self.items:
            if i.name == item:
                self.items.remove(i)

    def linkRoomTo(self, room, inDirection):
        self.linkedRooms[inDirection] = room