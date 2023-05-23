
import map_layout as m
import menu as men
import inventory as i
import dictionary as dic

playing = True


def message():
    """
    Messages that corresponds to the location the player is currently in and execute functions for player being there
    """
    while playing:
        # location description dictated by the location of the player on the map
        current_location = m.map_grid[m.row][m.col]
        location_description = current_location
        if location_description == 'front-foyer':  # if the location matches the name then print
            print(dic.map_info['front-foyer']["location"])
            print(dic.map_info['front-foyer']["description"])
            men.menu_options()  # prints menu options
            men.menu()  # goes back to the action menu
        if location_description == 'living-room':  # if the location matches the name then print
            print(dic.map_info['living-room']["location"])
            print(dic.map_info['living-room']["description"])
            men.menu_options()  # prints action menu options
            men.menu()  # goes back to the action menu
        if location_description == 'garage':  # if the location matches the name then print
            print(dic.map_info['garage']["location"])
            print(dic.map_info['garage']["description"])
            men.menu_options()  # prints action menu options
            men.menu()  # goes back to the action menu
        if location_description == 'flowerbed':  # if the location matches the name then print
            print(dic.map_info['flowerbed']["location"])
            print(dic.map_info['flowerbed']["description"])
            i.pickup()  # function that picks up the key the player said they saw
            men.menu_options()  # prints action menu options
            men.menu()  # goes back to the action menu
        if location_description == 'shed':  # if the location matches the name then print
            print(dic.map_info['shed']["location"])
            if i.Inventory == ['key']:
                print(dic.map_info['shed']['description']['unlocked'])
                print("Thanks for playing.")
                exit()
            else:
                print(dic.map_info['shed']['description']['locked'])
            men.menu_options()  # prints action menu options
            men.menu()  # goes back to the action menu options
        if location_description == 'dining-room':  # if the location matches the name then print
            print(dic.map_info['dining-room']["location"])
            print(dic.map_info['dining-room']["description"])
            men.menu_options()  # prints action menu options
            men.menu()  # goes back to the action menu options
        if location_description == 'backyard':  # if the location matches the name then print
            print(dic.map_info['backyard']["location"])
            print(dic.map_info['backyard']["description"])
            men.menu_options()  # prints action menu options
            men.menu()  # goes back to the action menu options
        if location_description == 'kitchen':
            print(dic.map_info['kitchen']["location"])
            print(dic.map_info['kitchen']["description"])
            men.menu_options()
            men.menu()
        if location_description == 'washroom':
            print(dic.map_info['washroom']["location"])
            print(dic.map_info['washroom']["description"])
            men.menu_options()
            men.menu()
