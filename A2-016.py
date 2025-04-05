x = input().split()
y = input().split()


if len(x) < 2 or len(y) < 2 or not x[0].isupper() or not y[0].isupper() or not x[0].isalpha() or not y[0].isalpha():
    exit(1)

a, l = x[0], x[1]  
c, v = y[0], y[1]  


if x == y:
    print(1000000)
elif l == v:
    print(100000) 
elif a == c and v[-3:] == l[-3:]:
    print(2000)  
elif a == c and v[-2:] == l[-2:]:
    print(1000) 
elif v[-3:] == l[-3:]:
    print(200) 
elif v[-2:] == l[-2:]:
    print(100)  
elif a == c:
    print(20) 
else:
    print(0)  
