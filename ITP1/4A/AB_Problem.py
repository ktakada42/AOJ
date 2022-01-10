a, b = list(map(int, input().split()))

d = int(a / b)
r = int(a % b)
f = float(a / b)

print(d, r, "{:.5f}".format(f))
