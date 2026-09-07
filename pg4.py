n = input()
d = {'2': 'abc', '3': 'def', '4': 'ghi','5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
ans = [""]
for digit in n:
    temp = []
    for x in ans:
        for y in d[digit]:
            temp.append(x + y)
    ans = temp
if n=="":
    ans=[]
print(ans)
