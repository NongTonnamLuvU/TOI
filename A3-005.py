m, n = map(int, input().split())
v = []

for _ in range(n):
    l, r = map(int, input().split())
    v.append((l, 1))
    v.append((r + 1, -1))

v.sort()

mx = 0
count = 0
for i in range(len(v)):
    idx, k = v[i]
    count += k
    if i < len(v) - 1 and idx == v[i + 1][0]:
        continue
    mx = max(mx, count)

print(mx)
