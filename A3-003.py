n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

x, y = 1, 1
count = 0

for i in range(n):
    xx = a[i]
    yy = b[i]
    p, pp = x, xx
    q, qq = y, yy

    if p > pp:
        p, pp = pp, p
    if q > qq:
        q, qq = qq, q

    if p == q and pp == qq:
        count += 1
    elif p != q and p != qq and pp != q and pp != qq:
        if p < q and pp > q and pp < qq:
            count += 1
        elif q < p and qq > p and qq < pp:
            count += 1

    x, y = xx, yy

print(count)
