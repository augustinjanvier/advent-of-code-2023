# https://adventofcode.com/2023/day/3

import re

file_name = "input.txt"
file = open(file_name, "r")

engine = []

def get_adjacent_numbers(line_index, char_index, engine):
    numbers = []
    line_self = engine[line_index][char_index-1:char_index+2]
    line_self_full = get_potential_line(line_index, char_index, engine)
    numbers.extend(get_full_numbers(line_self, line_self_full))
    if line_index != 0:
        line_up = engine[line_index-1][char_index-1:char_index+2]
        line_up_full = get_potential_line(line_index-1, char_index, engine)
        numbers.extend(get_full_numbers(line_up, line_up_full))
    if line_index != (len(engine) - 1):
        line_down = engine[line_index + 1][char_index-1:char_index+2]
        line_down_full = get_potential_line(line_index+1, char_index, engine)
        numbers.extend(get_full_numbers(line_down, line_down_full))
    return numbers

def get_potential_line(line_index, char_index, engine):
    substring = engine[line_index][char_index-3:char_index+4]
    return(substring)

def get_full_numbers(line_partial, line_full):
    numbers = []

    if not line_partial[1].isdigit():
        if line_partial[0].isdigit():
            n = line_full[0:3].replace(".","").replace("*","")
            numbers.append(int(n))
        if line_partial[2].isdigit():
            n = line_full[4:7].replace(".","").replace("*","")
            numbers.append(int(n))
    
    else:
        if line_partial[0].isdigit() and line_partial[2].isdigit():
            print(line_full)
            n = line_full[2:5]
            numbers.append(int(n))
        elif line_partial[0].isdigit():
            n = line_full[1:4].replace(".","").replace("*","")
            numbers.append(int(n))
        elif line_partial[2].isdigit():
            n = line_full[3:6].replace(".","").replace("*","")
            numbers.append(int(n))
        else:
            n = line_partial[1]
            numbers.append(int(n))

    return numbers

# Prepare engine
for line in file:
    line = line[0: len(line) - 1]
    line = re.sub("[^.0-9*]", "$",line)
    print(line)
    engine.append(line)

numbers = []
# Iterate on engine
for line_index, line in enumerate(engine):
    for char_index, char in enumerate(line):
        if char == "*":
            numbers.append(get_adjacent_numbers(line_index, char_index, engine))

ratio = 0
for gear in numbers:
    if len(gear) == 2:
        ratio += gear[0] * gear[1]

print(ratio)