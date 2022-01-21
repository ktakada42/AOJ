r, c = map(int, input().split())
sheet = [list(map(int, input().split())) for _ in range(r)]

for i in range(r):
	row_sum = 0
	for j in range(c):
		row_sum += sheet[i][j]
		j += 1
	sheet[i].append(row_sum)
	i += 1
	j = 0

column_sum_array = [0]*(c + 1)
i = 0
j = 0
for j in range(c + 1):
	column_sum = 0
	for i in range(r):
		column_sum += sheet[i][j]
		i += 1
	column_sum_array[j] = column_sum
	i = 0
	j += 1
for _ in range(r):
	print(*sheet[_])
print(*column_sum_array)
