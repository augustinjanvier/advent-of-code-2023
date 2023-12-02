# https://adventofcode.com/2023/day/2

file_name = "input.txt"
file = open(file_name, "r")

result = 0
game_number = 0

for game in file:
    game = game.split("\n")[0]
    game = game.split(":")[1]

    min_blue = 0
    min_red = 0
    min_green = 0

    #set =  12 blue, 15 red, 2 green
    sets = game.split(";")
    for set in sets:
        dices = set.split(",")
        for dice in dices:
            tmp = dice.split(" ")
            dice_name = tmp[2]
            dice_number = int(tmp[1])
            if dice_name == "red":
                min_red = max(min_red, dice_number)
            if dice_name == "blue":
                min_blue = max(min_blue, dice_number)
            if dice_name == "green":
                min_green = max(min_green, dice_number)
    result += min_red * min_blue * min_green
print(result)    
            
                
