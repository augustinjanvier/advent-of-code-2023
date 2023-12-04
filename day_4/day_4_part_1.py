# https://adventofcode.com/2023/day/4

file_name = "input.txt"
file = open(file_name, "r")

def get_winning_number(line):
    numbers = line.split(":")[1].split("|")[0].split(" ")
    numbers = list(filter(('').__ne__, numbers))
    return numbers

def get_player_numbers(line):
    numbers = line.split("|")[1].replace("\n", "").split(" ")
    numbers = list(filter(('').__ne__, numbers))
    return numbers

def get_points(winning_numbers, player_numbers):
    multiplyer = -1
    for number in player_numbers:
        if number in winning_numbers:
            multiplyer += 1
    if multiplyer >= 0:
        return pow(2, multiplyer)
    else:
        return 0

points = 0
for line in file:
    winning_numbers = get_winning_number(line)
    player_numbers = get_player_numbers(line)
    points += get_points(winning_numbers, player_numbers)
print(points)
