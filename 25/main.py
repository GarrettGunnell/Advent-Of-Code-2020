inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

card_key = int(inputLines[0].strip())
door_key = int(inputLines[1].strip())

subject_number = 7
value = 1

loop_number = 0
while value != card_key:
    value *= subject_number
    value = value % 20201227
    loop_number += 1

subject_number = door_key
value = 1
for _ in range(loop_number):
    value *= subject_number
    value = value % 20201227

print(value)