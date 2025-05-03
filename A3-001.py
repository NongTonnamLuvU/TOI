import sys
sys.setrecursionlimit(10**6)

adj = [[] for _ in range(1005)]
ans = 0

def dfs(u):
    global ans
    a = []
    for t, v in adj[u]:
        if t == 1:
            a.append(v)
        else:
            a.append(dfs(v))
    ans += abs(a[0] - a[1])
    return 2 * max(a[0], a[1])

n = int(input())
x = []
for i in range(1, n + 1):
    a, l, b, r = map(int, input().split())
    adj[i].append((a, l))
    adj[i].append((b, r))
    if a == 1:
        x.append(l)
    if b == 1:
        x.append(r)

dfs(1)
print(ans)
