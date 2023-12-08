# https://adventofcode.com/2023/day/8

import time

start =time.time()

file_name = "input.txt"
file = open(file_name, "r")

directions = file.readline().strip()
file.readline()

tree = {}

for line in file:
    line = line.strip().replace("(","").replace(")","").split(" = ")
    key = line[0]
    left_right = line[1].split(", ")
    tree[key] = left_right

current_nodes = []

for key in tree:
    if(key[2] == 'A'):
        current_nodes.append(key)

print(current_nodes)

def get_child(key, direction):
    if direction == 'L':
        return tree[key][0]
    return tree[key][1]

z_steps = []

for node in current_nodes:
    completed = False
    step = 0
    while not completed:
        for dir in directions:
            step += 1
            node = get_child(node, dir)
            if node[2] == 'Z':
                z_steps.append(step)
                completed = True
                break

def pgcd(x,y):
    while(y):
        x, y = y, x % y
    return x

def lcm(x, y):
    lcm = (x*y)//pgcd(x, y)
    return lcm

result = z_steps[0]

for step in z_steps:
    result = lcm(result, step)

end = time.time()
print("result :", result)
print("time :", end - start, "seconds.")