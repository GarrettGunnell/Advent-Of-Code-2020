from copy import deepcopy

inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

iterations = 0
points = set()
active = set()

for y in range(len(inputLines)):
    line = inputLines[y].strip()
    for x in range(len(line)):
        if line[x] == '#': active.add((x, y, 0, 0))

while iterations < 6:
    old_active = deepcopy(active)
    active.clear()
    points.clear()

    for point in old_active:
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    for w in range(-1, 2):
                        p = (point[0] + x, point[1] + y, point[2] + z, point[3] + w)
                        points.add(p)

    for point in points:
        active_neighbors = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    for w in range(-1, 2):
                        if x == 0 and y == 0 and z == 0 and w == 0: continue
                        p = (point[0] + x, point[1] + y, point[2] + z, point[3] + w)
                        if p in old_active: active_neighbors += 1

        if point in old_active:
            if active_neighbors == 2 or active_neighbors == 3: active.add(point)
        else:
            if active_neighbors == 3: active.add(point)

    iterations += 1

print(len(active))