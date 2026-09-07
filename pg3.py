n1=int(input())
n2=int(input())
a=[int(input()) for i in range(n1)]
b=[int(input()) for i in range(n2)]
a.extend(b)
s=set(a)
l=sorted(s)
if len(l)%2!=0:
    i=len(l)//2
    print(l[i])
else:
    i=len(l)//2
    res=(l[i-1]+l[i])/2
    print(res)
