while True:
	m, f, r = list(map(int, input().split()))
	if m == -1 and f == -1 and r == -1:
		break
	else:
		grading = 0
		if m == -1 or f == -1:
			grading = 'F'
		elif m + f >= 80:
			grading = 'A'
		elif m + f >= 65:
			grading = 'B'
		elif m + f >= 50:
			grading = 'C'
		elif m + f >= 30:
			if r >= 50:
				grading = 'C'
			else:
				grading = 'D'
		else:
			grading = 'F'
		print(grading)

