import copy

inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
for line in inputLines:
    line = line.strip()
    input.append([line[0], int(line[1:])])

def silver(input):
    direction = 'E'
    x = 0
    y = 0
    for i in range(len(input)):
        instruction = input[i][0]
        value = input[i][1]
        if instruction == 'F':
            if direction == 'N':
                y += value
            elif direction == 'S':
                y -= value
            elif direction == 'W':
                x -= value
            elif direction == 'E':
                x += value
        elif instruction != 'R' and instruction != 'L':
            if instruction == 'N':
                y += value
            elif instruction == 'S':
                y -= value
            elif instruction == 'W':
                x -= value
            elif instruction == 'E':
                x += value
        else:
            for _ in range(value // 90):
                if direction == 'E':
                    direction = 'S' if instruction == 'R' else 'N'
                elif direction == 'S':
                    direction = 'W' if instruction == 'R' else 'E'
                elif direction == 'W':
                    direction = 'N' if instruction == 'R' else 'S'
                elif direction == 'N':
                    direction = 'E' if instruction == 'R' else 'W'

    return abs(x) + abs(y)

def gold(input):
    x = 0
    y = 0
    wayX = 10
    wayY = 1
    for i in range(len(input)):
        instruction = input[i][0]
        value = input[i][1]
        if instruction == 'F':
            x += wayX * value
            y += wayY * value
        elif instruction != 'R' and instruction != 'L':
            if instruction == 'N':
                wayY += value
            elif instruction == 'S':
                wayY -= value
            elif instruction == 'W':
                wayX -= value
            elif instruction == 'E':
                wayX += value
        else:
            for _ in range(value // 90):
                if instruction == 'R':
                    wayX, wayY = wayY, -wayX
                else:
                    wayY, wayX = wayX, -wayY

    return abs(x) + abs(y)

print(silver(input))
print(gold(input))
