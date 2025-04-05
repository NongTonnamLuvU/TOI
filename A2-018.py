C , N = input().split()
N = int(N)

cm = ['R' , 'G', 'B']
cs = ['Red', 'Green', 'Blue']

si = cm.index(C)

R = []
for i in range(N):
    R.append(cs[(si+i)%3])
print(" ".join(R))
