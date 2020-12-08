import copy
import random

inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
for line in inputLines:
    line = line.strip().split()
    input.append(line)

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

accumulator = False
while accumulator == False:
    input_copy = copy.deepcopy(input)
    random_index = random.randint(0, len(input) - 1)
    command = input_copy[random_index][0]
    if command == "jmp":
        input_copy[random_index][0] = "nop"
    elif command == "nop":
        input_copy[random_index][0] = "jmp"
    else:
        continue

    accumulator = execute(input_copy)

print(accumulator)
