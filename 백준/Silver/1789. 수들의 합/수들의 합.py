s=int(input())
cnt=0
sum=0
for i in range (1,s+1):
    s-=i
    
    if (s < 0):
        break
    cnt+=1

print(cnt)