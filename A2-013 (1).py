x = input().split()
y = input().split()

if len(x) < 2 or len(y) < 3:
    exit(1)

if not x[1].isdigit() or not y[1].isdigit() or not y[2].isdigit():
    exit(1)

km = int(x[1])

if x[0] == "H":
    ck = 5 * km
elif x[0] == "O":
    ck = 3 * km
elif x[0] == "J":
    ck = 2 * km
else:
    exit(1)

R = [12, 18, 25]
T = [15, 20, 30]
M = [10, 15, 20]

v = y[0]  
z = int(y[1])  
cha = int(y[2])  


if v == "R" and 1 <= z <= 3:
    c = R[z - 1] * cha
elif v == "T" and 1 <= z <= 3:
    c = T[z - 1] * cha
elif v == "M" and 1 <= z <= 3:
    c = M[z - 1] * cha
else:
    exit(1)

if isinstance(ck, int) and isinstance(c, int):
    print(ck + c)
else:
    exit(1)