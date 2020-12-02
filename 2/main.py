
inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
for line in inputLines:
    splitLine = line.strip().split()
    minmax = splitLine[0].split('-')
    permittedCharacter = splitLine[1].split(':')
    inputArray = []
    inputArray.append(minmax[0])
    inputArray.append(minmax[1])
    inputArray.append(permittedCharacter[0])
    inputArray.append(splitLine[2])
    input.append(inputArray)

def solution(input):
    numValid = 0
    for i in input:
        minAppearances = i[0]
        maxAppearances = i[1]
        character = i[2]
        password = i[3]
        numAppearances = 0

        for j in password:
            if j == character:
                numAppearances += 1
            
        if numAppearances < int(minAppearances) or numAppearances > int(maxAppearances):
            continue
        else:
            numValid += 1
    
    return numValid

def solution2(input):
    numValid = 0
    for i in input:
        firstIndex = i[0]
        secondIndex = i[1]
        character = i[2]
        password = i[3]

        if password[int(firstIndex) - 1] == character and password[int(secondIndex) - 1] == character:
            continue

        if password[int(firstIndex) - 1] == character or password[int(secondIndex) - 1] == character:
            numValid += 1

    return numValid