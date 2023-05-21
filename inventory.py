Inventory = []  # placeholder for items to be added

Items = ['key']  # list of items


def inventory():
    """Prints the inventory"""
    print(f"Current Inventory: ")  # Current Inventory message
    for item in Inventory:  # list items in the inventory list
        print(f" * {item.capitalize()}")  # prints items in a list capitalized
        return


def pickup():
    """In a certain part of the map you can pick up an item"""
    import map_layout as m
    global Items, Inventory  # global variables that the function pulls from the lists above
    location_description = m.Map[m.row][m.col]  # current location
    if location_description == 'flowerbed':  # if you are in the flowerbed
        for item in Items:
            print("You picked up a key.")  # print item being added to inventory
            Inventory.append(item)  # add item to inventory
