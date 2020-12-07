
inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

bags = {}
bagsThatHaveGold = set()
for line in inputLines:
    line = line.strip().split()
    key = line[0] + ' ' + line[1]
    bags[key] = []
    for i in range(len(line)):
        if line[i].isdigit():
            color = line[i + 1] + ' ' + line[i + 2]
            if color == 'shiny gold':
                bagsThatHaveGold.add(key)
            elif color in bagsThatHaveGold:
                bagsThatHaveGold.add(key)

for line in inputLines:
    line = line.strip().split()
    key = line[0] + ' ' + line[1]
    for i in range(len(line)):
        if line[i].isdigit():
            color = line[i + 1] + ' ' + line[i + 2]
            if color == 'shiny gold':
                bagsThatHaveGold.add(key)
            elif color in bagsThatHaveGold:
                bagsThatHaveGold.add(key)

for line in inputLines:
    line = line.strip().split()
    key = line[0] + ' ' + line[1]
    for i in range(len(line)):
        if line[i].isdigit():
            color = line[i + 1] + ' ' + line[i + 2]
            if color == 'shiny gold':
                bagsThatHaveGold.add(key)
            elif color in bagsThatHaveGold:
                bagsThatHaveGold.add(key)

for line in inputLines:
    line = line.strip().split()
    key = line[0] + ' ' + line[1]
    for i in range(len(line)):
        if line[i].isdigit():
            color = line[i + 1] + ' ' + line[i + 2]
            if color == 'shiny gold':
                bagsThatHaveGold.add(key)
            elif color in bagsThatHaveGold:
                bagsThatHaveGold.add(key)

for line in inputLines:
    line = line.strip().split()
    key = line[0] + ' ' + line[1]
    for i in range(len(line)):
        if line[i].isdigit():
            color = line[i + 1] + ' ' + line[i + 2]
            if color == 'shiny gold':
                bagsThatHaveGold.add(key)
            elif color in bagsThatHaveGold:
                bagsThatHaveGold.add(key)

for line in inputLines:
    line = line.strip().split()
    key = line[0] + ' ' + line[1]
    for i in range(len(line)):
        if line[i].isdigit():
            color = line[i + 1] + ' ' + line[i + 2]
            if color == 'shiny gold':
                bagsThatHaveGold.add(key)
            elif color in bagsThatHaveGold:
                bagsThatHaveGold.add(key)


print(len(bagsThatHaveGold))