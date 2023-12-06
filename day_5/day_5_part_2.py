# https://adventofcode.com/2023/day/5

import numbers
import time
import re

start = time.time()

file_name = "input.txt"
file = open(file_name, "r")

# Initialize seeds table

tmp = file.readline().strip().split(": ")[1].split(" ")
tmp = list(map(int,tmp))
seeds = []
for i in range(len(tmp)):
    if i % 2 != 0:
        continue
    seeds.append([tmp[i], tmp[i] + tmp[i+1] - 1])

file.readline()

maps_list = []
current_map = []

def convert_line_to_map_entry(line):
    line = list(map(int, line.split(" ")))
    map_entry = [line[1], line[1] + line[2] - 1, line[0] - line[1]]
    
    return map_entry

for line in file:
    line = line.strip()
    if re.findall(":", line) != []:
        # Then line is "source-to-dest map:", this is the beginning of a map
        current_map = []
        continue
    if line == "":
        # Then line is empty, this is the end of a map
        current_map = sorted(current_map)
        maps_list.append(current_map)
        continue
    map_entry = convert_line_to_map_entry(line)
    current_map.append(map_entry)
current_map = sorted(current_map)
maps_list.append(current_map)

# maps_list :
# [[[50, 97, +2], [98, 99, -48]], [[0, 14, +39], ...
# means :
#   first map (seed-to-soil map) is [[50, 97, 2], [98, 99, -48]]
#       - from seed 50 to seed 97, do +2
#       - from seed 98 to seed 99, do -48
#       - otherwise, keep the same seed number

# We have the same for seeds : [[79, 92], [55, 67]] means we go through seed 79 to 92, and through seed 55 to 67.

# Now we need to use the map seed-to-soil to get the soils intervals from the seed interval :
# seeds : [79, 92]
# seed-to-soil map : [[50, 97, 2], [98, 99, -48]]
# minimum_source = 79
# maximum_source = 92

# is the whole [79, 92] interval contained in [50, 97] ? Yes
# then it means the soils interval is : [79 + 2, 92 + 2] = [81, 94]

# then, do th same with next source-to-dest map, until the last one to get an interval of locations, and take the minimum value of this interval.
# Note that the interval can be split in several intervals, so it has to be reccursive. For example, let's try with seeds interval [25, 59] :

# is the whole [25, 59] interval contained in [50, 97] ? No
# so we split the seeds interval in two intervals [25, 49] [50, 59] :
# now, is [25, 49] in [50, 97] ? Not at all, so is this in [98, 99] ? No
# so interval [25, 49] stays [25, 49].
# now is interval [50, 59] in [50, 97] ? Yes
# so interval [50, 49] becomes [52, 59]
# so now we have soils intervals : [25, 49] [52, 59]. We can go through those 2 interval with the next source-to-dest map, and so on.
# at the end we have a lot of locations intervals for one interval of seeds.
# we need to find the minimum value of those intervals, it will be a very fast program.

def get_destination_intervals(source_interval, map):
    # map = [[10, 15, -1], [41, 65, +6], [85, 86, -50]]

    #print("")
    #print("starting interval :", source_interval)
    #print("map is", map)

    for destination_interval in map:
        
        #print("  testing on map", destination_interval)

        source_x = source_interval[0]
        source_y = source_interval[1]
        dest_x = destination_interval[0]
        dest_y = destination_interval[1]
        modifier = destination_interval[2]

        # if whole interval is included in destination
        if (source_x >= dest_x) and (source_y <= dest_y):
            #print("  > whole inside !")
            return [[source_x + modifier, source_y + modifier]]
        
        # if interval is out by right side
        if (source_x >= dest_x) and (source_x <= dest_y) and (source_y > dest_y):
            #print("  > out by right !")
            out_of_bound_interval = [dest_y + 1, source_y]
            interval = [[source_x + modifier, dest_y + modifier]]
            interval.extend(get_destination_intervals(out_of_bound_interval, map))
            return interval

        # if inteval is out by left side
        if (source_x < dest_x) and (source_y <= dest_y) and (source_y > dest_x):
            #print("  > out by left !")
            out_of_bound_interval = [source_x, dest_x - 1]
            interval = [[dest_x + modifier, source_y + modifier]]
            interval.extend(get_destination_intervals(out_of_bound_interval, map))
            return interval
        
        # if interval is out by both sides
        if (source_x < dest_x) and (source_y > dest_y):
            #print("  > out by both sides !")
            out_of_bound_left = [source_x, dest_x - 1]
            out_of_bound_right = [dest_y + 1, source_y]
            interval = [[dest_x + modifier, dest_y + modifier]]
            interval.extend(get_destination_intervals(out_of_bound_left, map))
            interval.extend(get_destination_intervals(out_of_bound_right, map))
            return interval
        
        # if whole interval is out of destination
        if (source_x < dest_x) or (source_y > dest_y):
            #print("  > whole outside !")
            continue
    
    return [source_interval]


# seed = [X,Y], map = whole map
def get_seed_locations_interval(seed):
    intervals = [seed]

    for map in maps_list:
        new_intervals = []
        for interval in intervals:
            new_interval = get_destination_intervals(interval, map)
            new_intervals.extend(new_interval)
        #print("    destinations are:", new_intervals)
        intervals = new_intervals
    return intervals

result_intervals = []

for seed in seeds:
    result_intervals.append(get_seed_locations_interval(seed))

# Sorting data & getting minimum value:
sorted_intervals = []
for intervals in result_intervals:
    sorted_intervals.extend(intervals)

result = sorted(sorted_intervals)[0][0]

end = time.time()

print("Result is", result)
print("Time :", end - start, "seconds")
