# https://adventofcode.com/2023/day/1

file_name = "input.txt"
file = open(file_name, "r")

res = 0
min_number = 0
max_number = 0

def get_string_in_digit(line, i):
    if i + 2 < len(line):
        substring = line[i:i+3]
        if substring == "one":
            return 1
        if substring == "two":
            return 2
        if substring == "six":
            return 6
    if i + 3 < len(line):
        substring = line[i:i+4]
        if substring == "four":
            return 4
        if substring == "five":
            return 5
        if substring == "nine":
            return 9
    if i + 4 < len(line):
        substring = line[i:i+5]
        if substring == "three":
            return 3
        if substring == "seven":
            return 7
        if substring == "eight":
            return 8
    return 0

def get_string_in_digit_reversed(line, i):
    if i - 2 >= 0:
        substring = line[i-2:i+1]
        if substring == "one":
            return 1
        if substring == "two":
            return 2
        if substring == "six":
            return 6
    if i - 3 >= 0:
        substring = line[i-3:i+1]
        if substring == "four":
            return 4
        if substring == "five":
            return 5
        if substring == "nine":
            return 9
    if i - 4 >= 0:
        substring = line[i-4:i+1]
        if substring == "three":
            return 3
        if substring == "seven":
            return 7
        if substring == "eight":
            return 8
    return 0


for line in file:

    line = line.replace('\n', '')

    # Trouvaille du premier digit de la ligne
    for i in range(len(line)):
        min_number = 0

        if line[i].isnumeric():
            min_number = int(line[i])
            break
            
        elif min_number == 0:
            min_number = get_string_in_digit(line, i)
            if min_number != 0:
                break
    
    # Trouvaille du dernier digit de la ligne
    for i in range(len(line)):
        # On inverse le compteur pour partir de la fin
        i = len(line) - i - 1
        max_number = 0

        if line[i].isnumeric():
            max_number = int(line[i])
            break
            
        elif max_number == 0:
            max_number = get_string_in_digit_reversed(line, i)
            if max_number != 0:
                break
            
    line_amount = int(str(min_number) + str(max_number))

    res += line_amount

print(res)

