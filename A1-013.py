x = str(input())
y = int(input())

if x == "H" and y == 4567:
    print("safe unlocked")
elif x == "H":
    print("safe locked - change digit")
elif y == 4567:
    print("safe locked - change char")
else:
    print("safe locked")