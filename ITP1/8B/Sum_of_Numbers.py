while True:
	x = input()
	if x == '0':
		break;
	else:
		sum = 0
		for d in x:
			sum += int(d)
		print(sum)
