# https://adventofcode.com/2023/day/7

import time

start = time.time()

file_name = "input.txt"
file = open(file_name, "r")


def hand_numeric(line):
    hand = list(line[0])
    for index, card in enumerate(hand):
        card = card.replace("T","11")
        card = card.replace("J","1")
        card = card.replace("Q","13")
        card = card.replace("K","14")
        card = card.replace("A","15")
        hand[index] = card
    return hand

def get_hand_weight(line):
    #print("")
    #print("--", line[0], "--")
    hand = hand_numeric(line)

    initial_hand = hand

    max_occurences = 0
    max_card = '0'

    if '1' in hand:
        #print(" There is at least 1 J in this hand.")
        for index, card in enumerate(hand):
            if card != '1':
                card_count = line[0].count(line[0][index])
                if card_count > max_occurences:
                    max_card = card
                    max_occurences = max(card_count, max_occurences)
        hand = [max_card if x == '1' else x for x in hand]
    #print("   Max card is", max_card)

    max_occurences = 0

    for index, card in enumerate(hand):
        #card_count = line[0].count(line[0][index])
        card_count = hand.count(card)
        if card_count > max_occurences:
            max_card = card
            max_occurences = max(card_count, max_occurences)
        
    #print("   Max occurence is", max_occurences)
    length = 5 - len(set(hand))

    score = length

    if max_occurences >= 3:
        score += 1
    
    if score >= 4 and max_occurences >= 4:
        score += 1

    #print(" > score:", score)
    
    # score is 0 to 6, going from no duplicates to full hand.
    # now we can use this as a basis : score = 3 : 3 00 00 00 00 00,
    # where each 00 will be replace by the next card value (02 to 15)
    # and it will make a number we can easily sort the list on.
    
    initial_hand = list(map(int,initial_hand))
    weight = score * 10000000000
    weight += initial_hand[0] * 100000000
    weight += initial_hand[1] * 1000000
    weight += initial_hand[2] * 10000
    weight += initial_hand[3] * 100
    weight += initial_hand[4]
    #print(" > >", weight)
    return weight

game = []

for line in file:
    line = line.strip().split(" ")
    game.append(line)

game.sort(key=get_hand_weight)

result = 0
for index, hand in enumerate(game):
    result += (index + 1) * int(hand[1])

end = time.time()

print("Result :", result)
print("Time :", end - start, "seconds")