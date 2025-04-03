y1, m1, d1 = int(input()), int(input()), int(input())
y2, m2, d2 = int(input()), int(input()), int(input())

print("1" if (y1, m1, d1) < (y2, m2, d2) else "2" if (y1, m1, d1) > (y2, m2, d2) else "0")