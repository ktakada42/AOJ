import math

a, b, C = map(int, input().split())

radC = math.radians(C)
sinC = math.sin(radC)
cosS = math.cos(radC)
S = a * b / 2 * sinC

c_sq = a ** 2 + b ** 2 - 2 * a * b * cosS
c = math.sqrt(c_sq)
L = a + b + c
h = 2 * S / a
print(S, L, h)
