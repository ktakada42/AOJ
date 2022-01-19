while True:
	n, x = map(int, input().split())
	if n == 0 and x == 0:
		break
	else:
		i = 1
		j = 2
		k = 3
		count = 0
		while i <= n - 2:
			while j <= n - 1:
				while k <= n:
					if (i + j + k) == x:
						count += 1
					k += 1
				j += 1
				k = j + 1
			i += 1
			j = i + 1
			k = j + 1
	print(count)

