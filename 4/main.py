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

def validateRange(n, min, max):
    return True if min <= n <= max else False

def gold(input):
    validPassports = 0
    validYears = validHeight = validHairColor = validEyeColor = validPID = 0

    for passport in input:
        if (len(passport.keys()) == 8 or (len(passport.keys()) == 7 and 'cid' not in passport)):
            if validateRange(int(passport['byr']), 1920, 2002) and \
               validateRange(int(passport['iyr']), 2010, 2020) and \
               validateRange(int(passport['eyr']), 2020, 2030):
               validYears = 1
                
            if 'cm' in passport['hgt']:
                height = int(passport['hgt'].split('cm')[0])
                if validateRange(height, 150, 193):
                    validHeight = 1
            elif 'in' in passport['hgt']:
                height = int(passport['hgt'].split('in')[0])
                if validateRange(height, 59, 76):
                    validHeight = 1
                    
            validHairColor = 1 if '#' in passport['hcl'] else 0

            for color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                if passport['ecl'] == color:
                    validEyeColor = 1
                    break

            validPID = 1 if len(passport['pid']) == 9 else 0

            if validYears and validHeight and validHairColor and validEyeColor and validPID:
                validPassports += 1

            validYears = validHeight = validHairColor = validEyeColor = validPID = 0

    return validPassports

print(silver(input))
print(gold(input))