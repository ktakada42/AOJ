while True:
	H, W = list(map(int, input().split()))
	if H == 0 and W == 0:
		break
	else:
		h = 1
		w = 1
		if H == 1 and W == 1:
			print("#")
		else:
			while h <= H:
				if h % 2 == 1:
					while w <= W:
						if w % 2 == 1:
							print("#", end='')
							w += 1
						else:
							print(".", end='')
							w += 1
					print()
					h += 1
					w = 1
				else:
					while w <= W:
						if w % 2 == 1:
							print(".", end='')
							w += 1
						else:
							print("#", end='')
							w += 1
					print()
					h += 1
					w = 1
		print()
