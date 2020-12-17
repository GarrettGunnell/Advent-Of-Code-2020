from copy import deepcopy

inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
grid = {}
for line in inputLines:
    line = line.strip()
    input.append([char for char in line])

grid[0] = deepcopy(input)

def pretty_print(input):
    for i in input:
        string = ''
        for char in i:
            string += char
        print(string)

def add_layers(grid):
    new_layer = []

    for z in sorted(grid.keys()):
        grid[z].insert(0, ['.' for _ in range(len(grid[z][0]))])
        grid[z].insert(len(grid[z]), ['.' for _ in range (len(grid[z][0]))])
    
        for line in grid[z]:
            line.insert(0, '.')
            line.insert(len(line), '.')

    for _ in range(len(grid[0])):
        new_layer.append(['.' for j in range(len(grid[0][0]))])

    grid[min(grid.keys()) - 1] = deepcopy(new_layer)
    grid[max(grid.keys()) + 1] = deepcopy(new_layer)


def sample_neighbor(grid, r, c, s, x, y, z):
    return grid[s + z][r + y][c + x] if 0 <= r + y < len(grid[0]) and 0 <= c + x < len(grid[0][0]) and min(grid.keys()) <= s + z <= max(grid.keys()) else None

def sample_neighbors(grid, r, c, s):
    active = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):  
                if x == 0 and y == 0 and z == 0: continue
                if sample_neighbor(grid, r, c, s, x, y, z) == '#': active += 1
                if active > 3: return active

    return active

def silver(grid):
    iteration = 0

    while iteration < 6:
        add_layers(grid)
        previous_iteration = deepcopy(grid)

        for z in sorted(grid.keys()):
            for line in range(len(grid[z])):
                for cell in range(len(grid[z][line])):
                    active = sample_neighbors(previous_iteration, line, cell, z)
                    if previous_iteration[z][line][cell] == '#':
                        grid[z][line][cell] = '.' if active != 2 and active != 3 else '#'
                    else:
                        grid[z][line][cell] = '#' if active == 3 else '.'

        iteration += 1

    active = 0
    for z in sorted(grid.keys()):
        for line in grid[z]:
            for char in line:
                if char == '#': active += 1

    return active

def gold(grid):
    return

print(silver(grid))
print(gold(grid))