import re

inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
rules = {}
rules_parsing = 1
for line in inputLines:
    line = line.strip()
    if line == '':
        rules_parsing = 0
    elif rules_parsing:
        line = line.split()
        rules[line[0][:-1]] = line[1:]
    else:
        input.append(line)

regex = ''
def parse(rule):
    global regex
    if rule == "106" or rule == "65":
        regex = regex + "a" if rule == "106" else regex + "b"
    else:
        regex += '('
        for r in rules[rule]:
            if r == '|':
                regex += '|'
            else:
                parse(r) 
        regex += ')'

for r in rules['0']:
    parse(r)

pattern = re.compile('^' + regex + '$')
num_matches = 0

for message in input:
    if bool(pattern.match(message)):
        num_matches += 1

print(num_matches)