


class World:

    rooms: {}

    def __init__(self, player):
        self.player = player

    def showMap(self, player):
        print(f'~~~\n      - Map -')
        for direction in player.currentRoom.linkedRooms:
            print(f'The {player.currentRoom.linkedRooms[direction].name} is to the {direction}\n')
        print(f'~~~')