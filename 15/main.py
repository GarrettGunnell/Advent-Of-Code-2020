inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
for line in inputLines:
    line = line.strip().split(',')
    for i in line:
        input.append(int(i))

def silver(input):
    spoken = {}
    turn = 0
    last_spoken = 0
    last_difference = 0

    for num in input:
        turn += 1
        spoken[num] = turn
        last_spoken = num

    while turn != 2020:
        turn += 1
        last_spoken = last_difference
        last_difference = turn - spoken[last_spoken] if last_spoken in spoken else 0
        spoken[last_spoken] = turn

    return last_spoken

def gold(input):
    spoken = {}
    turn = 0
    last_spoken = 0
    last_difference = 0

    for num in input:
        turn += 1
        spoken[num] = turn
        last_spoken = num

    while turn != 30000000:
        turn += 1
        last_spoken = last_difference
        last_difference = turn - spoken[last_spoken] if last_spoken in spoken else 0
        spoken[last_spoken] = turn

    return last_spoken

print(silver(input))
print(gold(input))
