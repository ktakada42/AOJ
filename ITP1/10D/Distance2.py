n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

for p in range(1, 4):
	print((sum([abs(a - b) ** p for a, b in zip(x, y)]) ** (1 / p)))

print(max([abs(a - b) for a, b in zip(x, y)]))
