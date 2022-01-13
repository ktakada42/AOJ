n = int(input())

i = 1
checker = 0
while i <= n:
	if i % 3 == 0:
		checker = 1
	elif i / 1000 >= 1:
		if int(i / 1000) == 3:
			checker = 1
		elif int(i % 1000 / 100) == 3:
			checker = 1
		elif int(i % 1000 % 100 / 10) == 3:
			checker = 1
		elif i % 1000 % 100 % 10 == 3:
			checker = 1
	elif i / 100 >= 1:
		if int(i / 100) == 3:
			checker = 1
		elif int(i % 100 / 10) == 3:
			checker = 1
		elif i % 100 % 10 == 3:
			checker = 1
	elif i / 10 >= 1:
		if int(i / 10) == 3:
			checker = 1
		elif i % 10 == 3:
			checker = 1
	if checker == 1:
		print(" ", i, end='')
	i += 1
	checker = 0
