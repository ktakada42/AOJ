import math

while True:
	n = int(input())
	if n == 0:
		break
	s = list(map(int, input().split()))
	total = 0
	for i in range(n):
		total += s[i]
	m = total / n
	a_sqn = 0
	for j in range(n):
		a_sqn += (s[j] - m) ** 2
	a_sq = a_sqn / n
	a = math.sqrt(a_sq)
	print(a)
