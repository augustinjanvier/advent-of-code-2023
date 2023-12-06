# https://adventofcode.com/2023/day/6

file_name = "input_small.txt"
file = open(file_name, "r")

data = []

for line in file:
    line = line.strip().split(" ")
    line = list(filter(str.isnumeric, line))
    line = list(map(int, line))
    data.append(line)

races = []

for i in range(len(data[0])):
    races.append([data[0][i], data[1][i]])

races_distances = []

for race in races:
    race_distances = []
    minimum_distance = race[1]
    time = race[0]
    for i in range(0, time + 1):
        distance = (time - i) * i
        if distance > minimum_distance:
            race_distances.append(distance)
    races_distances.append(race_distances)

records = 1

for index, race_distance in enumerate(races_distances):
    records *= len(race_distance)

print(records)