from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

#room['outside'].n_to = room['foyer']
#room['foyer'].s_to = room['outside']
#room['foyer'].n_to = room['overlook']
#room['foyer'].e_to = room['narrow']
#room['overlook'].s_to = room['foyer']
#room['narrow'].w_to = room['foyer']
#room['narrow'].n_to = room['treasure']
#room['treasure'].s_to = room['narrow']

room['outside'].linkRoomTo(room['foyer'], 'n')
room['foyer'].linkRoomTo(room['outside'], 's')
room['foyer'].linkRoomTo(room['overlook'], 'n')
room['foyer'].linkRoomTo(room['narrow'], 'e')
room['overlook'].linkRoomTo(room['foyer'], 's')
room['narrow'].linkRoomTo(room['foyer'], 'w')
room['narrow'].linkRoomTo(room['treasure'], 'n')
room['treasure'].linkRoomTo(room['narrow'], 's')

sword = Item("Sword", "A big sword")
room['outside'].addItem(sword)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
newPlayer = Player(room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

#if newPlayer.currentRoom.linkedRooms[direction] is not None:

# Private Functions
def moveTo(direction):
    if direction in newPlayer.currentRoom.linkedRooms:
        newPlayer.currentRoom = newPlayer.currentRoom.linkedRooms[direction]
    else:
        print(f"Not a valid move")

def take(itemName):
    for i in newPlayer.currentRoom.items:
        if i.name == itemName:
            newPlayer.currentRoom.removeItem(itemName)
            newPlayer.addItem(i)

def drop(itemName):
    for i in newPlayer.items:
        if i.name == itemName:
            newPlayer.removeItem(itemName)
            newPlayer.currentRoom.addItem(i)

def showInventory():
    if len(newPlayer.items) > 0:
        print(f"Your inventory contains: {newPlayer.items}")
    else:
        print(f"You have nothing in your inventory")


# Loop
while True:
    print(f"\n Currently in room: {newPlayer.currentRoom.name}")
    print(f"\n {newPlayer.currentRoom.description}")
    print(f"\n This room contains: {newPlayer.currentRoom.items}")

    action = input("\nChoose an action:").split()

    if len(action) == 1:
        if action == 'q':
            print("Done")
            break

        if action in ('n', 'e', 's', 'w'):
            moveTo(action)

        elif action in ('i', 'inventory'):
            showInventory()

        else:
            print(f"Not a valid command")

    elif len(action) == 2:
        if action[0] == 'take':
            take(action[1])

        elif action[0] == 'drop':
            drop(action[1])