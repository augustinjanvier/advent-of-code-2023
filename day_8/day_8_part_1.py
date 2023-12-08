# https://adventofcode.com/2023/day/7


file_name = "input_small.txt"
file = open(file_name, "r")

directions = file.readline().strip()
file.readline()

for line in file:
    line = line.strip()