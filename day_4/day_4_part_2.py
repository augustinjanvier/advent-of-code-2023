# https://adventofcode.com/2023/day/4

file_name = "input_small.txt"
file = open(file_name, "r")

def get_card_number(line):
    number = line.split(":")[0].split(" ")
    number = list(filter(('').__ne__, number))
    return number[1]

def get_winning_number(line):
    numbers = line.split(":")[1].split("|")[0].split(" ")
    numbers = list(filter(('').__ne__, numbers))
    return numbers

def get_player_numbers(line):
    numbers = line.split("|")[1].replace("\n", "").split(" ")
    numbers = list(filter(('').__ne__, numbers))
    return numbers

def get_won_card_numbers(card):
    card_number = card[0]
    winning_numbers = card[1]
    player_numbers = card[2]

    won_numbers = []
    cpt = 1
    for number in player_numbers:
        if number in winning_numbers:
            won_numbers.append(str(int(card_number) + cpt))
            cpt += 1
    return(won_numbers)

cards = []

players_card_numbers = []

# Initialization
for line in file:
    card_number = get_card_number(line)
    winning_numbers = get_winning_number(line)
    player_numbers = get_player_numbers(line)
    cards.append([card_number, winning_numbers, player_numbers])
    players_card_numbers.append(card_number)

won = True
while(won):
    won = False
    new_player_card_numbers = []
    for card_number in players_card_numbers:
        card = cards[int(card_number) - 1]
        won_card_numbers = get_won_card_numbers(card)
        if(won_card_numbers != []):
            won = True
            new_player_card_numbers += won_card_numbers
            print(new_player_card_numbers)
    players_card_numbers = new_player_card_numbers
    print("result:", players_card_numbers)
