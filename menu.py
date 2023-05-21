
playing = True


def menu_options():
    """Menu options"""
    print('* Walk')  # print walk
    print('* Inventory')  # print inventory
    print('* Map')
    print('* Quit')  # print quit


def menu():
    """The main menu of the game"""
    import inventory as i
    import messages as mess
    import map_layout as m
    global playing  # globe variables that the menu pulls from
    while playing:
        action_choice = input(f"Choice: ")  # player choices are inputted

        if (action_choice.lower() == 'walk') or (action_choice.lower() == 'w'):  # if the player types: walk or w
            possible_directions()

        elif (action_choice.lower() == 'inventory') or (action_choice.lower() == 'i'):  # if player types inventory or i
            i.inventory()  # run inventory function
            print('\n')
            mess.message()

        elif (action_choice.lower() == 'map') or (action_choice.lower() == 'm'):
            m.draw_map()

        elif (action_choice.lower() == 'quit') or (action_choice.lower() == 'q'):  # if player types quit or q
            print("Are you sure you want to quit?")  # print confirmation message
            # print instructions to quit and input function
            confirmation = input(f"Type Quit or Q to quit the game: quit: ")
            if (confirmation.lower() == 'quit') or (confirmation.lower() == 'q'):  # if the player types quit or q
                print(f"Goodbye :( .")  # when the loop ends it prints the farewell message
                exit()
            elif (confirmation.lower() == 'back') or (confirmation.lower() == 'b'):
                mess.message()
            else:
                print("Invalid Option")  # if the player inputs an invalid option
                mess.message()


def possible_directions():
    import map_layout as maps
    import movement as move
    while True:
        print(f"Where would you like to go?")  # prints question
        if maps.row != 0:
            print(f" * North")  # prints north as an option if the row does not equal to 0
        if maps.row != maps.MaxRow:
            print(f" * South")  # prints south as an option if the row does not exceed 2
        if maps.col != maps.MaxCol:
            print(f" * East")  # print east as an option if the column does not exceed 2
        if maps.col != 0:
            print(f" * West")  # print west as an option if the column does not equal to 0
        print(f" * Back")
        move.movement()
