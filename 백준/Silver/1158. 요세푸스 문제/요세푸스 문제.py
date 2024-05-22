n,k=map(int,input().split(' '))
list1=[]
for i in range(n):
    list1.append(i+1)
answer=[]
ind=0
for j in range(n):
    ind+=k-1
    if ind >= len(list1):
        ind = ind % len(list1)

    answer.append(list1.pop(ind))

print("<",end="")
for k in range(n-1):
    print(answer[k], end=", ")
print(answer[-1], end="")
print(">")
    