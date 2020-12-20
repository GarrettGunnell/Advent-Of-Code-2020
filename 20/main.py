from copy import deepcopy
import re

inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

def pretty_print(tile):
    for row in tile:
        string = ''
        for col in row:
            string += col
        print(string)

def getLeftSide(tile):
    side = ''
    for row in tile:
        side += row[0]

    return side

def getRightSide(tile):
    side = ''
    for row in tile:
        side += row[-1]

    return side

def getSides(tile):
    return [''.join(tile[0]), getLeftSide(tile), getRightSide(tile), ''.join(tile[-1])]

def reverse_tile(tile):
    for row in range(len(tile)):
        tile[row] = tile[row][::-1]

def rotate(tile):
    return list(zip(*tile[::-1]))

def orientations(tile):
    origin = deepcopy(tile)
    permutations = []
    for _ in range(4):
        origin = rotate(origin)
        permutations.append(deepcopy(origin))

    reverse_tile(origin)
    for _ in range(4):
        origin = rotate(origin)
        permutations.append(deepcopy(origin))

    return permutations

def isMatching(tiles1, tiles2):
    for tile1 in tiles1:
        for tile2 in tiles2:
            sides = getSides(tile2)
            for side in getSides(tile1):
                if side in sides: return side

    return False

def matchesLeft(tile1, tile2):
    return True if getLeftSide(tile1) == getRightSide(tile2) else False 

def matchesRight(tile1, tile2):
    return True if getRightSide(tile1) == getLeftSide(tile2) else False 

def matchesTop(tile1, tile2):
    return True if ''.join(tile1[0]) == ''.join(tile2[-1]) else False 

def matchesBottom(tile1, tile2):
    return True if ''.join(tile1[-1]) == ''.join(tile2[0]) else False 
    

tiles = {}
tile_matches = {}
curr_tile = ''
for line in inputLines:
    line = line.strip()
    if 'Tile' in line:
        curr_tile = line[5:-1]
        tiles[curr_tile] = []
        tile_matches[curr_tile] = set()
    elif line != '':
        tiles[curr_tile].append(tuple(line))

for key in tiles.keys():
    tiles[key] = orientations(tiles[key])

for i in tiles.keys():
    for j in tiles.keys():
        if i == j: continue
        if isMatching(tiles[i], tiles[j]): tile_matches[i].add(j)

corner_tiles = []
for key in tile_matches.keys():
    if len(tile_matches[key]) == 2: corner_tiles.append(key)

top_left_corner = corner_tiles[1]
tile_orientations = {}
tile_orientations[top_left_corner] = tiles[top_left_corner][3]

board = [[top_left_corner]]
curr_tile = top_left_corner
while len(board) != 12:
    successor_found = False
    for j in tile_matches[curr_tile]:
        if successor_found: break
        for tile in tiles[j]:
            if matchesBottom(tile_orientations[curr_tile], tile): 
                board.append([j])
                tile_orientations[j] = tile
                curr_tile = j
                successor_found = True
                break

for i in range(12):
    curr_tile = board[i][0]
    while len(board[i]) != 12:
        successor_found = False
        for j in tile_matches[curr_tile]:
            if successor_found: break
            for tile in tiles[j]:
                if matchesRight(tile_orientations[curr_tile], tile): 
                    board[i].append(j)
                    tile_orientations[j] = tile
                    curr_tile = j
                    successor_found = True
                    break

for key in tile_orientations:
    tile_orientations[key] = tile_orientations[key][1:-1]
    for row in range(len(tile_orientations[key])):
        tile_orientations[key][row] = tile_orientations[key][row][1:-1]

board_image = []
for row in board:
    for i in range(len(tile_orientations[top_left_corner])):
        string = ''
        for col in row:
            tile = tile_orientations[col]
            for char in tile[i]:
                string += char
        board_image.append(string)

f = open("image.txt", "w")
for row in board_image:
    f.write(''.join(row) + '\n')
f.close()

imageFile = open('image.txt', 'r')
imageLines = imageFile.readlines()

board_image = []
for line in imageLines:
    board_image.append(line.strip())

for row in range(len(board_image)):
    board_image[row] = board_image[row][::-1]

monstertop = re.compile('..................#.')
monstermid = re.compile('#....##....##....###')
monsterlow = re.compile('.#..#..#..#..#..#...')

num_monsters = 0
for i in range(1, len(board_image) - 1):
    for j in range(len(board_image[0]) - 20):
        topsli = ''.join(board_image[i - 1][j:j + 20])
        midsli = ''.join(board_image[i][j:j + 20])
        bottomsli = ''.join(board_image[i + 1][j:j + 20])
        if bool(monstermid.match(midsli)):
            if bool(monstertop.match(topsli)):
                if bool(monsterlow.match(bottomsli)):
                    num_monsters += 1

num_waves = 0
for row in board_image:
    num_waves += row.count('#')

print(num_waves - (num_monsters * 15))