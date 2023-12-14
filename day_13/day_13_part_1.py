# https://adventofcode.com/2023/day/13

file_name = "input.txt"
file = open(file_name)

patterns_list = []

# Filling patterns_list to be able to work with data
pattern = []
for line in file:
    line = line.strip()

    if line == "":
        patterns_list.append(pattern)
        pattern = []
        continue

    pattern.append(line)
patterns_list.append(pattern)

def horizontal_symmetry(pattern):
    for index in range(1, len(pattern)):
        one = pattern[:index]
        two = pattern[index:]
        if len(one) >len(two):
            one = one[len(one) - len(two):]
        if len(two) > len(one):
            two = two[:len(one)]
        two.reverse()
        if (one == two):
            return len(pattern[:index])
    return 0

def vertical_symmetry(pattern):
    new_pattern = []
    for line in pattern[0]:
        new_pattern.append("")
    
    for line in pattern:
        for index, char in enumerate(line):
            new_pattern[index] += char
    return(horizontal_symmetry(new_pattern))

result = 0
for pattern in patterns_list:
    result += vertical_symmetry(pattern)
    result += 100 * horizontal_symmetry(pattern)

print(result)