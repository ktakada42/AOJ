n, m, l = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(m)]
for i in range(n):
	c = []
	for j in range(l):
		tmp = 0
		for k in range(m):
			tmp += a[i][k] * b[k][j]
		c.append(tmp)
	print(*c)
