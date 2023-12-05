# https://adventofcode.com/2023/day/5

file_name = "input.txt"
file = open(file_name, "r")

seeds = file.readline().strip().split(": ")[1].split(" ")
seeds = list(map(int, seeds))
file.readline()
maps = []

current_map = []

# Rewrite the input in a readable table :
for line in file:
    line = line.strip()
    if line == "":
        current_map = sorted(current_map)
        maps.append(current_map)
        continue
    
    line = line.split(" ")

    if line[1] == "map:":
        current_map = []
        continue
    line = list(map(int, line))
    current_map.append(line)

current_map = sorted(current_map)
maps.append(current_map)

# Now we need to go through the whole table, going from the seed to find the location
def get_location_from_seed(seed, maps):
    source = seed
    for map in maps:
        destination = get_destination_from_source(source, map)
        source = destination
    return source

def get_destination_from_source(source, map):
    destination = source
    for combinaison in map:
        if source in range(combinaison[1],combinaison[1] + combinaison[2]):
            difference = destination - combinaison[1]
            destination = combinaison[0] + difference
            break
    return destination

locations = []

for seed in seeds:
    locations.append(get_location_from_seed(seed, maps))

locations = sorted(locations)
print(locations[0])
    
