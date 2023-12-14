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

def is_single_difference(one, two):
    number_of_differences = 0
    for index in range(len(one)):
        if one[index] == two[index]:
            continue
        for i, _ in enumerate(one[index]):
            if one[index][i] != two[index][i]:
                number_of_differences += 1
    return number_of_differences == 1

def horizontal_symmetry(pattern):
    for index in range(1, len(pattern)):
        one = pattern[:index]
        two = pattern[index:]
        if len(one) >len(two):
            one = one[len(one) - len(two):]
        if len(two) > len(one):
            two = two[:len(one)]
        two.reverse()
        if is_single_difference(one, two):
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