su=0
e=0
o=0
values = list(map(int, input().split()))
n=values[0]
if len(values)==2:
    b=values[1]
else:
    b=1
exp=str(n)
for i in range(n-1,b-1,-1):
    if (i+1)%2==0:
        e=e+1
        if e%2==1:
            exp+="//"+str(i)
        else:
            exp+="*"+str(i)
    else:
        o=o+1
        if o%2==1:
            exp+="+"+str(i)
        else:
            exp+="-"+str(i)
print(eval(exp))
