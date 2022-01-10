a, b, c = list(map(int, input().split()))
array = a, b, c
sorted_array = sorted(array)
num_of_array = len(sorted_array)
i = 0
while i < num_of_array - 1:
	print(sorted_array[i], end = ' ')
	i += 1
print(sorted_array[i])
