# https://adventofcode.com/2023/day/12

file_name = "input.txt"
file = open(file_name, "r")

def get_arrangements_for_line(line, numbers, size = 0, has_to_work = False):
    if line == "":
        if numbers:
            if len(numbers) == 1 and numbers[0] == size:
                return 1
            return 0
        else:
            if size == 0:
                return 1
            return 0
    
    if len(numbers) == 0:
        if "#" in line or size > 0:
            return 0
        return 1

    spring = line[0]
    rest = line[1:]

    if spring == "?":
        return get_arrangements_for_line("#" + rest, numbers, size, has_to_work) + get_arrangements_for_line("." + rest, numbers, size, has_to_work)

    if spring == "#":
        if has_to_work:
            return 0
        size = size + 1

        if size > numbers[0]:
            return 0
        if size == numbers[0]:
            return get_arrangements_for_line(rest, numbers[1:], 0, True)
        return get_arrangements_for_line(rest, numbers, size, False)
    
    if spring == ".":
        if has_to_work or size == 0:
            return get_arrangements_for_line(rest, numbers, 0, False)
        if size != numbers[0]:
            return 0
        return get_arrangements_for_line(rest, numbers[1:], 0, False)
    return 0


result = 0

for line in file:
    line = line.strip().split(" ")

    sources = line[0]

    numbers = list(map(int, line[1].split(',')))
    arrangements = get_arrangements_for_line(sources, numbers)
    print(line, arrangements)
    result += arrangements

print(result)