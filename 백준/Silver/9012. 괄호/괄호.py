n=int(input())
for i in range (n):
    sentence=input()
    cnt=0
    for j in range(len(sentence)):
        if (sentence[j]=='('):
            cnt+=1
        elif (sentence[j]==')'):
            cnt-=1
        if (cnt<0):
            break

    if (cnt==0):
        print('YES')
    else:
        print('NO')