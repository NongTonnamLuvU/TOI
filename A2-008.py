n = int(input())
car = []

for _ in range(n):
    a, b = map(int, input().split())
    car.append((a, b))

car.sort()
count = 0

for i in range(1, n):
    if car[i][1] < car[i - 1][1]:
        count += 1
    car[i] = (car[i][0], max(car[i][1], car[i - 1][1]))

print(count)
