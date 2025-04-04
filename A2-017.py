x = input().split()
y = input().split()

if len(x) < 2:
    exit(1)

S = [60,80]
M = [80,100]
L = [100,120]

a, l = x[0], x[1]  
c = y[0]


if a == "S":
    if l == "R":
        i = S[0]
    elif l == "T":
        i = S[1]
elif a == "M":
    if l == "R":
        i = M[0]
    elif l == "T":
        i = M[1]
elif a == "L":
    if l == "R":
        i = L[0]
    elif l == "T":
        i = L[1]
else:
    exit(1)

if c == "N":
    k = 0
elif len(y) < 2 or not y[0].isalpha or not y[0].isupper or not y[1].isdigit:
    exit(1)
elif c == "P":
    k = 15*int(y[1])
elif c == "E":
    k = 10*int(y[1])
else:
    exit(1)
print(i+k)
