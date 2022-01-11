while True:
	H, W = list(map(int,input().split()))
	if H == 0 and W == 0:
		break
	else:
		h = 0
		w = 0
		while h < H:
			while w < W - 1:
				print("#", end='')
				w += 1
			print("#")
			h += 1
			w = 0
		print()
