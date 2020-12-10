inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
for line in inputLines:
    line = line.strip()
    input.append(int(line))

input.sort()

def silver(input):
    return len([i for i in range(len(input)) if input[i] - input[i - 1] == 1]) * len([i for i in range(len(input)) if input[i] - input[i - 1] == 3])

def gold(input):
    known = {0:1}
    for i in range(len(input)):
        adapter = input[i]
        diffof1 = adapter - 1
        diffof2 = adapter - 2
        diffof3 = adapter - 3

        if adapter not in known:
            known[adapter] = 0
        if diffof1 not in known:
            known[diffof1] = 0
        if diffof2 not in known:
            known[diffof2] = 0
        if diffof3 not in known:
            known[diffof3] = 0

        known[adapter] += known[diffof1] + known[diffof2] + known[diffof3] 

    return known[input[-1]]

print(input)
print(silver(input))
print(gold(input))