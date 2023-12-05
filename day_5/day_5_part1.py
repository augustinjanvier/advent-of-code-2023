# https://adventofcode.com/2023/day/5

file_name = "input_small.txt"
file = open(file_name, "r")

seeds = file.readline().strip().split(": ")[1].split(" ")
file.readline()
map = []

current_map = []

# Rewrite the input in a readable table :
for line in file:
    line = line.strip()
    if line == "":
        print("space")
        map.append(current_map)
        continue
    
    line = line.split(" ")

    if line[1] == "map:":
        current_map = []
        print("map line")
        continue
    
    current_map.append(line)

# Now we need to go through the whole table, going from the seed to find the location

    