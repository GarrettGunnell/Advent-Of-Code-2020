
inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
for line in inputLines:
    line = line.strip()
    input.append(line)

def silver(input):
    answers = set()
    total_yes = 0
    for group in input:
        if group == '':
            total_yes += len(answers)
            answers.clear()
        for answer in group:
            answers.add(answer)

    
    return total_yes + len(answers)
        

def gold(input):
    answers = {}
    total = 0
    group_size = 0
    for group in input:
        if group == '':
            for key in answers:
                if answers[key] == group_size:
                    total += 1
            answers.clear()
            group_size = 0
        else:
            for answer in group:
                if answer in answers:
                    answers[answer] += 1
                else:
                    answers[answer] = 1
            group_size += 1
            
    for key in answers:
        if answers[key] == group_size:
            total += 1

    return total

print(silver(input))
print(gold(input))