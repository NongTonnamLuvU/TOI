x = int(input())
y = int(input())

c = ["winter", "spring", "summer", "fall" ,"winter"]
for i in c:
    if x in [1,2,3]:
        i = 0
    elif x in [4,5,6]:
        i = 1
    elif x in [7,8,9]:
        i = 2
    elif x in [10,11,12]:
        i = 3
    else:
        exit()

if x in [3,6,9,12] and y > 21:
    print(c[i+1])
else:
    print(c[i])
