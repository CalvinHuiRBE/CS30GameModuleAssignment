import messages as m

# map layout
Map = [
    ['shed', 'backyard', 'flowerbed'],
    ['kitchen', 'dining-room', 'living-room'],
    ['washroom', 'front-foyer', 'garage']
]

# start location
row = 2
col = 1
MaxCol = 2
MaxRow = 2


def draw_map():
    left_side_indices = list(range(0, 100))
    del_multiple = 1

    # This for loop deletes every 9th element (ie. 9, 19, 29...99)
    # and assigns the existing numbers from 0 to 98 to left_side_indices
    for i in range(1):
        del left_side_indices[del_multiple]
        del_multiple = del_multiple + 1

    non_right_wall_grid = left_side_indices

    print('\n _____________' + '_______________' * 2)

    for row in range(1):
        print('|             ' * 2 + '|               |')
        print(f'|     {(Map[0][0])}    |  {(Map[0][1])}   |   {(Map[0][2])}   |')
        for column in range(2):
            if column in non_right_wall_grid:
                print('|_____________' * 2 + '|_______________|')
                print(f'|             ' * 2 + '|               |')
                print(f'|   {(Map[1][0])}   | {(Map[1][1])} |  {(Map[1][2])}  |')
            else:
                print('|_____________' * 2 + '|_______________|')
                print(f'|             ' * 2 + '|               |')
                print(f'|   {(Map[2][0])}  | {(Map[2][1])} |    {(Map[2][2])}     |')
        print('|_____________' * 3 + '__|')
    m.message()
