W = input()
cnt = 0
while True:
	T = input()
	if T == "END_OF_TEXT":
		break
	else:
		T = list(T.lower().split())
		for _ in range(len(T)):
			if W == T[_]:
				cnt += 1
print(cnt)
