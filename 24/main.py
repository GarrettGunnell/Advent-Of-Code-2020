from copy import deepcopy

inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
for line in inputLines:
    line = line.strip()
    instructions = []
    i = 0
    while i < len(line):
        if i + 1 == len(line):
            instructions.append(line[i])
            break
        else:
            possible_instruction = line[i] + line[i + 1]
            if possible_instruction == 'se' or possible_instruction == 'sw' \
               or possible_instruction == 'nw' or possible_instruction == 'ne':
                instructions.append(possible_instruction)
                i += 2
            else:
                instructions.append(line[i])
                i += 1

    input.append(instructions)

black_tiles = set()
directions = {
    'w': [1, -1, 0],
    'e': [-1, 1, 0],
    'nw': [0, -1, 1],
    'ne': [-1, 0, 1],
    'sw': [1, 0, -1],
    'se': [0, 1, -1]
}

for instructions in input:
    point = [0, 0, 0]
    for instruction in instructions:
        for i in range(3):
            point[i] += directions[instruction][i]

    tile = tuple(point)
    if tile in black_tiles: black_tiles.remove(tile)
    else: black_tiles.add(tile)

print(len(black_tiles))

points = set()
for _ in range(100):
    old_black = deepcopy(black_tiles)
    black_tiles.clear()
    points.clear()

    for point in old_black:
        neighbor = list(point)
        for direction in directions.values():
            for i in range(3):
                neighbor[i] += direction[i]
            points.add(tuple(neighbor))
            neighbor = list(point)

    for point in points:
        active_neighbors = 0
        neighbor = list(point)
        for direction in directions.values():
            for i in range(3):
                neighbor[i] += direction[i]
            if tuple(neighbor) in old_black: active_neighbors += 1
            neighbor = list(point)

        if point in old_black:
            if active_neighbors == 1 or active_neighbors == 2: black_tiles.add(point)
        else:
            if active_neighbors == 2: black_tiles.add(point)

print(len(black_tiles))