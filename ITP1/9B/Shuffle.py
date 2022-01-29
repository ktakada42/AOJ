while True:
	n = input()
	if n == '-':
		break
	else:
		m = int(input())
		h_list = [0] * m
		for _ in range(m):
			h_list[_] = int(input())
		for i in range(m):
			top_to_end_n = n[:h_list[i]]
			remain_n = n[h_list[i]:]
			n = remain_n + top_to_end_n
		print(n)
