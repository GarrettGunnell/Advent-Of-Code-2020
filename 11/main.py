import copy

inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
for line in inputLines:
    line = line.strip()
    input.append([char for char in line])

def sample_neighbor(seats, r, s, x, y):
    return seats[r + y][s + x] if 0 <= r + y < len(seats) and 0 <= s + x < len(seats[0]) else None

def sample_nearest(seats, r, s, x, y):
    rownum = r + y
    seatnum = s + x
    while 0 <= rownum < len(seats) and 0 <= seatnum < len(seats[0]):
        if seats[rownum][seatnum] != '.': return seats[rownum][seatnum]

        rownum += y
        seatnum += x

def solution(input, part):
    sampler = sample_neighbor if part == 1 else sample_nearest
    previous_iteration = input
    while True:
        next_iteration = copy.deepcopy(previous_iteration)
        for r in range(len(input)):
            for s in range(len(previous_iteration[r])):
                num_occupied = 0
                seat = previous_iteration[r][s]
                if seat == '.': continue
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if (x == 0 and y == 0): continue
                        if sampler(previous_iteration, r, s, x, y) == '#': num_occupied += 1

                if seat == '#' and num_occupied >= 3 + part:
                    next_iteration[r][s] = 'L'
                elif seat == 'L' and num_occupied == 0:
                    next_iteration[r][s] = '#'

        if previous_iteration == next_iteration: break
        previous_iteration = copy.deepcopy(next_iteration)

    num_occupied = 0
    for row in previous_iteration: num_occupied += row.count('#')

    return num_occupied