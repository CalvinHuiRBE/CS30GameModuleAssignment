# map layout
map_grid = [
    ['shed', 'backyard', 'flowerbed'],
    ['kitchen', 'dining-room', 'living-room'],
    ['washroom', 'front-foyer', 'garage']
]

output_file = 'map_output.txt'


def draw_map(map_grid, file_path):
    with open(file_path, 'w') as f:
        f.write(' _______________ _______________ _______________\n')
        for row in map_grid:
            f.write('|               |               |               |\n')
            f.write(f'|  {row[0]:^12s} |  {row[1]:^12s} |  {row[2]:^12s} |\n')
            f.write('|_______________|_______________|_______________|\n')


draw_map(map_grid, output_file)
