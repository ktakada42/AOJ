n = int(input())
taro = 0
hanako = 0
for _ in range(n):
	vs = input().split()
	if vs[0] > vs[1]:
		taro += 3
	elif vs[0] == vs[1]:
		taro += 1
		hanako += 1
	else:
		hanako += 3
print(taro, hanako)
