# https://adventofcode.com/2023/day/1

file_name = "input.txt"
file = open(file_name, "r")

res = 0
min_number = 0
max_number = 0

def get_digit(substring):
    strings = ["one","two","three","four","five","six","seven","eight","nine"]
    numbers = [1,2,3,4,5,6,7,8,9]
    if substring in strings:
        return numbers[strings.index(substring)]
    return 0

def get_string_in_digit(line, i):
    if i + 2 < len(line):
        substring = get_digit(line[i:i+3])
        if substring != 0:
            return substring
    if i + 3 < len(line):
        substring = get_digit(line[i:i+4])
        if substring != 0:
            return substring
    if i + 4 < len(line):
        substring = get_digit(line[i:i+5])
        if substring != 0:
            return substring
    return 0

def get_string_in_digit_reversed(line, i):
    if i - 2 >= 0:
        substring = get_digit(line[i-2:i+1])
        if substring != 0:
            return substring
    if i - 3 >= 0:
        substring = get_digit(line[i-3:i+1])
        if substring != 0:
            return substring
    if i - 4 >= 0:
        substring = get_digit(line[i-4:i+1])
        if substring != 0:
            return substring
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

