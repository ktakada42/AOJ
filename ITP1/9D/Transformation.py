str = input()
q = int(input())
for _ in range(q):
	q_order = input().split()
	a, b = map(int, q_order[1:3])
	if q_order[0] == "print":
		print(str[a:b + 1])
	elif q_order[0] == "reverse":
		reverse_str = str[::-1]
		str = str[:a] + reverse_str[len(str) - b - 1: len(str) - a] + str[b + 1:]
	else:
		replace_str = q_order[3]
		str = str[:a] + replace_str + str[b + 1:]
