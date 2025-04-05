i = input()

x = len(i)

z = []
c = 1

for j in range(1,x):
    if i[j] == i[j-1]: 
        c += 1
    else:
        z.append(str(c) + i[j-1])  
        c = 1

z.append(str(c) + i[x-1])

print(''.join(z))

