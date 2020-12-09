import copy
inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
for line in inputLines:
    line = line.strip().split()
    input.append(line)

def silver(input):
    accumulator = 0
    instruction = 0
    executed_instructions = set()
    while True:
        if instruction in executed_instructions:
            break
        executed_instructions.add(instruction)
        instructions = input[instruction]
        command = instructions[0]
        sign = instructions[1][0]
        value = int(instructions[1][1:])
        if command == "acc":
            accumulator = accumulator + value if sign == '+' else accumulator - value
        elif command == "jmp":
            instruction = instruction + value if sign == '+' else instruction - value
            continue

        instruction += 1

    return accumulator

def execute(program):
    accumulator = 0
    instruction = 0
    executed_instructions = set()
    while True:
        if instruction == len(program):
            return accumulator
        if instruction in executed_instructions:
            return False
        executed_instructions.add(instruction)
        instructions = program[instruction]
        command = instructions[0]
        sign = instructions[1][0]
        value = int(instructions[1][1:])
        if command == "acc":
            accumulator = accumulator + value if sign == '+' else accumulator - value
        elif command == "jmp":
            instruction = instruction + value if sign == '+' else instruction - value
            continue

        instruction += 1

    return accumulator

def gold(input):
    jumps = [i for i in range(len(input)) if input[i][0] == "jmp"]
    nopes = [i for i in range(len(input)) if input[i][0] == "nop"]
    for i in jumps:
        input_copy = copy.deepcopy(input)
        input_copy[i][0] = "nop"
        accumulator = execute(input_copy)
        if accumulator != False:
            return accumulator
    
    for i in nopes:
        input_copy = copy.deepcopy(input)
        input_copy[i][0] = "jmp"
        accumulator = execute(input_copy)
        if accumulator != False:
            return accumulator

    return "No Solution Found"

print(silver(input))
print(gold(input))