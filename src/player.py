# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room
from item import Item

class Player:
    currentRoom: Room

    items: [Item] = []

    def __init__(self, room):
        self.currentRoom = room


    def addItem(self, item):
        self.items.append(item)