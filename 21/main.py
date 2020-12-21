from copy import deepcopy

inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
ingredients = set()
allergens = set()
all_allergens = set()
allergen_assignments = {}
for line in inputLines:
    ingredients.clear()
    allergens.clear()
    line = line.strip().split(' (contains ')
    for ingredient in line[0].split():
        ingredients.add(ingredient)
    for allergen in line[1].split():
        allergens.add(allergen[:-1])
        all_allergens.add(allergen[:-1])
        allergen_assignments[allergen[:-1]] = set()

    input.append([deepcopy(ingredients), deepcopy(allergens)])

for allergen in all_allergens:
    allergen_assignments[allergen] = set.intersection(*(ingredients for (ingredients, allergens) in input if allergen in allergens))

possible_allergens = set.union(*allergen_assignments.values())

num_safe_ingredients = 0
for data in input:
    num_safe_ingredients += len(data[0] - possible_allergens)

print(num_safe_ingredients)

found_allergens = set()
while True:
    for allergen in allergen_assignments.values():
        if len(allergen) == 1: found_allergens.add(*allergen)

    if len(found_allergens) == len(allergen_assignments): break

    for possibilities in allergen_assignments.values():
        if len(possibilities) != 1:
            possibilities -= found_allergens

ingredient_list = ''
for ingredient in sorted(allergen_assignments.items()):
    ingredient_list += ''.join(ingredient[1]) + ','

print(ingredient_list[:-1])