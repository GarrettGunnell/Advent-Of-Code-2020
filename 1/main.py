
inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
for line in inputLines:
    input.append(int(line.strip()))

def solution1(input):
    for i in input:
        for j in input:
            if (i + j == 2020):
                return i * j

def solution2(input):
    for i in input:
        for j in input:
            for k in input:
                if (i + j + k == 2020):
                    return i * j * k