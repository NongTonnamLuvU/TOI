x = input().split()
y = input().split()


if len(x) < 2 or len(y) < 2 or not x[0].isupper() or not y[0].isupper() or not x[0].isalpha() or not y[0].isalpha():
    exit(1)

a, l = x[0], x[1]  
c, v = y[0], y[1]  


if not x[1].isdigit() or not y[1].isdigit() or len(l) != 5 or len(v) != 5 or len(a) != 1 or len(c) != 1:
    exit(1)

if x == y:
    print("1000000") 
elif a == c:
    if l[3:] == v[3:]:
        print("1000")  
    elif l[2:] == v[2:]:
        print("2000")  
    else:
        print("20") 
elif l == v:
    print("100000")  
elif l[3:] == v[3:]:
    print("100") 
elif l[2:] == v[2:]:
    print("200") 
else:
    print("0")