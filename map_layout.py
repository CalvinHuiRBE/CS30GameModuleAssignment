import messages as m

# map layout
map_grid = [
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
    """
    Draws the map and prints the outcome to an external file.
    :return:
    """

    with open('map_output.txt', 'w') as f:
        f.write(' _______________ _______________ _______________\n')
        for row in map_grid:
            f.write('|               |               |               |\n')
            f.write(f'|  {row[0]:^12s} |  {row[1]:^12s} |  {row[2]:^12s} |\n')
            f.write('|_______________|_______________|_______________|\n')
    m.message()


