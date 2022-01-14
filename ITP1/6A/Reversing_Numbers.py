n = int(input())
a_array = list(map(int, input().split()))

i = n - 1
while i > 0:
	print(a_array[i], end=' ')
	i -= 1
print(a_array[0])
