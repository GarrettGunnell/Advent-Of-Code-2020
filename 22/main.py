from copy import deepcopy

inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

player_one_deck = []
player_two_deck = []
player_one = True
for line in inputLines[1:]:
    line = line.strip()
    if "Player" in line:
        player_one = False
        continue
    if line == '': continue
    if player_one:
        player_one_deck.append(line)
    else:
        player_two_deck.append(line)

def recursive_combat(p1_deck, p2_deck):
    seen = set()

    while len(p1_deck) != 0 and len(p2_deck) != 0:
        game_state = (p1_deck, p2_deck)
        if game_state in seen:
            return [1, p1_deck]
        seen.add(game_state)

        one_draw = int(p1_deck[0])
        two_draw = int(p2_deck[0])
        p1_deck = p1_deck[1:]
        p2_deck = p2_deck[1:]

        if one_draw <= len(p1_deck) and two_draw <= len(p2_deck):
            result = recursive_combat(p1_deck[:one_draw],  p2_deck[:two_draw])
            if result[0] == 1:
                p1_deck = p1_deck + (one_draw, two_draw)
            else:
                p2_deck = p2_deck + (two_draw, one_draw)
        else:
            if one_draw > two_draw:
                p1_deck = p1_deck + (one_draw, two_draw)
            else:
                p2_deck = p2_deck + (two_draw, one_draw)

    return [1, p1_deck] if len(p1_deck) != 0 else [2, p2_deck]

result = recursive_combat(tuple(player_one_deck), tuple(player_two_deck))

deck = list(result[1])
deck.reverse()

result = 0
i = 0
while i < len(deck):
    i += 1
    result += i * int(deck[i - 1])

print(result)