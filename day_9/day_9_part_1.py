# https://adventofcode.com/2023/day/9

file_name = "input.txt"
file = open(file_name, "r")

result = 0

for line in file:
    print("")
    line = line.strip().split(" ")
    line = list(map(int,line))
    table = [line]

    while not all(x == 0 for x in line):
        print("iterating for line :", line)
        sub_line = []
        for index, number in enumerate(line):
            if index < len(line) - 1:
                sub_line.append(line[index + 1] - number)
        table.append(sub_line)
        line = sub_line
        print(" > line is now :", line)


    table.reverse()
    print("")

    next_value = 0
    for line in table:
        next_value += line[len(line) - 1]
    result += next_value

print(result)