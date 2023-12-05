# https://adventofcode.com/2023/day/5

file_name = "input_small.txt"
file = open(file_name, "r")

seeds_inital = file.readline().strip().split(": ")[1].split(" ")
seeds_inital = list(map(int, seeds_inital))

file.readline()
whole_map = []

current_map = []

# Rewrite the input in a readable table :
for line in file:
    line = line.strip()
    if line == "":
        current_map = sorted(current_map)
        whole_map.append(current_map)
        continue
    
    line = line.split(" ")

    if line[1] == "map:":
        current_map = []
        continue
    line = list(map(int, line))
    current_map.append(line)

current_map = sorted(current_map)
whole_map.append(current_map)

# Now we need to go through the whole table, going from the seed to find the location
def get_location_from_seed(seed, maps):
    source = seed
    for map in maps:
        destination = get_destination_from_source(source, map)
        source = destination
    return source

def get_destination_from_source(source, map):
    for combinaison in map:
        if source >= combinaison[1] and source <= combinaison[1] + combinaison[2]:
            return combinaison[0] + source - combinaison[1]
    return source

def process(pool, maps):
    for map in maps:
        good_pools = []

        first_seed = pool[0]
        last_seed = pool[1]

        first_seed_in_range = True if first_seed in range(map[1], map[1] + map[2] - 1) else False
        last_seed_in_range = True if last_seed in range(map[1], map[1] + map[2] - 1) else False

        if first_seed_in_range:
            if last_seed_in_range:
                print(first_seed, last_seed, "are in range of", range(map[1], map[1] + map[2] - 1))
                good_pools.append([first_seed + map[0] - map[1], last_seed + map[0] - map[1]])
            else:
                good_pools.append(process([first_seed + map[0] - map[1], map[0] + map[2] - 1], map))
            
        else:
            if last_seed_in_range:
                good_pools.append(process([map[1], last_seed + map[0] - map[1]], map))
                continue
            elif map[1] in range (first_seed, last_seed) and map[1] + map[2] - 1 in range(first_seed, last_seed):
                good_pools.append(process([map[1],map[0] + map[2] - 1], map))
                continue
    if good_pools == []:
        return [pool]
    return good_pools


mini = 999999999999999
i = 0
while i < len(seeds_inital):
    pool = [seeds_inital[i], seeds_inital[i] + seeds_inital[i + 1] - 1]
    good_pools = []
    for maps in whole_map:
        
        good_pools.append(process(pool, maps))
    i += 2
    print(good_pools)
