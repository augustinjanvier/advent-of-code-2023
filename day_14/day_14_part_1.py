# https://adventofcode.com/2023/day/14

file_name = "input.txt"
file = open(file_name)

dish_tmp = []

for line in file:
    line = line.strip()
    dish_tmp.append(line)


for line in dish_tmp:
    print(line)

print("")

dish = []
for line in dish_tmp[0]:
    dish.append("")
    
for line in dish_tmp:
    for index, char in enumerate(line):
        dish[index] += char

for index, line in enumerate(dish):
    dish[index] = line[::-1]
    print(line)

print("")

def boulders_right(line):
    finished = False
    while not finished:
        finished = True
        for i in range(len(line) - 1):
            if i < len(line):
                if line[i] == 'O' and line[i+1] == '.':
                    line = line[:i] + ".O" + line[i+2:]
                    finished = False
    return line

new_dish = []
for line in dish:
    new_dish.append(boulders_right(line))

for line in new_dish:
    print(line)

dish_final = []
for line in new_dish[0]:
    dish_final.append("")
    
for line in new_dish:
    for index, char in enumerate(line):
        dish_final[index] += char

print("")

result = 0
for index, line in enumerate(dish_final):
    for c in line:
        if c == 'O':
            result += index + 1

print(result)