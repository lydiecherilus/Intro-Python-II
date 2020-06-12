from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"), 

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""), 

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""), 

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""), 

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# List of items

tiara = Item("tiara", "Beautiful and Precious")
bag = Item("bag", "Protect valuable")
candle = Item("candle", "Shine light")
lighter = Item("lighter", "DO you have a candle?")
maps = Item("maps", "Help to find burried treasure")
pen = Item("pen", "All set!")

# Add items to rooms

room["outside"].items.append(candle)
room["foyer"].items.append(bag)
room["overlook"].items.append(maps)
room["narrow"].items.append(lighter)
room["treasure"].items.append(tiara)
room["outside"].items.append(pen)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

name = input("Please enter your name: ")
player = Player(name, room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
print("")
print(f"Welcome, {name}!, Enjoy playing!")
print(player.current_room.name)
print(player.current_room.description)

print("")
print("Please enter your diection: ")
print(player.current_room)

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    direction = input("\n-> ")
    if direction == "q":
        print("Goodbye!")
        break
    elif direction in ["n", "s", "e", "w"]:
        player.travel(direction)
        print(player.current_room.name)
        print(player.current_room.description)
        print("Please enter your diection from the list: ")
        # Print valid directions
        print(player.current_room)
        print(f'Items you have: {player.inventory}')
    
        # Allow player to take and drop items from rooms
        action = input("Please enter take or drop followed by an item name to take or drop an item: ")
        user_action = action.split(" ")
        print(user_action)
        
        if user_action[0] == "take":
            item = player.current_room.get_item(user_action[1])
            if item == None:
                print("That item is not in the room.")
            else:
                # Remove items from rooms and add them to player contents
                player.current_room.items.remove(item)
                player.inventory.append(item)
                item.on_take()
        elif user_action[0] == "drop":
            item = player.get_item(user_action[1])
            if item == None:
                print("That item is not in your inventory.")
            else:
                # Remove items from player items list and add them to rooms and add them to rooms
                player.current_room.items.append(item)
                player.inventory.remove(item)
                item.on_drop()
 
    else:
        print("Invalid direction.")
        print("Please enter a valid diection from the list of items: ")
        print(player.current_room)