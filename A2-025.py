w, l = map(int, input().split())
x, y = map(int, input().split())
v = int(input())

infected_rows = []
infected_cols = []
for i in range(v):
    p, j = map(int, input().split())
    infected_rows.append(p)
    infected_cols.append(j)

risk_map = [[0 for _ in range(l)] for _ in range(w)]

def update_risk(r, c, level, radius):
    for i in range(r - radius, r + radius + 1):
        for j in range(c - radius, c + radius + 1):
            if 0 <= i < w and 0 <= j < l:
                if max(abs(i - r), abs(j - c)) <= radius:
                    risk_map[i][j] = max(risk_map[i][j], level)

for idx in range(v):
    r, c = infected_rows[idx], infected_cols[idx]
    update_risk(r, c, 100, 0)
    update_risk(r, c, 60, 1)
    update_risk(r, c, 20, 2)

safe_count = sum(row.count(0) for row in risk_map)
bunny_risk = risk_map[x][y]

print(safe_count)
print(f"{bunny_risk}%")
