inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
for line in inputLines:
    line = line.strip()
    input.append(int(line))

def silver(input):
    for i in range(25, len(input)):
        sum_found = 0
        number = input[i]
        for j in input[:i]:
            if sum_found: break
            for k in input[:i]:
                if j + k == number:
                    sum_found = 1
                    break
        
        if sum_found == 0:
            return number


    return "No solution"

def gold(input):
    previous_solution = 1398413738
    continous_sum = []
    for i in range(len(input)):
        continous_sum = []
        for j in input[i:]:
            continous_sum.append(j)
            sum = 0
            for k in continous_sum:
                sum += k
                if sum == previous_solution:
                    continous_sum.sort()
                    return continous_sum[0] + continous_sum[-1]
                elif sum > previous_solution:
                    break
    
    return "no solution"

print(silver(input))
print(gold(input))