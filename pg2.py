N=int(input())
l1=list(map(int,input().split()))
n=int(input())
res=[]
for i in l1:
    binary=bin(i)[2:]
    binary=binary[:-n]
    if binary=="":
        res.append(0)
    else:
        res.append(int(binary,2))
print(*res)
