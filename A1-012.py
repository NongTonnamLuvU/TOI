x = int(input())
y = input()
if (x >= 10 and x <= 99):
    x2 = int(str(x)[::-1])
    if y == "+":
        print(f"{x} + {x2} = {x+x2}")
    elif y == "*":
        print(f"{x} * {x2} = {x*x2}")