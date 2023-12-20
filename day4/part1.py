from Card import Card

file_input = open("input", "r")
res = open("result1", "w")

lines = file_input.readlines()

for line in lines:
    line = line.replace("\n", "")

cards = []
winning_cards = []

for line in lines:
    card = Card()
    card.fromLine(line)
    cards.append(card)

for card in cards:
    card.calc_points_and_copies()

totalPoints = 0
for card in cards:
    totalPoints += card.points

res.write(str(totalPoints))
