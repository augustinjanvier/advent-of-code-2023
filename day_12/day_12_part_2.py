# https://adventofcode.com/2023/day/12

from functools import lru_cache

file_name = "input.txt"
file = open(file_name, "r")

@lru_cache(maxsize=None)
def get_arrangements_for_line(source, numbers, size = 0, has_to_work = False):
    if source == "":
        if numbers:
            if len(numbers) == 1 and numbers[0] == size:
                return 1
            return 0
        else:
            if size == 0:
                return 1
            return 0
    
    if len(numbers) == 0:
        if "#" in source or size > 0:
            return 0
        return 1

    spring = source[0]
    rest = source[1:]

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
        if has_to_work:
            return get_arrangements_for_line(rest, numbers, 0, False)
        if size == 0:
            return get_arrangements_for_line(rest, numbers, 0, False)
        if size != numbers[0]:
            return 0
        return get_arrangements_for_line(rest, numbers[1:], 0, False)
    return 0


def result():
    result = 0
    for line in file:
        line = line.strip().split(" ")

        sources = "?".join([line[0]] * 5)

        numbers = ",".join([line[1]] * 5)
        numbers = tuple(map(int, numbers.split(',')))

        result += get_arrangements_for_line(sources, numbers)
    return result

print(result())