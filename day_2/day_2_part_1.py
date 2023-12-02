# https://adventofcode.com/2023/day/2

file_name = "input.txt"
file = open(file_name, "r")

max_blue = 14
max_red = 12
max_green = 13

result = 0
game_number = 0

for game in file:
    game_possible = True
    game_number +=1
    game = game.split("\n")[0]
    game = game.split(":")[1]

    #set =  12 blue, 15 red, 2 green
    sets = game.split(";")
    for set in sets:
        if not game_possible:
            break
        dices = set.split(",")
        for dice in dices:
            tmp = dice.split(" ")
            dice_name = tmp[2]
            dice_number = int(tmp[1])
            if dice_name == "red" and dice_number > max_red:
                game_possible = False
                break
            if dice_name == "blue" and dice_number > max_blue:
                game_possible = False
                break
            if dice_name == "green" and dice_number > max_green:
                game_possible = False
                break
    if game_possible:
        result += game_number
print(result)    
            
                
