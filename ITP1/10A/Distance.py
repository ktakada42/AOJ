import math

x1, y1, x2, y2 = map(float, input().split())

distance_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2
distance = math.sqrt(distance_sq)
print(distance)
