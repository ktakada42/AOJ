W, H, x, y, r = list(map(int, input().split()))

if x < r or y < r:
	print("No")
elif (x + r) > W or (y + r) > H:
	print("No")
else:
	print("Yes")
