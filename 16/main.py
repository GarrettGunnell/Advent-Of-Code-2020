inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
classes = {}
for line in inputLines:
    fields = True
    my_ticket = 0
    nearby_tickets = 0
    line = line.strip()

    if line == '':
        if fields:
            fields = False
            my_ticket = 1
        elif my_ticket == 1:
            my_ticket = 0
            nearby_tickets = 1

    elif fields:
        line = line.split()
        if len(line) == 5: field = line[0] + ' ' + line[1][:-1]
        elif len(line) != 0: field = line[0][:-1]

    input.append(line)

for i in range(0, 20):
    line = inputLines[i].strip().split()
    if len(line) == 5: 
        field = line[0] + ' ' + line[1][:-1]
        firstfield = line[2].split('-')
        secondfield = line[4].split('-')
        classes[field] = [[int(firstfield[0]), int(firstfield[1])], [int(secondfield[0]), int(secondfield[1])]]
    elif len(line) != 0: 
        field = line[0][:-1]
        firstfield = line[1].split('-')
        secondfield = line[3].split('-')
        classes[field] = [[int(firstfield[0]), int(firstfield[1])], [int(secondfield[0]), int(secondfield[1])]]

my_ticket = [int(i) for i in inputLines[22].strip().split(',')]

tickets = []
for i in range(25, len(inputLines)):
    tickets.append(inputLines[i].strip().split(','))

error_num = 0
invalid_tickets = set()
for i in range(len(tickets)):
    valid = 0
    for field in tickets[i]:
        valid = 0
        for key in classes:
            minfieldone = classes[key][0][0]
            maxfieldone = classes[key][0][1]
            minfieldtwo = classes[key][1][0]
            maxfieldtwo = classes[key][1][1]
            if minfieldone <= int(field) <= maxfieldone or minfieldtwo <= int(field) <= maxfieldtwo:
                valid = 1
                break
        
        if not valid:
            invalid_tickets.add(i)
            error_num += int(field)

print(error_num)
order = {}
potential_fields = {}
for key in classes:
    minfieldone = classes[key][0][0]
    maxfieldone = classes[key][0][1]
    minfieldtwo = classes[key][1][0]
    maxfieldtwo = classes[key][1][1]

    for i in range(len(tickets[0])):
        field_found = 1
        for j in range(len(tickets)):
            if j in invalid_tickets: 
                continue
            field = int(tickets[j][i])
            if minfieldone <= field <= maxfieldone or minfieldtwo <= field <= maxfieldtwo:
                continue
            else:
                field_found = 0
                break

        if field_found:
            if key in potential_fields: potential_fields[key].append(i)
            else: potential_fields[key] = [i]

def fields_found():
    for key in potential_fields:
        if len(potential_fields[key]) != 1: return False
    return True

while not fields_found():
    for key in potential_fields:
        if len(potential_fields[key]) == 1:
            field_index = potential_fields[key][0]
            for field in potential_fields:
                if field == key: continue
                if field_index in potential_fields[field]:
                    potential_fields[field].remove(field_index)

for key in potential_fields: order[key] = potential_fields[key][0]
        
print(my_ticket[order['departure location']] \
      * my_ticket[order['departure station']] \
      * my_ticket[order['departure platform']] \
      * my_ticket[order['departure track']] \
      * my_ticket[order['departure date']] \
      * my_ticket[order['departure time']])