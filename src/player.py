# Write a class to hold player information, e.g. what room they are in
# currently.

import room
import item

class player:
    currentRoom: room

    items: [item] = []

    def __init__(self, room):
        self.currentRoom = room