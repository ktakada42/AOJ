n = int(input())

hold_card = []
for _ in range(n):
	hold_suits, hold_num = input().split()
	hold_num = int(hold_num)
	hold_card.append((hold_suits, hold_num))
all_card = [(suits, number) for suits in ["S", "H", "C", "D"] for number in range(1, 14)]
for card in all_card:
	if card not in hold_card:
		print(*card)
