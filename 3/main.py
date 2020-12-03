
inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
for line in inputLines:
    input.append(line.strip())

def silver(input):
    starting_index = 0
    trees_encountered = 0

    for i in range(len(input) - 1):
        line = input[i + 1]
        starting_index += 3

        if line[starting_index % len(input[0])] == '#':
            trees_encountered += 1

    return trees_encountered

def gold(input):
    starting_index = 0
    trees1 = 0
    trees2 = 0
    trees3 = 0
    trees4 = 0
    trees5 = 0

    for i in range(len(input) - 1):
        line = input[i + 1]
        starting_index += 3

        if line[starting_index % len(input[0])] == '#':
            trees1 += 1

    starting_index = 0

    for i in range(len(input) - 1):
        line = input[i + 1]
        starting_index += 1

        if line[starting_index % len(input[0])] == '#':
            trees2 += 1

    starting_index = 0

    for i in range(len(input) - 1):
        line = input[i + 1]
        starting_index += 5

        if line[starting_index % len(input[0])] == '#':
            trees3 += 1

    starting_index = 0

    for i in range(len(input) - 1):
        line = input[i + 1]
        starting_index += 7

        if line[starting_index % len(input[0])] == '#':
            trees4 += 1

    starting_index = 0

    i = 0
    while i < len(input) - 1:
        i += 2
        line = input[i]
        starting_index += 1

        if line[starting_index % len(input[0])] == '#':
            trees5 += 1

    return trees1 * trees2 * trees3 * trees4 * trees5

print(silver(input))
print(gold(input))