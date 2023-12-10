# https://adventofcode.com/2023/day/10

file_name = "input.txt"
file = open(file_name, "r")

pipes_table = []

x = 0
y = 0

for line in file:
    line = line.strip()
    pipes_table.append(line)
    if 'S' in line:
        x = pipes_table.index(line)
        y = line.index("S")



loop_complete = False

def get_next_pipe(pipex, pipey, where_from, table):
    match table[pipex][pipey]:
        case "-":
            if where_from == 'left':
                return (pipex, pipey + 1, 'left')
            return (pipex, pipey - 1, 'right')
        case "|":
            if where_from == 'bottom':
                return (pipex - 1, pipey, 'bottom')
            return (pipex + 1, pipey, 'top')
        case "J":
            if where_from == 'left':
                return (pipex - 1, pipey, 'bottom')
            return (pipex, pipey - 1, 'right')
        case "F":
            if where_from == 'bottom':
                return (pipex, pipey + 1, 'left')
            return (pipex + 1, pipey, 'top')
        case "L":
            if where_from == 'top':
                return (pipex, pipey + 1, 'left')
            return (pipex - 1, pipey, 'bottom')
        case "7":
            if where_from == 'bottom':
                return (pipex, pipey - 1, 'right')
            return (pipex + 1, pipey, 'top')
        case "S":
            #checking top pipe
            pipe = table[x - 1][y]
            if pipe == "|" or pipe == "F" or pipe == "7":
                return (x - 1, y, 'bottom')

            #checking bottom pipe
            pipe = table[x + 1][y]
            if pipe == "|" or pipe == "J" or pipe == "L":
                return (x + 1, y, 'top')

            #checking right pipe
            pipe = table[x][y + 1]
            if pipe == "-" or pipe == "J" or pipe == "7":
                return (x, y + 1, 'left')

            #checking left pipe
            pipe = table[x][y - 1]
            if pipe == "-" or pipe == "L" or pipe == "F":
                return (x, y - 1, 'right')

where_from = 'none'

steps = 0

while not loop_complete:
    steps += 1
    pipe = get_next_pipe(x, y, where_from, pipes_table)
    print("Currently on", pipes_table[x][y], "in (" + str(x) + "," + str(y) + ")")
    x, y, where_from = pipe[0], pipe[1], pipe[2]

    if pipes_table[x][y] == "S":
        loop_complete = True

print("Completed", steps)
print("Farthest pipe is at", steps / 2)