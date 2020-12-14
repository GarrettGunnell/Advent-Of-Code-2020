import copy
from remainder import chinese_remainder

inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
for line in inputLines:
    line = line.strip()
    input.append(line.split(','))

def silver(input):
    busID = int(input[0][0])
    schedule = input[1:]
    times = []
    
    for i in schedule[0]:
        if i == 'x':
            continue
        departure = 0
        while departure <= int(busID):
            departure += int(i)

        times.append([departure, int(i)])

    minTime = times[0][0]
    minID = times[0][1]
    for i in times:
        time = i[0]
        if time < minTime:
            minTime = time
            minID = i[1]

    return (minTime - busID) * minID

def gold(input):
    schedule = input[1:][0]
    IDs = []
    times = []

    for i in range(len(schedule)):
        bus = schedule[i]
        if bus == 'x': continue
        IDs.append(int(bus))
        times.append(-i)

    print(chinese_remainder(IDs, times))

print(silver(input))
print(gold(input))


