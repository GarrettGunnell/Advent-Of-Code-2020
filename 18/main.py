inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

def find_parenthesis(problem, input):
    i = 0
    string = []
    while i < len(input):
        char = input[i]
        if char == ' ':
            i += 1
            continue
        elif char == '(':
            i += find_parenthesis(string, input[i + 1:])
        elif char == ')':
            problem.append(string)
            return i + 2
        else:
            string.append(char)
            i += 1

input = []
for line in inputLines:
    line = line.strip()
    problem = []
    i = 0
    while i < len(line):
        char = line[i]
        if char == ' ':
            i += 1
            continue
        elif char == '(':
            i += find_parenthesis(problem, line[i + 1:])
        else:
            problem.append(char)
            i += 1

    input.append(problem)

def solve(problem):
    operator = ''
    answer = 0
    if isinstance(problem[0], list):
        answer = solve(problem[0])
    else:
        answer = int(problem[0])

    for i in range(1, len(problem)):
        element = problem[i]

        if isinstance(element, list):
            answer = answer + solve(element) if operator == '+' else answer * solve(element)
        elif element.isdigit():
            answer = answer + int(element) if operator == '+' else answer * int(element)
        else:
            operator = element

    return answer

def silver(input):
    result = 0

    for problem in input:
        result += solve(problem)

    return result

def parseAddition(problem):
    for i in range(len(problem)):
        if isinstance(problem[i], list):
            problem[i] = parseAddition(problem[i])

    while '+' in problem:
        for i in range(len(problem)):
            if problem[i] == '+':
                result = solveWithPriority(problem[i - 1]) + solveWithPriority(problem[i + 1])
                problem[i - 1:i + 2] = [result]
                break

    return problem

def solveWithPriority(problem):
    operator = ''
    answer = 0
    if not isinstance(problem, list):
        return int(problem)

    if isinstance(problem[0], list):
        answer = solveWithPriority(problem[0])
    else:
        answer = int(problem[0])

    for i in range(1, len(problem)):
        element = problem[i]

        if isinstance(element, list):
            sub_answer = solveWithPriority(parseAddition(element))
            answer = answer + sub_answer if operator == '+' else answer * sub_answer
        elif element != '+' and element != '*':
            answer = answer + int(element) if operator == '+' else answer * int(element)
        else:
            operator = element

    return answer


def gold(input):
    result = 0

    for problem in input:
        result += solveWithPriority(parseAddition(problem))
            
    return result

print(silver(input))
print(gold(input))


