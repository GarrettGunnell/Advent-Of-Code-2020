import random

inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
for line in inputLines:
    line = line.strip()
    input.append(int(line))

while True:
    start = random.randint(0, len(input) - 1)
    end = random.randint(start, len(input) - 1)
    if len(input[start:end]) < 2: continue
    if sum(input[start:end]) == 1398413738:
        exit(print(min(input[start:end]) + max(input[start:end])))