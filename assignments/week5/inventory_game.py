import sys
import time

# --- game state ---
inventory = []
health = 3
current_room = "Great Hall"
MAX_INVENTORY_SIZE = 5
has_shield = False

def type_print(text):
    # prints with typing effect
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.015)
    print()

# all items in each room
rooms = {
    "Great Hall": [
        {"name": "Torch", "type": "tool", "description": "Lights up dark places. You should use it and look around again"},
        {"name": "Bread", "type": "food", "description": "Restores one life point."},
        {"name": "Map", "type": "tool", "description": "Might show you the layout."},
        {"name": "Broken Sword", "type": "tool", "description": "Could be useful against enemies."},
        {"name": "Mirror", "type": "hazard", "description": "A tall, cracked mirror leans against the wall. There is something special about it"},
        {"name": "Stone Key", "type": "tool", "description": "This might open the door to the Treasure Chamber."},
        {"name": "Shadow Dust", "type": "hazard", "description": "A cursed substance that drains your energy."}

    ],
    "Treasure Chamber": [
        {"name": "Jeweled Key", "type": "tool", "description": "Unlocks the exit."},
        {"name": "Bread", "type": "food", "description": "Restores one life point."},
        {"name": "Spider Egg", "type": "hazard", "description": "You get bitten trying to pick it up!"},
        {"name": "Ancient Scroll", "type": "tool", "description": "It’s written in an unreadable language."},
        {"name": "Rusted Shield", "type": "tool", "description": "Offers a bit of protection."},
        {"name": "Cursed Amulet", "type": "hazard", "description": "The amulet pulses with dark energy. You feel weaker."}
    ]
}

# --- functions ---
def show_inventory():
    # displays player's inventory
    if not inventory:
        type_print("Your inventory is empty.")
    else:
        type_print("You carry:")
        for item in inventory:
            type_print(f"- {item['name']}")

def show_room_items():
    # describes the current room's visible items
    type_print(f"You are in the {current_room}. You see:")
    for item in rooms[current_room]:
        # you need torch to see all the items available
        if current_room == "Great Hall" and not find_item("Torch", inventory):
            if item["name"] == "Torch":
                type_print(f"- {item['name']}")
            continue
        type_print(f"- {item['name']}")
        # only show the mirror's description
        if (current_room == "Great Hall"
            and find_item("Torch", inventory)
            and item["name"].lower() == "mirror"):
            type_print(f"  {item['description']}")


def find_item(item_name, collection):
    # finds item in a given collection
    for item in collection:
        if item["name"].lower() == item_name.lower():
            return item
    return None

def pick_up(item_name):
    # picks up an item if available and handles effects
    global health, has_shield
    if len(inventory) >= MAX_INVENTORY_SIZE:
        type_print("Your inventory is full. You should drop something you don't need anymore!")
        return
    item = find_item(item_name, rooms[current_room])
    if not item:
        type_print("No such item here.")
        return

    # Special mirror event
    if item["name"].lower() == "mirror":
        type_print("You walk slowly toward the mirror...")
        time.sleep(1)
        type_print("As you reach for it, your reflection flickers.")
        time.sleep(1)
        type_print("It smiles — but you didn’t.")
        type_print("The surface shimmers and a cold hand reaches out...")
        time.sleep(1)
        type_print("You stumble back as the mirror bursts into shards!")
        health -= 2
        type_print("(-2 health)")
        if health <= 0:
            type_print("The temple got you. You see stars and everything spins....")
            time.sleep(1)
            type_print("suddenly everything goes black. GAME OVER")
            exit()
        rooms[current_room].remove(item)
        return

    # losing health
    if item["type"] == "hazard":
        if has_shield:
            type_print(f"You feel a dark force from the {item['name']}, but your Rusted Shield absorbs the damage. You drop the item back on the floor in fear.")
        else:
            health -= 1
            type_print(f"Oh no! Picking up the {item['name']} harmed you. Health is now {health}. You drop the item back on the floor in fear.")
    else:
        inventory.append(item)
        type_print(f"You picked up the {item['name']}.")
        type_print(f"(It's a {item['type'].capitalize()}: {item['description']})")
        # shield to protect you
        if item['name'] == 'Rusted Shield':
            has_shield = True
    rooms[current_room].remove(item)


def drop(item_name):
    # drops an item from inventory into the current room
    item = find_item(item_name, inventory)
    if not item:
        type_print("You don't have that item.")
        return
    inventory.remove(item)
    rooms[current_room].append(item)
    type_print(f"You dropped the {item['name']}.")

def use(item_name):
    # uses an item and handles its effect
    global current_room, health
    item = find_item(item_name, inventory)
    if not item:
        type_print("You don't have that item.")
        return
    if item['name'] == 'Torch':
        type_print("You light up the area and notice a passage leading to the Treasure Chamber.")
    elif item['name'] == 'Stone Key':
        if current_room == "Great Hall":
            type_print("You unlock the door to the Treasure Chamber. You can now use 'move room' to enter it.")
        else:
            type_print("Nothing to unlock here with the Stone Key.")
    elif item['name'] == 'Broken Sword':
        if current_room == "Treasure Chamber":
            type_print("You fend off a lurking spider in the shadows with the broken sword.")
        else:
            type_print("You wave the sword around, just in case.")
    elif item['name'] == 'Rusted Shield':
        type_print("You strap the Rusted Shield to your arm. It might protect you from some harm.")
    elif item['name'] == 'Jeweled Key':
        if current_room == "Great Hall":
            type_print("You unlock the final exit and escape the temple.")
            type_print("As the temple doors creak open, sunlight floods the hall. You breathe the air of freedom. You've survived the cursed temple and live to tell the tale. Victory!")
            sys.exit()
        else:
            type_print("There’s nothing to unlock here.")
    elif item['name'] == 'Bread':
        if health < 3:
            health += 1
            type_print(f"You eat the bread and regain one health. Health is now {health}.")
            inventory.remove(item)
        else:
            type_print("You’re already at full health.")
    elif item['name'] == 'Map': # print full map
        print("""Map layout:
          +--------------------+
          |   Treasure Chamber|
          +--------------------+
                   ^
             [locked door]
                   ^
          +--------------------+
          |     Great Hall     | > [ancient signs on a wall... and a tiny hole]
          +--------------------+

    You need the Stone Key to enter the Treasure Chamber. The Jeweled Key will unlock the exit.""")
    elif item['name'] == 'Ancient Scroll':
        type_print("You can't make sense of the scroll. Maybe it's useless...")
    else:
        type_print("You can't use that now.")

def examine(item_name):
    # examines an item from inventory or the room
    item = find_item(item_name, inventory) or find_item(item_name, rooms[current_room])
    if item:
        type_print(f"{item['name']}: {item['description']}")
    else:
        type_print("You don't see that item here.")

def move_room():
    # moves to treasure chamber with conditionals
    global current_room, health
    if current_room == "Great Hall":
        if find_item("Stone Key", inventory):
            current_room = "Treasure Chamber"
            type_print("You are now in the Treasure Chamber.")
        else:
            if find_item("Broken Sword", inventory):
                type_print("A giant spider blocks the way, but you fight it off with your Broken Sword. You manage to get through.")
                current_room = "Treasure Chamber"
                type_print("You are now in the Treasure Chamber.")
            else:
                type_print("As you try to force the door, a giant spider attacks you! You lose 1 health.")
                health -= 1
                type_print(f"Health is now: {health}")
    elif current_room == "Treasure Chamber":
        current_room = "Great Hall"
        type_print("You are now in the Great Hall.")
    else:
        type_print("You can’t go anywhere from here. Try using an item instead.")

# --- game loop ---
def game_loop():
    # main loop of the game
    global health
    type_print("You stand in complete darkness. Cold stone surrounds you, and the air is thick with the scent of old dust.")
    type_print("Somewhere in this forgotten temple, a way out exists — but you’ll need the right tools to survive.")
    type_print("Welcome to the Temple Escape!")
    type_print("Type 'help' for a list of commands.")
    while True:
        if health <= 0:
            type_print("You have perished in the temple. Game Over.")
            break
        command = input("\n> ").strip().lower()
        if command == "help":
            type_print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], move room, try escape, quit")
        elif command == "inventory":
            show_inventory()
        elif command == "look":
            show_room_items()
        elif command.startswith("pickup "):
            item_name = command[7:]
            pick_up(item_name)
        elif command.startswith("drop "):
            item_name = command[5:]
            drop(item_name)
        elif command.startswith("use "):
            item_name = command[4:]
            use(item_name)
        elif command == "move room":
            move_room()
        elif command == "try escape":
            try_escape()
        elif command.startswith("examine "):
            item_name = command[8:]
            examine(item_name)
        elif command == "quit":
            type_print("Thanks for playing!")
            break
        else:
            type_print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    game_loop()

