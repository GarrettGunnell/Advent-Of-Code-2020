import math

inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
for line in inputLines:
    line = line.strip()
    input.append(line)

def silver(input):
    string = 'FBFBBFFRLR'
    row_range = [0, 127]
    col_range = [0, 7]
    highestID = 0
    for string in input:
        row_range = [0, 127]
        col_range = [0, 7]
        for i in range(7):
            char = string[i]
            if char == 'F':
                row_range[1] = math.floor((row_range[0] + row_range[1]) / 2)
            if char == 'B':
                row_range[0] = math.ceil((row_range[0] + row_range[1]) / 2)

        for i in range(7, 10):
            char = string[i]
            if char == 'L':
                col_range[1] = math.floor((col_range[0] + col_range[1]) / 2)
            if char == 'R':
                col_range[0] = math.ceil((col_range[0] + col_range[1]) / 2)
        
        passID = (row_range[0] * 8) + col_range[0]
        highestID = passID if passID > highestID else highestID
        row_range = [0, 127]
        col_range = [0, 7]

    return highestID

        

def gold(input):
    row_range = [0, 127]
    col_range = [0, 7]
    IDs = []
    for string in input:
        row_range = [0, 127]
        col_range = [0, 7]
        for i in range(7):
            char = string[i]
            if char == 'F':
                row_range[1] = math.floor((row_range[0] + row_range[1]) / 2)
            if char == 'B':
                row_range[0] = math.ceil((row_range[0] + row_range[1]) / 2)

        for i in range(7, 10):
            char = string[i]
            if char == 'L':
                col_range[1] = math.floor((col_range[0] + col_range[1]) / 2)
            if char == 'R':
                col_range[0] = math.ceil((col_range[0] + col_range[1]) / 2)
        
        passID = (row_range[0] * 8) + col_range[0]
        IDs.append(passID)
        row_range = [0, 127]
        col_range = [0, 7]

    IDs.sort()
    for i in IDs:
        if i + 1 not in IDs:
            return i + 1

print(silver(input))
print(gold(input))