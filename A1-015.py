x = str(input())
y = str(input())
z = int(input())

if len(x) > 5 and len(y) > 5:
    print(x[:2]+y[-1]+str(z)[-1])
else:
    print(x[0]+str(z)+y[-1])