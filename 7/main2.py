
inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
bags = {}

for line in inputLines:
    line = line.strip().split()
    key = line[0] + ' ' + line[1]
    bags[key] = []
    for i in range(len(line)):
        if line[i].isdigit():
            color = line[i + 1] + ' ' + line[i + 2]
            number = line[i]
            bags[key].append([color, number])

def add(key):
    values = 1
    for bag in bags[key]:
        values += int(bag[1]) * add(bag[0])

    return values


print(add('shiny gold') - 1)