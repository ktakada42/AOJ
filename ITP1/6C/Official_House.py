residents = [[[0 for room in range(10)] for floor in range(3)] for bldg in range(4)]
n = int(input())
for _ in range(n):
	b, f, r, v = list(map(int,input().split()))
	residents[b - 1][f - 1][r - 1] += v
i, j, k = 0, 0, 0
while i < 4:
	while j < 3:
		while k < 10:
			print('', residents[i][j][k], end='')
			k += 1
		print()
		k = 0
		j += 1
	if i != 3:
		print("####################")
	i += 1
	j = 0
