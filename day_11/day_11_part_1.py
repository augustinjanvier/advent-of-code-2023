# https://adventofcode.com/2023/day/11

import copy

file_name = "input.txt"
file = open(file_name, "r")

# 1 - expand the universe

universe = []

for line in file:
    line = line.strip()
    universe.append(list(line))
    if not '#' in line:
        universe.append(list(line))

expanded_universe = copy.deepcopy(universe)

inserted_lines = 0
for i in range(len(universe[0])):
    empty = True
    for line in universe:
        if line[i] == '#':
            empty = False
            break
    if empty:
        for index, _ in enumerate(universe):
            expanded_universe[index].insert(i + inserted_lines, ".")
        inserted_lines += 1

# 2 - store each galaxy's coordinates

galaxies = []

for y, line in enumerate(expanded_universe):
    for x, elt in enumerate(line):
        if elt == '#':
            galaxies.append((x,y))
        
print(galaxies)

def distance(g1, g2):
    x_distance = abs(g1[0] - g2[0])
    y_distance = abs(g1[1] - g2[1])
    return(x_distance + y_distance)

print("test", distance((4,0),(9,10)))

result = 0

for g1 in galaxies:
    for g2 in galaxies:
        if(g1 == g2):
            continue
        result += distance(g1,g2)

print(result/2)

# 3 - calculate distance bitween each galaxy.