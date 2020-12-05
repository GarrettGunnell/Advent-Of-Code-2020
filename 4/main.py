inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
passport = {}
for line in inputLines:
    if line == '\n':
        input.append(passport)
        passport = {}
        continue

    line = line.strip().split()
    for i in line:
        i = i.split(':')
        passport[i[0]] = i[1]
input.append(passport)

def silver(input):
    validPassports = 0
    for passport in input:
        if (len(passport.keys()) == 8):
            validPassports += 1
        elif (len(passport.keys()) == 7 and 'cid' not in passport):
            validPassports += 1

    return validPassports

def gold(input):
    validPassports = 0

    for passport in input:
        if (len(passport.keys()) == 8 or (len(passport.keys()) == 7 and 'cid' not in passport)):
            birthYear = int(passport['byr'])
            initialYear = int(passport['iyr'])
            endYear = int(passport['eyr'])
            height = passport['hgt']
            hairColor = passport['hcl']
            eyeColor = passport['ecl']
            pid = passport['pid']

            if birthYear < 1920 or 2002 < birthYear or \
               initialYear < 2010 or 2020 < initialYear or \
               endYear < 2020 or 2030 < endYear:
                continue

            if 'cm' not in height and 'in' not in height: continue
                
            if 'cm' in height:
                height = int(height.split('cm')[0])
                if height < 150 or 193 < height:
                    continue
            elif 'in' in height:
                height = int(height.split('in')[0])
                if height < 59 or 76 < height:
                    continue
                    
            if '#' not in hairColor: continue

            if eyeColor not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                continue

            if len(pid) != 9: continue

            validPassports += 1

    return validPassports

print(silver(input))
print(gold(input))