card, speak = map(int,input().split())
numbers=list(map(int,input().split()))
cand=[]

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        for k in range(j+1,len(numbers)):
            num = numbers[i]+numbers[j]+numbers[k]
            if (num > speak):
                num=0
            cand.append(num)

print(max(cand))