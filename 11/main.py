import copy

inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
for line in inputLines:
    line = line.strip()
    input.append([char for char in line])

def silver(input):
    previous_iteration = input
    while True:
        next_iteration = copy.deepcopy(previous_iteration)
        for row in range(len(input)):
            for s in range(len(previous_iteration[row])):
                occupied_neighbors = 0
                seat = previous_iteration[row][s]
                if seat == '.': continue
                if row == 0 or row == len(input) - 1:
                    if s == 0 or s == len(previous_iteration[row]) - 1:
                        if seat == 'L':
                            next_iteration[row][s] = '#'
                    else:
                        if row == 0:
                            if previous_iteration[row][s - 1] == '#': occupied_neighbors += 1
                            if previous_iteration[row][s + 1] == '#': occupied_neighbors += 1
                            if previous_iteration[row + 1][s - 1] == '#': occupied_neighbors += 1
                            if previous_iteration[row + 1][s] == '#': occupied_neighbors += 1
                            if previous_iteration[row + 1][s + 1] == '#': occupied_neighbors += 1

                            if seat == '#' and occupied_neighbors >= 4:
                                next_iteration[row][s] = 'L'
                            elif seat == 'L' and occupied_neighbors == 0:
                                next_iteration[row][s] = '#'
                        else:
                            if previous_iteration[row - 1][s - 1] == '#': occupied_neighbors += 1
                            if previous_iteration[row - 1][s] == '#': occupied_neighbors += 1
                            if previous_iteration[row - 1][s + 1] == '#': occupied_neighbors += 1
                            if previous_iteration[row][s - 1] == '#': occupied_neighbors += 1
                            if previous_iteration[row][s + 1] == '#': occupied_neighbors += 1

                            if seat == '#' and occupied_neighbors >= 4:
                                next_iteration[row][s] = 'L'
                            elif seat == 'L' and occupied_neighbors == 0:
                                next_iteration[row][s] = '#'

                elif s == 0:
                    if previous_iteration[row - 1][0] == '#': occupied_neighbors += 1
                    if previous_iteration[row - 1][1] == '#': occupied_neighbors += 1
                    if previous_iteration[row][1] == '#': occupied_neighbors += 1
                    if previous_iteration[row + 1][1] == '#': occupied_neighbors += 1
                    if previous_iteration[row + 1][0] == '#': occupied_neighbors += 1

                    if seat == '#' and occupied_neighbors >= 4:
                        next_iteration[row][s] = 'L'
                    elif seat == 'L' and occupied_neighbors == 0:
                        next_iteration[row][s] = '#'
                elif s == len(previous_iteration[row]) - 1:
                    if previous_iteration[row - 1][-1] == '#': occupied_neighbors += 1
                    if previous_iteration[row - 1][-2] == '#': occupied_neighbors += 1
                    if previous_iteration[row][-2] == '#': occupied_neighbors += 1
                    if previous_iteration[row + 1][-2] == '#': occupied_neighbors += 1
                    if previous_iteration[row + 1][-1] == '#': occupied_neighbors += 1

                    if seat == '#' and occupied_neighbors >= 4:
                        next_iteration[row][s] = 'L'
                    elif seat == 'L' and occupied_neighbors == 0:
                        next_iteration[row][s] = '#'

                else:
                    if previous_iteration[row - 1][s - 1] == '#': occupied_neighbors += 1
                    if previous_iteration[row - 1][s] == '#': occupied_neighbors += 1
                    if previous_iteration[row - 1][s + 1] == '#': occupied_neighbors += 1
                    if previous_iteration[row][s - 1] == '#': occupied_neighbors += 1
                    if previous_iteration[row][s + 1] == '#': occupied_neighbors += 1
                    if previous_iteration[row + 1][s - 1] == '#': occupied_neighbors += 1
                    if previous_iteration[row + 1][s] == '#': occupied_neighbors += 1
                    if previous_iteration[row + 1][s + 1] == '#': occupied_neighbors += 1

                    if seat == '#' and occupied_neighbors >= 4:
                        next_iteration[row][s] = 'L'
                    elif seat == 'L' and occupied_neighbors == 0:
                        next_iteration[row][s] = '#'
        
        if previous_iteration == next_iteration:
            break
        
        previous_iteration = copy.deepcopy(next_iteration)

    num_occupied = 0
    for row in previous_iteration:
        for seat in row:
            if seat == '#': num_occupied += 1

    return num_occupied


def find_upperleft(seats, row, s):
    seat = ''
    while True:
        try:
            if seat == 'L' or seat == '#':
                break
            seat = seats[row - 1][s - 1]
            row -= 1
            s -= 1
            if row < 0 or s < 0:
                break
        except:
            break

    return seat

def find_upper(seats, row, s):
    seat = ''
    while True:
        try:
            if seat == 'L' or seat == '#':
                break
            seat = seats[row - 1][s]
            row -= 1
            if row < 0 or s < 0:
                break
        except:
            break

    return seat

def find_upperright(seats, row, s):
    seat = ''
    while True:
        try:
            if seat == 'L' or seat == '#':
                break
            seat = seats[row - 1][s + 1]
            row -= 1
            s += 1
            if row < 0 or s < 0:
                break
        except:
            break

    return seat

def find_left(seats, row, s):
    seat = ''
    while True:
        try:
            if seat == 'L' or seat == '#':
                break
            seat = seats[row][s - 1]
            s -= 1
            if s < 0:
                break
        except:
            break

    return seat

def find_right(seats, row, s):
    seat = ''
    while True:
        try:
            if seat == 'L' or seat == '#':
                break
            seat = seats[row][s + 1]
            s += 1
        except:
            break

    return seat

def find_lowerleft(seats, row, s):
    seat = ''
    while True:
        try:
            if seat == 'L' or seat == '#':
                break
            seat = seats[row + 1][s - 1]
            row += 1
            s -= 1
            if s < 0:
                break
        except:
            break

    return seat

def find_lower(seats, row, s):
    seat = ''
    while True:
        try:
            if seat == 'L' or seat == '#':
                break
            seat = seats[row + 1][s]
            row += 1
        except:
            break

    return seat

def find_lowerright(seats, row, s):
    seat = ''
    while True:
        try:
            if seat == 'L' or seat == '#':
                break
            seat = seats[row + 1][s + 1]
            row += 1
            s += 1
        except:
            break

    return seat

def gold(input):
    previous_iteration = input
    while True:
        next_iteration = copy.deepcopy(previous_iteration)
        for row in range(len(input)):
            for s in range(len(previous_iteration[row])):
                occupied_neighbors = 0
                seat = previous_iteration[row][s]
                if seat == '.': continue
                if row == 0 or row == len(input) - 1:
                    if s == 0 or s == len(previous_iteration[row]) - 1:
                        if seat == 'L':
                            next_iteration[row][s] = '#'
                    else:
                        if row == 0:
                            if find_left(previous_iteration, row, s) == '#': occupied_neighbors += 1
                            if find_right(previous_iteration, row, s) == '#': occupied_neighbors += 1
                            if find_lowerleft(previous_iteration, row, s) == '#': occupied_neighbors += 1
                            if find_lower(previous_iteration, row, s) == '#': occupied_neighbors += 1
                            if find_lowerright(previous_iteration, row, s) == '#': occupied_neighbors += 1

                            if seat == '#' and occupied_neighbors >= 5:
                                next_iteration[row][s] = 'L'
                            elif seat == 'L' and occupied_neighbors == 0:
                                next_iteration[row][s] = '#'
                        else:
                            if find_upperleft(previous_iteration, row, s) == '#': occupied_neighbors += 1
                            if find_upper(previous_iteration, row, s) == '#': occupied_neighbors += 1
                            if find_upperright(previous_iteration, row, s) == '#': occupied_neighbors += 1
                            if find_left(previous_iteration, row, s) == '#': occupied_neighbors += 1
                            if find_right(previous_iteration, row, s) == '#': occupied_neighbors += 1

                            if seat == '#' and occupied_neighbors >= 5:
                                next_iteration[row][s] = 'L'
                            elif seat == 'L' and occupied_neighbors == 0:
                                next_iteration[row][s] = '#'

                elif s == 0:
                    if find_upper(previous_iteration, row, s) == '#': occupied_neighbors += 1
                    if find_upperright(previous_iteration, row, s) == '#': occupied_neighbors += 1
                    if find_right(previous_iteration, row, s) == '#': occupied_neighbors += 1
                    if find_lower(previous_iteration, row, s) == '#': occupied_neighbors += 1
                    if find_lowerright(previous_iteration, row, s) == '#': occupied_neighbors += 1

                    if seat == '#' and occupied_neighbors >= 5:
                        next_iteration[row][s] = 'L'
                    elif seat == 'L' and occupied_neighbors == 0:
                        next_iteration[row][s] = '#'
                elif s == len(previous_iteration[row]) - 1:
                    if find_upperleft(previous_iteration, row, s) == '#': occupied_neighbors += 1
                    if find_upper(previous_iteration, row, s) == '#': occupied_neighbors += 1
                    if find_left(previous_iteration, row, s) == '#': occupied_neighbors += 1
                    if find_lowerleft(previous_iteration, row, s) == '#': occupied_neighbors += 1
                    if find_lower(previous_iteration, row, s) == '#': occupied_neighbors += 1

                    if seat == '#' and occupied_neighbors >= 5:
                        next_iteration[row][s] = 'L'
                    elif seat == 'L' and occupied_neighbors == 0:
                        next_iteration[row][s] = '#'

                else:
                    if find_upperleft(previous_iteration, row, s) == '#': occupied_neighbors += 1
                    if find_upper(previous_iteration, row, s) == '#': occupied_neighbors += 1
                    if find_upperright(previous_iteration, row, s) == '#': occupied_neighbors += 1
                    if find_left(previous_iteration, row, s) == '#': occupied_neighbors += 1
                    if find_right(previous_iteration, row, s) == '#': occupied_neighbors += 1
                    if find_lowerleft(previous_iteration, row, s) == '#': occupied_neighbors += 1
                    if find_lower(previous_iteration, row, s) == '#': occupied_neighbors += 1
                    if find_lowerright(previous_iteration, row, s) == '#': occupied_neighbors += 1

                if seat == '#' and occupied_neighbors >= 5:
                    next_iteration[row][s] = 'L'
                elif seat == 'L' and occupied_neighbors == 0:
                    next_iteration[row][s] = '#'

        if previous_iteration == next_iteration:
            break
        
        previous_iteration = copy.deepcopy(next_iteration)

    num_occupied = 0
    for row in previous_iteration:
        for seat in row:
            if seat == '#': num_occupied += 1

    return num_occupied

print(silver(input))
print(gold(input))