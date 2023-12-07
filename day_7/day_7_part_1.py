# https://adventofcode.com/2023/day/7

file_name = "input.txt"
file = open(file_name, "r")


def hand_numeric(line):
    print("line:",line)
    hand = list(line[0])
    for index, card in enumerate(hand):
        card = card.replace("T","11")
        card = card.replace("J","12")
        card = card.replace("Q","13")
        card = card.replace("K","14")
        card = card.replace("A","15")
        hand[index] = card
    return hand

def get_hand_weight(line):
    hand = hand_numeric(line)
    print("hand:", hand)
    max_occurences = 0
    for index, _ in enumerate(hand):
        card_count = line[0].count(line[0][index])
        max_occurences = max(card_count, max_occurences)

    length = 5 - len(set(hand))

    score = length

    if max_occurences >= 3:
        score += 1
    
    if score >= 4 and max_occurences >= 4:
        score += 1
    
    # score is 0 to 6, going from no duplicates to full hand.
    # now we can use this as a basis : score = 3 : 3 00 00 00 00 00,
    # where each 00 will be replace by the next card value (02 to 15)
    # and it will make a number we can easily sort the list on.

    hand = list(map(int,hand))
    print(hand)
    weight = score * 10000000000
    weight += hand[0] * 100000000
    weight += hand[1] * 1000000
    weight += hand[2] * 10000
    weight += hand[3] * 100
    weight += hand[4]

    print(line[0], weight)

    return weight

game = []

for line in file:
    line = line.strip().split(" ")
    game.append(line)

game.sort(key=get_hand_weight)
print(game)

result = 0
for index, hand in enumerate(game):
    print(hand[1], "*", index + 1)
    result += (index + 1) * int(hand[1])

print(result)