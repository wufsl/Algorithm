list1=[]
n=int(input())

for i in range(n):
    m=int(input())
    list1.append(m)

for i in range(n):
    for j in range(n):
        if(list1[i]<list1[j]):
            list1[i], list1[j] = list1[j], list1[i]

for i in list1:
    print(i)