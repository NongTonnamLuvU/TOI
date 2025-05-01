n, passed = map(int, input().split())

# Create and fill the tour matrix (1-indexed for easier translation from C++)
tour = [[0] * (n + 1)]
for _ in range(n):
    tour.append([0] + list(map(int, input().split())))

checklist = list(range(1, n + 1))

while len(checklist) > 1:
    winner = []
    for i in range(0, len(checklist), 2):
        x, y = checklist[i], checklist[i + 1]
        if tour[x][y] == x:
            if passed == y:
                passed = 0
                winner.append(y)
            else:
                winner.append(x)
        else:
            if passed == x:
                passed = 0
                winner.append(x)
            else:
                winner.append(y)
    checklist = winner

print(checklist[0])
