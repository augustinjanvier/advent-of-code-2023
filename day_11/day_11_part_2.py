# https://adventofcode.com/2023/day/11

import copy

file_name = "input.txt"
file = open(file_name, "r")

# 1 - expand the universe

universe = []

empty_lines = []
empty_columns = []

for index, line in enumerate(file):
    line = line.strip()
    universe.append(list(line))
    if not '#' in line:
        empty_lines.append(index)

for line in universe:
    print(line)

for i in range(len(universe[0])):
    empty = True
    for line in universe:
        if line[i] == '#':
            empty = False
            break
    if empty:
        empty_columns.append(i)


print(empty_lines)
print(empty_columns)

# 2 - store each galaxy's coordinates

galaxies = []

for y, line in enumerate(universe):
    for x, elt in enumerate(line):
        if elt == '#':
            galaxies.append((x,y))
        
print(galaxies)

empty_modifier = 1000000

def x_distance(x1, x2):
    min_x = min(x1,x2)
    max_x = max(x1,x2)
    x_distance = max_x - min_x
    
    for i in empty_columns:
        if i in range(min_x, max_x):
            x_distance += empty_modifier - 1
    return x_distance

def y_distance(y1, y2):
    min_y = min(y1,y2)
    max_y = max(y1,y2)
    y_distance = max_y - min_y
    
    for i in empty_lines:
        if i in range(min_y, max_y):
            y_distance += empty_modifier - 1
    return y_distance

def distance(g1, g2):
    x = x_distance(g1[0], g2[0])
    y = y_distance(g1[1], g2[1])
    return(x + y)

print("test", distance((4,0),(9,10)))

result = 0

for g1 in galaxies:
    for g2 in galaxies:
        if(g1 == g2):
            continue
        result += distance(g1,g2)

print(int(result/2))

# 3 - calculate distance bitween each galaxy.