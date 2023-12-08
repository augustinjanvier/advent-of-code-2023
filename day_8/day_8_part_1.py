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

steps = 0

current_node = "AAA"

while current_node != "ZZZ":
    for dir in directions:
        steps += 1

        if dir == 'L':
            current_node = tree[current_node][0]

        else:
            current_node = tree[current_node][1]

        if current_node == "ZZZ":
            break

end = time.time()

print("result :", steps)
print("time :", end - start, "seconds.")