while True:
	x, y = list(map(int,input().split()))
	if x == 0 and y == 0:
		break
	else:
		if x <= y:
			print(x, y)
		else:
			print (y, x)

