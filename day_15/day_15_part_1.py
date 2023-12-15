# https://adventofcode.com/2023/day/15

file_name = "input.txt"
file = open(file_name)

steps = file.readline().split(",")

def step_value(step):
    result = 0
    for c in step:
        result += ord(c)
        result *= 17
        result %= 256
    return result


res = 0
for step in steps:
    res += step_value(step)

print(res)