while True:
	H, W = list(map(int,input().split()))
	if H == 0 and W == 0:
		break
	else:
		h = 1
		w = 1
		while w < W:
			print("#", end='')
			w += 1
		print("#")
		h += 1
		w = 1
		while h < H:
			if w == 1:
				print("#", end='')
				w += 1
			elif w < W:
				print(".", end='')
				w += 1
			else:
				print("#")
				h += 1
				w = 1
		if h == H:
			while w < W:
				print("#", end='')
				w += 1
		print("#")
		print()
