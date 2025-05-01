x = int(input())

if x > 1582:
    if(x%4) == 0:
        if (x%100) == 0:
            if (x%400) == 0:
                print("yes")
            else:
                print("no")
        else:
            print("yes")
    else:
        print("no")
else:
    print("yes")
