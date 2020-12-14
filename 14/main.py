inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
for line in inputLines:
    line = line.strip()
    input.append(line.split())

def silver(input):
    mask = ''
    memory = {}
    for line in input:
        if line[0] == 'mask':
            mask = line[2]
        else:
            binary = str(bin(int(line[2])))[2:].rjust(36, '0')
            output = ''
            for i in range(len(mask)):
                output = output + binary[i] if mask[i] == 'X' else output + mask[i]

            address = ''
            for i in range(4, len(line[0])):
                if line[0][i] == ']': break
                else: address += line[0][i]

            memory[int(address)] = int(output, 2)

    return sum(memory.values())

def gold(input):
    mask = ''
    memory = {}
    for line in input:
        if line[0] == 'mask':
            mask = line[2]
        else:
            address = ''
            for i in range(4, len(line[0])):
                if line[0][i] == ']': break
                else: address += line[0][i]
            
            address = str(bin(int(address)))[2:].rjust(36, '0')
            addresses = ['']
            for i in range(len(mask)):
                if mask[i] == 'X':
                    for j in range(len(addresses)):
                        addresses.append(addresses[j] + '1')
                        addresses[j] += '0'
                elif mask[i] == '0':
                    for j in range(len(addresses)):
                        addresses[j] += address[i]
                elif mask[i] == '1':
                    for j in range(len(addresses)):
                        addresses[j] += '1'

            for i in addresses:
                memory[int(i, 2)] = int(line[2])

    return sum(memory.values())

print(silver(input))
print(gold(input))


