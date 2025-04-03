x = int(input())
y = str(input())
if len(y) == 1:
    if x < 18 or y == "s" or y == "S":
        print("20")
    else:
        print("50")
