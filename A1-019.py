x = int(input())
y = int(input())
z = int(input())

if x == y == z:
    print("all the same")
elif x != y and y != z and x != z:
    print("all different")
else:
    print("neither")
    
