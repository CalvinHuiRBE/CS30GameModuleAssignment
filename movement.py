def movement():
    import map_layout as maps
    import messages as mess
    import menu as men
    while True:
        """
        Prints movement options according to the location of the player and prevents the player form walking off the map
        """
        # player can input their desired direction with in the list above
        movement_choice = input(f"Choice move: ")  # player movement choices are inputted

        # if the movement choice was north or n the player will subtract 1 from the row in the array
        if (movement_choice.lower() == 'north') or (movement_choice.lower() == "n") and maps.row > 0:
            maps.row -= 1
            mess.message()
            break
        # if the movement choice was south or s the player will add 1 unit to the row in the array
        elif (movement_choice.lower() == 'south') or (movement_choice.lower() == "s") and maps.row < maps.MaxRow:
            maps.row += 1
            mess.message()
            break
        # if the movement choice was east or e the player will add 1 unit to the column in the array
        elif (movement_choice.lower() == 'east') or (movement_choice.lower() == "e") and maps.col < maps.MaxCol:
            maps.col += 1
            mess.message()
            break
        # if the movement choice was north or n the player will subtract 1 from the column in the array
        elif (movement_choice.lower() == 'west') or (movement_choice.lower() == "w") and maps.col > 0:
            maps.col -= 1
            mess.message()
            break
        # type back to back out and return to main menu
        elif (movement_choice.lower() == 'back') or (movement_choice.lower() == "b"):
            mess.message()

        else:
            print(f"Sorry cant go that way!")  # any other movement input would print invalid option message
            men.possible_directions()
