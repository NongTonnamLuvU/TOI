x = int(input())
f = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

if x < 1:
    print("Error : Please input positive number")
elif x == 0 or x > 10:
    print("Error : Out of range")
else:
    print(f[x-1])
