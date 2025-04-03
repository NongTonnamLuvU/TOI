p = ["a", "e", "i", "o", "u"]
a = input()

if a.islower() and len(a) == 1:
    if a in p:
        print("yes")
    else:
        print("no")
