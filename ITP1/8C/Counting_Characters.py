import sys

original_txt = sys.stdin.read()
original_txt = original_txt.lower()

cnt = [0]*26
letters = [0]*26
for _ in range(26):
	letters[_] = chr(_ + 97)
for x in original_txt:
	i = 0
	for y in letters:
		if x == y:
			cnt[i] += 1
		i += 1

for i in range(26):
	print(letters[i], ":", cnt[i])
