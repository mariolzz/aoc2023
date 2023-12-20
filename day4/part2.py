from Card import Card

file_input = open("input", "r")
res = open("result2", "w")

lines = file_input.readlines()

for line in lines:
    line = line.replace("\n", "")

cards = []

for line in lines:
    card = Card()
    card.fromLine(line)
    cards.append(card)

total_ids_to_copy = {}

for card in cards:
    card.calc_points_and_copies()
    ids_to_copy = []
    if card.copy_num > 0:
        for i in range(card.id, card.id + card.copy_num):
            ids_to_copy.append(i + 1)

        print(f"Card {card.id} | Copies won: {card.copy_num} | {str(ids_to_copy)}")

        for id in ids_to_copy:
            try:
                total_ids_to_copy[id] += 1
            except:
                total_ids_to_copy[id] = 1

print(total_ids_to_copy)
total_cards = 0
for key in total_ids_to_copy:
    amount = total_ids_to_copy[key]
    print(f"{key}: {total_cards} + {amount}")
    total_cards += total_ids_to_copy[key]

res.write(str(total_cards))
