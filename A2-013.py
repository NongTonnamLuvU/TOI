x = str(input())
y = str(input())

km = x[2:]
if x[0] == "H":
    ck = 5*int(km)
elif x[0] == "O":
    ck = 3*int(km)
elif x[0] == "J":
    ck = 2*int(km)

R = [ 12, 18, 25]
T = [ 15, 20, 30]
M = [ 10, 15, 20]

cha = y[4:]
if y[0] == "R" and int(y[2]) > 0 and int(y[2]) < 3:
    c = R[int(y[2])-1] * int(cha)
elif y[0] == "T" and int(y[2]) > 0 and int(y[2]) < 3:
    c = T[int(y[2])-1] * int(cha)
elif y[0] == "M" and int(y[2]) > 0 and int(y[2]) < 3:
    c = M[int(y[2])-1] * int(cha)

if type(ck) == int and type(c) == int:
    print(ck+c)
else:
    exit()


